from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MEDIA_DIR = ROOT / "media"


@dataclass(frozen=True)
class Fingerprint:
    path: Path
    sha256: str
    frame_hashes: tuple[int, ...]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def dhash(frame: bytes) -> int:
    """Return a 64-bit difference hash for one 9x8 grayscale frame."""
    value = 0
    for row in range(8):
        offset = row * 9
        for col in range(8):
            value = (value << 1) | (frame[offset + col] > frame[offset + col + 1])
    return value


def frame_hashes(path: Path, fps: float) -> tuple[int, ...]:
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        raise RuntimeError("ffmpeg is required but was not found on PATH")

    command = [
        ffmpeg,
        "-v",
        "error",
        "-i",
        str(path),
        "-vf",
        f"fps={fps},scale=9:8:flags=area,format=gray",
        "-f",
        "rawvideo",
        "-pix_fmt",
        "gray",
        "-",
    ]
    result = subprocess.run(command, capture_output=True, check=True)
    frame_size = 9 * 8
    data = result.stdout
    return tuple(
        dhash(data[index : index + frame_size])
        for index in range(0, len(data) - frame_size + 1, frame_size)
    )


def fingerprint(path: Path, fps: float) -> Fingerprint:
    return Fingerprint(path=path, sha256=sha256(path), frame_hashes=frame_hashes(path, fps))


def hamming(left: int, right: int) -> int:
    return (left ^ right).bit_count()


def directional_similarity(candidate: Fingerprint, existing: Fingerprint) -> tuple[float, float]:
    """Measure whether candidate frames occur anywhere in an existing video.

    The directional comparison intentionally detects a short clip embedded inside
    a longer compilation, not only two videos with equal duration.
    """
    if not candidate.frame_hashes or not existing.frame_hashes:
        return 0.0, 64.0
    distances = [
        min(hamming(candidate_hash, existing_hash) for existing_hash in existing.frame_hashes)
        for candidate_hash in candidate.frame_hashes
    ]
    close_ratio = sum(distance <= 6 for distance in distances) / len(distances)
    mean_distance = sum(distances) / len(distances)
    return close_ratio, mean_distance


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Compare candidate videos with repository media using exact and sampled-frame hashes."
    )
    parser.add_argument("candidates", nargs="+", type=Path)
    parser.add_argument("--fps", type=float, default=1.0, help="sample rate used for visual hashes")
    parser.add_argument("--top", type=int, default=5, help="number of nearest repository videos to print")
    parser.add_argument(
        "--fail-on-match",
        action="store_true",
        help="exit non-zero when an exact or high-confidence visual duplicate is found",
    )
    args = parser.parse_args()

    candidates = [path.resolve() for path in args.candidates]
    missing = [str(path) for path in candidates if not path.is_file()]
    if missing:
        parser.error(f"candidate video not found: {', '.join(missing)}")

    existing_paths = sorted(MEDIA_DIR.glob("*.mp4"))
    existing = [fingerprint(path, args.fps) for path in existing_paths]
    found_duplicate = False
    report: list[dict[str, object]] = []

    for candidate_path in candidates:
        candidate = fingerprint(candidate_path, args.fps)
        comparisons: list[dict[str, object]] = []
        for item in existing:
            exact = candidate.sha256 == item.sha256
            close_ratio, mean_distance = directional_similarity(candidate, item)
            likely_duplicate = exact or (close_ratio >= 0.8 and mean_distance <= 6.0)
            found_duplicate = found_duplicate or likely_duplicate
            comparisons.append(
                {
                    "path": item.path.relative_to(ROOT).as_posix(),
                    "exact": exact,
                    "close_frame_ratio": round(close_ratio, 3),
                    "mean_nearest_hamming": round(mean_distance, 3),
                    "likely_duplicate": likely_duplicate,
                }
            )
        comparisons.sort(
            key=lambda row: (
                not bool(row["likely_duplicate"]),
                -float(row["close_frame_ratio"]),
                float(row["mean_nearest_hamming"]),
            )
        )
        report.append(
            {
                "candidate": str(candidate_path),
                "sha256": candidate.sha256,
                "sampled_frames": len(candidate.frame_hashes),
                "nearest": comparisons[: args.top],
            }
        )

    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if args.fail_on_match and found_duplicate else 0


if __name__ == "__main__":
    sys.exit(main())
