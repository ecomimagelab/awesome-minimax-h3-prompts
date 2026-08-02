from __future__ import annotations

from collections import Counter, defaultdict
from html import escape
from pathlib import PurePosixPath

from library import ROOT, load_categories, load_prompts


SITE_DIR = ROOT / "site"
SITE_URL = "https://ecomimagelab.github.io/awesome-minimax-h3-prompts/"
REPO_URL = "https://github.com/ecomimagelab/awesome-minimax-h3-prompts"


def video_anchor(path: str) -> str:
    return f"video-{PurePosixPath(path).stem}"


def mode_labels(categories: dict, mode: str) -> tuple[str, str]:
    labels = categories["modes"][mode]
    return labels["en"], labels["zh"]


def prompt_block(item: dict, categories: dict) -> str:
    mode_en, mode_zh = mode_labels(categories, item["mode"])
    reconstructed = item["prompt"].get("reconstructed_from_video") is True
    badge_en = "Reconstructed from video" if reconstructed else "Source prompt"
    badge_zh = "视频反推" if reconstructed else "来源原文"
    notice = "" if not reconstructed else (
        '<p class="reconstructed lang-en">Editorial reconstruction, not the creator’s published prompt.</p>'
        '<p class="reconstructed lang-zh">编辑反推内容，并非创作者发布的原始提示词。</p>'
    )
    return f"""
      <details class="prompt" id="{escape(item['id'], quote=True)}" open>
        <summary>
          <span class="prompt-id">{escape(item['id'].upper())}</span>
          <span class="lang-en">{escape(item['title']['en'])}</span>
          <span class="lang-zh">{escape(item['title']['zh'])}</span>
          <span class="pill lang-en">{escape(mode_en)}</span>
          <span class="pill lang-zh">{escape(mode_zh)}</span>
        </summary>
        <div class="prompt-body">
          <p class="description lang-en">{escape(item['description']['en'])}</p>
          <p class="description lang-zh">{escape(item['description']['zh'])}</p>
          <div class="prompt-label"><span class="lang-en">{badge_en}</span><span class="lang-zh">{badge_zh}</span></div>
          {notice}
          <pre class="lang-en"><code>{escape(item['prompt']['original'])}</code></pre>
          <pre class="lang-zh"><code>{escape(item['prompt']['zh'])}</code></pre>
          <div class="meta">
            <a href="{escape(item['source']['url'], quote=True)}" target="_blank" rel="noopener"><span class="lang-en">Original source ↗</span><span class="lang-zh">查看原始来源 ↗</span></a>
            <a class="lang-en" href="{REPO_URL}/blob/main/README.md#{escape(item['id'], quote=True)}" target="_blank" rel="noopener">View entry in repository ↗</a>
            <a class="lang-zh" href="{REPO_URL}/blob/main/README_zh.md#{escape(item['id'], quote=True)}" target="_blank" rel="noopener">查看仓库条目 ↗</a>
            <span>{escape(item['source']['author'])}</span>
          </div>
        </div>
      </details>"""


def video_card(path: str, items: list[dict], categories: dict) -> str:
    search_text = " ".join(
        [item["title"]["en"] + " " + item["title"]["zh"] + " " + " ".join(item["tags"]) for item in items]
    ).lower()
    modes = " ".join(sorted({item["mode"] for item in items}))
    title_en = items[0]["title"]["en"] if len(items) == 1 else f"{len(items)} prompts share this source video"
    title_zh = items[0]["title"]["zh"] if len(items) == 1 else f"同一原视频对应 {len(items)} 段提示词"
    blocks = "".join(prompt_block(item, categories) for item in items)
    return f"""
    <article class="video-card" id="{escape(video_anchor(path), quote=True)}" data-mode="{escape(modes, quote=True)}" data-search="{escape(search_text, quote=True)}">
      <header class="card-head">
        <div>
          <h2 class="lang-en">{escape(title_en)}</h2>
          <h2 class="lang-zh">{escape(title_zh)}</h2>
          <p><span class="lang-en">Original result video · {len(items)} prompt(s)</span><span class="lang-zh">原始成片 · {len(items)} 段提示词</span></p>
        </div>
      </header>
      <div class="player-shell">
        <video controls playsinline preload="metadata">
          <source src="{escape(path, quote=True)}#t=0.001" type="video/mp4">
          Your browser does not support HTML5 video.
        </video>
      </div>
      <div class="video-actions">
        <a href="{REPO_URL}/blob/main/{escape(path, quote=True)}" target="_blank" rel="noopener"><span class="lang-en">View video file on GitHub ↗</span><span class="lang-zh">在 GitHub 查看视频文件 ↗</span></a>
        <a href="{escape(path, quote=True)}" target="_blank" rel="noopener"><span class="lang-en">Open direct MP4 ↗</span><span class="lang-zh">打开 MP4 直链 ↗</span></a>
      </div>
      <div class="prompt-list">{blocks}</div>
    </article>"""


def generate() -> str:
    prompts = load_prompts()
    categories = load_categories()
    groups: dict[str, list[dict]] = defaultdict(list)
    for item in prompts:
        video = next(media for media in item["media"] if media["type"] == "video")
        groups[video["path"]].append(item)

    cards = "".join(video_card(path, items, categories) for path, items in groups.items())
    counts = Counter(item["mode"] for item in prompts)
    filters = [
        ("all", "All", "全部", len(prompts)),
        ("text-to-video", "Text to Video", "文生视频", counts["text-to-video"]),
        ("image-to-video", "Image to Video", "图生视频", counts["image-to-video"]),
        ("first-last-frame", "First / Last Frame", "首尾帧", counts["first-last-frame"]),
        ("reference-generation", "Reference Generation", "参考生成", counts["reference-generation"]),
    ]
    filter_html = "".join(
        f'<button class="filter{(" active" if key == "all" else "")}" data-filter="{key}"><span class="lang-en">{en} · {count}</span><span class="lang-zh">{zh} · {count}</span></button>'
        for key, en, zh, count in filters
    )

    return f"""<!doctype html>
<html lang="zh-CN" data-lang="zh">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="description" content="{len(prompts)} bilingual MiniMax H3 prompts with directly playable original videos.">
  <link rel="canonical" href="{SITE_URL}">
  <title>Awesome MiniMax H3 Prompts · Video Library</title>
  <style>
    :root {{ color-scheme: dark; --bg:#08090c; --panel:#111319; --line:#272b35; --text:#f5f7fb; --muted:#9ca4b3; --accent:#ff5b31; --accent2:#ffb347; }}
    * {{ box-sizing:border-box; }}
    html {{ scroll-behavior:smooth; }}
    body {{ margin:0; background:radial-gradient(circle at 75% -10%,#402011 0,transparent 28rem),var(--bg); color:var(--text); font:15px/1.6 Inter,ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif; }}
    a {{ color:#ff9a75; text-decoration:none; }} a:hover {{ text-decoration:underline; }}
    .lang-en {{ display:none; }} html[data-lang="en"] .lang-en {{ display:initial; }} html[data-lang="en"] .lang-zh {{ display:none; }}
    .hero {{ padding:68px max(24px,calc((100vw - 1180px)/2)) 42px; border-bottom:1px solid var(--line); }}
    .eyebrow {{ color:var(--accent2); letter-spacing:.14em; text-transform:uppercase; font-weight:750; }}
    h1 {{ max-width:900px; margin:12px 0 16px; font-size:clamp(38px,7vw,76px); line-height:.98; letter-spacing:-.055em; }}
    .lede {{ max-width:760px; color:#c5cad4; font-size:18px; }}
    .hero-actions {{ display:flex; gap:10px; flex-wrap:wrap; margin-top:24px; }}
    .button,.lang-toggle {{ border:1px solid var(--line); border-radius:999px; padding:10px 16px; background:#171a21; color:var(--text); font-weight:700; cursor:pointer; }}
    .button.primary {{ background:linear-gradient(135deg,var(--accent),#e8374e); border:0; color:white; }}
    .stats {{ display:flex; gap:32px; flex-wrap:wrap; margin-top:34px; }} .stat strong {{ display:block; font-size:26px; }} .stat span {{ color:var(--muted); }}
    .toolbar {{ position:sticky; top:0; z-index:10; padding:14px max(20px,calc((100vw - 1180px)/2)); background:rgba(8,9,12,.9); backdrop-filter:blur(16px); border-bottom:1px solid var(--line); }}
    .toolbar-inner {{ display:flex; gap:10px; flex-wrap:wrap; align-items:center; }}
    input[type="search"] {{ flex:1 1 260px; min-width:0; border:1px solid var(--line); border-radius:12px; padding:11px 14px; background:#111319; color:var(--text); font:inherit; }}
    .filters {{ display:flex; gap:7px; overflow:auto; }} .filter {{ white-space:nowrap; border:1px solid var(--line); border-radius:999px; padding:8px 12px; background:#111319; color:#c8ced9; cursor:pointer; }} .filter.active {{ background:#fff; color:#0b0c0f; }}
    main {{ width:min(1180px,calc(100% - 40px)); margin:34px auto 80px; display:grid; gap:30px; }}
    .video-card {{ overflow:hidden; scroll-margin-top:84px; border:1px solid var(--line); border-radius:20px; background:linear-gradient(180deg,#14171d,#0f1116); box-shadow:0 18px 70px rgba(0,0,0,.25); }}
    .video-card[hidden] {{ display:none; }} .card-head {{ padding:20px 22px 12px; }} .card-head h2 {{ margin:0; font-size:22px; }} .card-head p {{ margin:3px 0 0; color:var(--muted); }}
    .player-shell {{ background:#000; border-block:1px solid var(--line); }} video {{ width:100%; max-height:72vh; display:block; background:#000; }}
    .video-actions {{ display:flex; gap:16px; flex-wrap:wrap; padding:12px 22px 4px; font-size:13px; }}
    .prompt-list {{ padding:10px 20px 22px; }} details.prompt {{ border-bottom:1px solid var(--line); }} details.prompt:last-child {{ border-bottom:0; }}
    details.prompt {{ scroll-margin-top:84px; }}
    summary {{ display:flex; align-items:center; gap:10px; flex-wrap:wrap; padding:16px 2px; cursor:pointer; font-weight:750; }} .prompt-id {{ color:var(--accent2); font-size:12px; letter-spacing:.08em; }} .pill {{ margin-left:auto; padding:3px 9px; border:1px solid #393e49; border-radius:99px; color:#bfc5d0; font-size:12px; font-weight:650; }}
    .prompt-body {{ padding:0 0 20px; }} .description {{ color:#b9c0cc; }} .prompt-label {{ margin:16px 0 6px; color:#f5d2c4; font-size:12px; font-weight:800; letter-spacing:.08em; text-transform:uppercase; }}
    pre {{ margin:0; padding:16px; max-height:360px; overflow:auto; white-space:pre-wrap; border:1px solid #252a34; border-radius:12px; background:#090b0f; color:#dfe3eb; font:13px/1.65 ui-monospace,SFMono-Regular,Consolas,monospace; }}
    .meta {{ display:flex; gap:14px; flex-wrap:wrap; margin-top:12px; color:var(--muted); font-size:13px; }} .reconstructed {{ padding:10px 12px; border-left:3px solid var(--accent2); background:#2a2113; color:#f0d7a8; }}
    .empty {{ display:none; padding:60px 20px; text-align:center; color:var(--muted); }} footer {{ padding:30px 20px 60px; text-align:center; color:var(--muted); border-top:1px solid var(--line); }}
    @media (max-width:640px) {{ .hero {{ padding-top:42px; }} main {{ width:min(100% - 20px,1180px); }} .prompt-list {{ padding-inline:12px; }} .pill {{ margin-left:0; }} }}
  </style>
</head>
<body>
  <header class="hero">
    <div class="eyebrow">MiniMax H3 · Playable Prompt Library</div>
    <h1><span class="lang-en">Prompts you can watch.</span><span class="lang-zh">能直接播放的 H3 提示词库。</span></h1>
    <p class="lede lang-en">Every entry pairs a bilingual prompt with its downloaded original result video. Press play here—no external player or download step required.</p>
    <p class="lede lang-zh">每条内容都把中英双语提示词与已下载的原始成片放在一起。直接在本页点击播放，不需要跳转外部播放器。</p>
    <div class="hero-actions">
      <a class="button primary" href="#library"><span class="lang-en">Browse videos</span><span class="lang-zh">浏览视频</span></a>
      <a class="button" href="{REPO_URL}">GitHub ↗</a>
      <button class="lang-toggle" id="langToggle" type="button">English / 中文</button>
    </div>
    <div class="stats">
      <div class="stat"><strong>{len(prompts)}</strong><span class="lang-en">prompts</span><span class="lang-zh">条提示词</span></div>
      <div class="stat"><strong>{len(groups)}</strong><span class="lang-en">playable videos</span><span class="lang-zh">个可播放视频</span></div>
      <div class="stat"><strong>2</strong><span class="lang-en">languages</span><span class="lang-zh">种语言</span></div>
    </div>
  </header>
  <nav class="toolbar" id="library">
    <div class="toolbar-inner">
      <input id="search" type="search" placeholder="搜索标题、标签 / Search titles and tags" aria-label="Search prompts">
      <div class="filters">{filter_html}</div>
    </div>
  </nav>
  <main>{cards}<div class="empty" id="empty"><span class="lang-en">No matching prompts.</span><span class="lang-zh">没有匹配的提示词。</span></div></main>
  <footer>
    <p class="lang-en">Third-party prompts and videos retain their original rights. Attribution and source links are preserved on every entry.</p>
    <p class="lang-zh">第三方提示词与视频的权利归原作者所有；每条内容均保留署名与原始来源。</p>
  </footer>
  <script>
    const root=document.documentElement, cards=[...document.querySelectorAll('.video-card')], search=document.querySelector('#search'), empty=document.querySelector('#empty');
    let active='all';
    function applyFilters(){{const q=search.value.trim().toLowerCase();let shown=0;cards.forEach(card=>{{const modeOk=active==='all'||card.dataset.mode.split(' ').includes(active);const textOk=!q||card.dataset.search.includes(q);card.hidden=!(modeOk&&textOk);if(!card.hidden)shown++;}});empty.style.display=shown?'none':'block';}}
    document.querySelectorAll('.filter').forEach(btn=>btn.addEventListener('click',()=>{{document.querySelector('.filter.active').classList.remove('active');btn.classList.add('active');active=btn.dataset.filter;applyFilters();}}));
    search.addEventListener('input',applyFilters);
    document.querySelector('#langToggle').addEventListener('click',()=>{{const lang=root.dataset.lang==='zh'?'en':'zh';root.dataset.lang=lang;root.lang=lang==='zh'?'zh-CN':'en';localStorage.setItem('h3-lang',lang);}});
    const saved=localStorage.getItem('h3-lang');if(saved){{root.dataset.lang=saved;root.lang=saved==='zh'?'zh-CN':'en';}}
    document.querySelectorAll('video').forEach(video=>video.addEventListener('play',()=>document.querySelectorAll('video').forEach(other=>{{if(other!==video)other.pause();}})));
  </script>
</body>
</html>"""


def main() -> None:
    SITE_DIR.mkdir(parents=True, exist_ok=True)
    output = SITE_DIR / "index.html"
    html = "\n".join(line.rstrip() for line in generate().splitlines()) + "\n"
    output.write_text(html, encoding="utf-8")
    print(f"Wrote {output.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
