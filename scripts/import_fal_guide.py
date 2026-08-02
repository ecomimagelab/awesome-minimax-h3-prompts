#!/usr/bin/env python3
"""Import a curated bilingual subset of MiniMax H3 examples mirrored by fal.ai.

The raw JSON is captured from the public guide page in a browser so each
published prompt remains paired with its exact result-video URL. MiniMax's
official H3 materials take attribution precedence for examples that appear in
both places. This script adds the curated records and downloads the videos into
the repository.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


SOURCE_PAGE = "https://fal.ai/learn/devs/minimax-h3-prompting-guide"
OFFICIAL_SOURCE_PAGE = "https://www.minimax.io/blog/minimax-h3"
SELECTED = [1, 3, 4, 7, 8, 9, 10, 12, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24,
            26, 27, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43]

ZH = {
    1: {
        "title": "史诗太空歌剧预告片",
        "prompt": "史诗级院线太空歌剧预告片\n\n保持快速节奏和宏大尺度，不要让剪辑拖沓。使用凌厉的硬切、剧烈震动的指挥舱、炽白闪光、转瞬即逝的黑场，以及猛烈跃迁至曲速的冲击。标题卡使用宽字距的电影字体——不要用纯白色——配合克制的材质纹理、轻微照明和淡淡的边缘辉光。标题动画从深空阴影中浮现，掠过一束星光，逐渐拉开字距，留下轻微残影，并在黑场上短暂闪现。",
    },
    3: {
        "title": "沙漠时尚广告片",
        "prompt": "制作一支高级的 16:9 横屏时尚短片。图片 1 用于整体情绪、地点和胶片质感；图片 2 用于人物；图片 3 用于包袋；图片 4 用于片尾品牌标识。这是一支服装与包袋的时尚广告。基调高级、冷静、克制，但剪辑仍应活跃且具时尚前瞻性——不要拍成传统叙事电影或电商广告。\n\n故事保持简单：在沙漠公路的一辆老爷车旁，一位女子走到车尾，打开后备厢，取出一个黑色包袋，与站在旁边的男子安静对视片刻，随后提包离开。让服装和包袋自然融入表演，使其成为角色身份的一部分。",
    },
    4: {
        "title": "赛博垃圾摇滚时尚短片",
        "prompt": "图片 1 作为质感与情绪参考，图片 2 作为人物外观参考。生成一支 15 秒、16:9 的时尚短片。保持人物身份一致：铂金色长发、窄框黑色复古太阳镜、亮面黑色漆皮风衣、冷酷自信的表情，以及映在风衣上的橙色火光。\n\n风格：使用模拟胶片质感的快速剪辑时尚片，背景是夜间大火、黑烟和橙红色火焰。叠加 VHS 故障、监控信号中断、20 世纪 90 年代胶片颗粒、扫描线、色差、漏光、闪白转场和轻微画面抖动。",
    },
    7: {
        "title": "霓虹洗衣店邂逅",
        "prompt": "15 秒，16:9 横屏。将深夜自助洗衣店的真人实拍与手绘发光动画结合。小型自助洗衣店内，荧光灯轻微闪烁，洗衣机正在运转，散落着塑料筐、旧长凳，地上还有一只袜子。空间保持安静，略带怀旧感。\n\n采用单手持手机拍摄的感觉，保留明显抖动、白色荧光灯下的曝光波动、玻璃上的环境反射，以及近距离拍摄时稍显迟缓的自动对焦。避免精致的商业构图；画面应像在跟随一个奇异幻影时偶然拍到的真实深夜邂逅。",
    },
    8: {
        "title": "赛博垃圾摇滚说唱 MV",
        "prompt": "风格：暗黑流行／赛博垃圾摇滚／说唱音乐录像，兼具照片级高定时尚质感和扫描电影杂志的纹理——高对比但不廉价。参考 20 世纪 90 年代末至 21 世纪初的独立杂志、复印件、胶片扫描、地下音乐海报和 zine 拼贴。加入粗颗粒、轻微片门晃动、半色调网点、粗糙印刷边缘和轻微扫描套印偏移。保持快速剪辑，只使用硬切——不要淡入淡出或柔和转场。文字处理和表面质感要与参考图片一致。",
    },
    9: {
        "title": "绿幕转童话场景合成",
        "prompt": "移除视频 1 的绿幕背景，替换为与视频 2 相似的童话式背景。背景元素必须与视频 1 中人物的动作完全匹配。调整视频 1 中人物的光照，使其与新背景完全一致。",
    },
    10: {
        "title": "动态画廊海报",
        "prompt": "将源艺术作品制作成动态海报，同时保留白色画廊边框、内框、红白黑配色、3D 收藏级人偶质感和原始版式。每当文字出现时，加入轻快俏皮的打字音效。",
    },
    12: {
        "title": "竖屏家庭冲突短剧",
        "prompt": "一段 9:16 竖屏家庭冲突场景，采用真实自然的真人表演，发生在中国家庭住宅或小餐馆中。使用温暖室内光，背景带红色装饰和书法，浅景深、强烈情绪与紧凑节奏。\n\n表演：自然的短剧风格，绝不舞台化。秦昊轩带着愤怒、受伤和急迫进行反驳。年长女性以尖锐、强势、步步紧逼的语气质问他，冲突逐步升级。\n\n主要使用中近景，并频繁进行正反打剪辑。环境要有真实生活气息。不要科幻、古装或动画风格。不要出现字幕、额外文字、平台水印或贴纸。",
    },
    14: {
        "title": "未来感眼镜广告",
        "prompt": "制作一支高级 9:16 时尚眼镜广告。匹配参考视频的镜头节奏、剪辑速度、白色无缝背景效果和凌厉时尚态度。使用极简无缝白棚，并配以干净、大胆、前卫、足以匹配全球奢侈品牌广告的艺术指导。\n\n图片 1 作为主视觉：两位全身女性模特，一位黑人、一位白人，保留她们的高级服装、肢体语言、影棚灯光、T 台气场和冷峻态度。图片 2 用于面部细节。两位模特都佩戴基于图片 3 的未来奢华眼镜：环绕式弧形镜片、锐利的猫眼与护目镜混合轮廓、镜面反射、流线型镜腿，以及高级时尚配饰的精致表面。",
    },
    15: {
        "title": "人体工学椅产品短片",
        "prompt": "产品功能可视化\n\n在高级办公空间中展示一把黑色 Herman Miller 人体工学椅，并完成 360 度产品展示。切至透气网布椅背的微距镜头并可视化气流；展示腰部支撑和人体工学曲线的工程动画；演示多方向扶手和座椅高度调节。呈现设计师、开发者和创意专业人士长时间舒适工作的状态。加入 3D 骨骼支撑可视化，传达全天候舒适性，并搭配精致的室内设计。片尾显示：“WHERE INSPIRATION MEETS COMFORT.” 整体方向极简、冷色、专业、未来感且节奏舒缓。图片 1 用于功能细节，图片 2 用于产品。",
    },
    17: {
        "title": "Nike 风格产品落地页",
        "prompt": "围绕图片 1 中的产品，制作一个受 Nike 数字视觉语言启发的动态产品落地页 UI/UX 演示。使用超大、粗体、斜体无衬线字体，背景结合强调速度的光轨与深色碳纤维或透气运动网布纹理。展示流畅、快速、有力量的页面滚动，并加入高冲击力的悬停交互，如放大和颜色反转。",
    },
    18: {
        "title": "汽车网站 UI 动效",
        "prompt": "为网站 UI 制作动画：顶部标题向下滑入定位，下方文案面板向上滑入，汽车灯光从暗色变为红色。",
    },
    19: {
        "title": "旋转产品页面揭幕",
        "prompt": "从上到下揭示页面布局。上方和中部文字向下滑入，下方文字向上滑入。中央产品出现后，让它轻微旋转。",
    },
    20: {
        "title": "黏土动画熔岩峡谷飞跃",
        "prompt": "黏土动画。一只狐狸冲向悬崖边缘，毫不犹豫地起跳，以戏剧化的英雄式慢动作飞越巨大的熔岩峡谷。腾空时，摄影机以大胆的动态运动从狐狸腹部下方高速掠过，展现深不见底的峡谷和黏土身体完全舒展的动作。",
    },
    21: {
        "title": "仙侠角色短片",
        "prompt": "将图片 2 作为锁定的角色参考。保留半束的黑色长发、镂空银冠、靛蓝发带、层叠浅色汉服、半透明蓝色外袍、深蓝腰带、银色花形扣件和长流苏。图片 1 用于分镜顺序和节奏。\n\n以高质量 4K、16:9 的中式 3D 风格呈现，具备电影级仙侠制作水准：强烈、庄重，并带有宿命感。逐拍遵循分镜，摄影机运动自然、转场无缝——绝不能像幻灯片。仅在近景或特写中展示面部。远景使用背面、后侧三分之四视角或空镜；不要在远处展示正脸。",
    },
    22: {
        "title": "乙游男主角色宣传片",
        "prompt": "为乙女游戏中的男性主角制作角色宣传片。将图片 2 作为严格的身份参考。全程保持相同的面容、发型、身体比例、服装设计、材质细节和精致的乙游 CG 美学。",
    },
    23: {
        "title": "第一人称战术游戏画面",
        "prompt": "摄影机：第一人称、眼平视角、手持式游戏画面。模拟玩家操作现代战争 FPS，手持突击步枪，在军事基地外围缓慢推进。沿掩体旁的道路前进，让准星扫过前方通道，停下向远处目标射击数发，然后像真实玩家操控画面一样继续向前推进。\n\n光照：现代军事基地中的冷色自然光，与烟雾和火光混合。画面保持照片级真实和清晰，武器、材质、尘土与战场薄雾达到 AAA 游戏品质。\n\n摄影机运动：移动时带轻微的玩家操控摇摆；开场缓慢前进，小幅左右查看，射击时加入轻微后坐力，随后稳定继续向前。",
    },
    24: {
        "title": "互动乙游转场",
        "prompt": "互动乙女游戏\n\n将第一张图片作为精确起始帧，第二张图片作为精确结束帧。在高级中式乙女视觉小说界面中制作转场，呈现演出前后亲密的后台时刻。从“选择观看他的表演”自然过渡到“韩旭听到女主角的话后露出饶有兴趣的反应”。以精致的乙游动效呈现 UI 文案、选项和对话框。转场保持流畅，浪漫张力含蓄而克制。",
    },
    26: {
        "title": "多素材电影感重混",
        "prompt": "使用图片 1–6 作为素材。紧密匹配参考视频 1 的镜头节奏、转场语言和音乐。",
    },
    27: {
        "title": "真人场景体素化变换",
        "prompt": "保留视频 1 中的建筑、行人和整体环境为照片级真人实拍。仅将树木和汽车转换为《我的世界》风格的 3D 像素艺术或体素方块物体，并使用图片 1 作为视觉参考。保持它们的运动符合物理规律，同时保留真实环境中的阴影和透射光。视频 2 作为整体目标参考。",
    },
    29: {
        "title": "角色替换与表演参考",
        "prompt": "让图片 1 中角色的动作、表情和表演节奏紧密匹配输入视频 1。\n\n画面右侧水槽旁，男子把洗好的盘子递给左侧女子。他转身后突然用右手把洗洁精泡沫弹向她。她被吓到后立即反击。两人一边大笑、一边躲闪，玩闹着互相抛洒泡沫。",
    },
    30: {
        "title": "街舞动作迁移",
        "prompt": "使用视频 1 作为街舞表演的动作参考。使用图片 1 和图片 2 作为角色参考。",
    },
    31: {
        "title": "水豚动作复现",
        "prompt": "DIY 反应短片的动作参考\n\n使用固定广角机位匹配视频 1 中的动作。将三名穿西装的男子替换为三只高度照片级真实的水豚。精确保留原始运动路径：三只水豚同时快速趴到地面；左侧水豚跳到中央；中央水豚滚到最左侧；新的中央水豚滚到最右侧；右侧水豚跳到中央；最后中央水豚跳到另外两只上方，叠成金字塔。保持摄影机固定，并让毛发、光照和阴影真实融入场景。",
    },
    32: {
        "title": "声音克隆对白迁移",
        "prompt": "角色说道：“逐风而行，自在而活。抛开烦恼，享受当下。”声音匹配音频 1。",
    },
    34: {
        "title": "添加与群体同步的角色",
        "prompt": "在画面左侧添加一个人，穿着与其他人相同的队服，并与其他人同步运动。",
    },
    35: {
        "title": "主体与服装精准替换",
        "prompt": "精准主体与服装替换\n\n将视频 1 后方的儿童替换为图片 1 中的金毛犬。将最左侧儿童穿的卡其色夹克替换为图片 2 中的牛仔夹克。",
    },
    36: {
        "title": "绿幕环境替换",
        "prompt": "移除视频 1 的绿幕背景，替换为与视频 2 相似的童话环境。让所有背景元素正确响应主体的动作，并重新调整主体光照，使其自然融入新场景。",
    },
    37: {
        "title": "日转夜重打光",
        "prompt": "重新打光\n\n将参考视频中的光照从白天改为夜晚。",
    },
    38: {
        "title": "窗外景观替换",
        "prompt": "真人实拍环境替换\n\n将视频 1 中窗外的景色替换为图片 1。",
    },
    39: {
        "title": "对白与表演替换",
        "prompt": "在视频 1 中，将女子的台词——“我们不可能在一起。不是我不爱你；只是我们根本走不到最后。”——替换为音频 1 中的台词：“请不要走。这一次，我们不要再放开彼此。”细微调整表演，使其匹配新的对白。",
    },
    40: {
        "title": "多元素场景编辑",
        "prompt": "在参考视频中：将报纸替换为绿色精装书；将椅子替换为红色沙发；移除主体的太阳镜并露出清晰面容；移除汽车燃烧效果并恢复车辆正常状态；将从外套中取出的照片替换为黑色小笔记本；在画面左侧添加一棵树。",
    },
    41: {
        "title": "产品、招牌与对白替换",
        "prompt": "在参考视频中，将开头出现的罐装饮料替换为可口可乐。把背景中发光的“FamilyMart”便利店招牌改为“HUHUI”。结尾时，将塑料袋中的所有零食替换为罐装可口可乐，并把最后一句“我买了几样零食”改为“我买了一大堆可乐”。",
    },
    42: {
        "title": "精准服装互换",
        "prompt": "两名魔术师站在舞台上面向观众，表演“互换”魔术。他们同时挥动魔杖，烟雾升起。烟雾散去后，两人的西装颜色已经互换：左侧魔术师现在穿白色，右侧魔术师现在穿黑色。手套颜色不变。两人鞠躬；身后的红色幕布合拢，并逐渐从深红变为深蓝。",
    },
    43: {
        "title": "手绘浪漫特效",
        "prompt": "创意诠释＋动态手绘特效\n\n在视频 1 中两人周围加入类似图片 1 的橙黄色手绘标记。随着两人靠近，标记不断增多，从微小火花逐渐积累为明亮光芒。两人接吻时，加入粉色笔触。",
    },
}


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def mode_for(endpoint: str) -> str:
    return {
        "Text to Video": "text-to-video",
        "First & Last Frame": "first-last-frame",
        "Reference to Video": "reference-generation",
    }[endpoint]


def download(item: tuple[str, str, Path]) -> tuple[str, int]:
    title, url, target = item
    if target.exists() and target.stat().st_size > 1024:
        return title, target.stat().st_size
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    partial = target.with_suffix(target.suffix + ".part")
    with urllib.request.urlopen(request, timeout=120) as response, partial.open("wb") as out:
        shutil.copyfileobj(response, out, length=1024 * 1024)
    if partial.stat().st_size <= 1024:
        raise RuntimeError(f"Downloaded file is too small: {title}")
    os.replace(partial, target)
    return title, target.stat().st_size


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("raw_json", type=Path)
    parser.add_argument("--workers", type=int, default=6)
    args = parser.parse_args()

    repo = Path(__file__).resolve().parents[1]
    prompt_dir = repo / "data" / "prompts"
    media_dir = repo / "media"
    prompt_dir.mkdir(parents=True, exist_ok=True)
    media_dir.mkdir(parents=True, exist_ok=True)

    raw = {int(item["index"]): item for item in json.loads(args.raw_json.read_text(encoding="utf-8"))}
    missing = [index for index in SELECTED if index not in raw or index not in ZH]
    if missing:
        raise SystemExit(f"Missing selected records or translations: {missing}")

    jobs: list[tuple[str, str, Path]] = []
    queued_targets: set[Path] = set()
    for offset, index in enumerate(SELECTED, start=22):
        item = raw[index]
        translation = ZH[index]
        slug = slugify(item["title"])
        # Indexes 9 and 36 use the same official result video. Keep one
        # binary and let the README renderer group both prompts below it.
        media_name = (
            "minimax-official-green-screen-to-fairytale-composite.mp4"
            if index == 36
            else f"minimax-official-{slug}.mp4"
        )
        record = {
            "id": f"h3-{offset:04d}",
            "title": {"en": item["title"], "zh": translation["title"]},
            "description": {
                "en": f"A published MiniMax H3 example demonstrating {item['title'].lower()}, with its exact source prompt and result video.",
                "zh": f"公开的 MiniMax H3“{translation['title']}”案例，包含原始提示词与对应成片。",
            },
            "mode": mode_for(item["endpoint"]),
            "featured": False,
            "prompt": {
                "original_language": "en",
                "original": item["prompt"],
                "zh": translation["prompt"],
            },
            "parameters": {"duration": "5–15s", "resolution": "2K", "ratio": "not stated"},
            "tags": [mode_for(item["endpoint"]), "official"],
            "media": [{
                "type": "video",
                "path": f"media/{media_name}",
                "source_url": OFFICIAL_SOURCE_PAGE,
                "rights_status": "third-party-attributed",
            }],
            "source": {
                "type": "official",
                "author": "MiniMax",
                "url": OFFICIAL_SOURCE_PAGE,
                "source_location": "page",
                "published_at": "2026-07-31",
                "retrieved_at": "2026-08-01",
            },
            "verification": {
                "prompt_visible": True,
                "h3_confirmed": True,
                "output_visible": True,
                "notes": "Matched to the same prompt and result video in MiniMax's official H3 materials.",
            },
        }
        output = prompt_dir / f"h3-{offset:04d}.json"
        output.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        target = media_dir / media_name
        if target not in queued_targets:
            jobs.append((item["title"], item["video"]["src"], target))
            queued_targets.add(target)

    failures = []
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        futures = {pool.submit(download, job): job for job in jobs}
        for future in as_completed(futures):
            try:
                title, size = future.result()
                print(f"downloaded: {title} ({size:,} bytes)")
            except Exception as exc:
                failures.append((futures[future][0], str(exc)))
                print(f"FAILED: {futures[future][0]}: {exc}", file=sys.stderr)

    if failures:
        print(json.dumps(failures, ensure_ascii=False, indent=2), file=sys.stderr)
        return 1
    print(f"Imported {len(SELECTED)} prompt/video pairs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
