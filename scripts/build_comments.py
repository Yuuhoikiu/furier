#!/usr/bin/env python3
"""扫描 comments/<folder>/post.json，生成 comments/posts.js（GitHub Actions 自动执行）。"""

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
COMMENTS_DIR = ROOT / "comments"
OUTPUT = COMMENTS_DIR / "posts.js"

HEADER = """// 本文件由 scripts/build_comments.py 自动生成，请勿手动编辑
// 新增帖子：在 comments/ 下新建文件夹，放入 post.json 和图片，推送到 GitHub 即可
"""


def load_posts():
    posts = []
    errors = []

    for folder in sorted(COMMENTS_DIR.iterdir()):
        if not folder.is_dir() or folder.name.startswith(("_", ".")):
            continue

        post_file = folder / "post.json"
        if not post_file.is_file():
            continue

        try:
            data = json.loads(post_file.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            errors.append(f"{post_file}: {error}")
            continue

        title = str(data.get("title", "")).strip()
        if not title:
            errors.append(f"{post_file}: 缺少 title 字段")
            continue

        posts.append({
            "folder": folder.name,
            "title": title,
            "author": str(data.get("author", "匿名")).strip(),
            "date": str(data.get("date", "")).strip(),
            "content": str(data.get("content", "")).strip(),
            "tags": [str(tag).strip() for tag in data.get("tags", []) if str(tag).strip()],
            "images": [str(name) for name in data.get("images", [])],
        })

    posts.sort(key=lambda post: (post["date"], post["folder"]), reverse=True)
    return posts, errors


def main():
    posts, errors = load_posts()
    content = HEADER + "window.COMMENT_POSTS = " + json.dumps(posts, ensure_ascii=False, indent=2) + ";\n"

    if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != content:
        OUTPUT.write_text(content, encoding="utf-8")
        print(f"已写入 {OUTPUT.relative_to(ROOT)}，共 {len(posts)} 条帖子")
    else:
        print(f"{OUTPUT.relative_to(ROOT)} 无变化，共 {len(posts)} 条帖子")

    for message in errors:
        print(f"警告: {message}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
