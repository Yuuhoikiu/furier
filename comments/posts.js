// 本文件由 scripts/build_comments.py 自动生成，请勿手动编辑
// 新增帖子：在 comments/ 下新建文件夹，放入 post.json 和图片，推送到 GitHub 即可
window.COMMENT_POSTS = [
  {
    "folder": "20261109-welcome",
    "title": "评论区上线啦",
    "author": "秋云",
    "date": "2026-11-09",
    "content": "课表界面已经换成评论区。\n\n发布方法：在 comments/ 下新建一个文件夹（可以直接复制 comments/_template），编辑里面的 post.json，把图片放进同一目录，然后上传到 GitHub。仓库里的 GitHub Actions 会自动扫描所有帖子文件夹并生成清单，推送后稍等片刻即可在网页看到。\n\n本地预览：把整个文件夹拖到网页评论区即可立即查看，不需要手动改任何清单文件。",
    "tags": [
      "公告",
      "使用说明"
    ],
    "images": []
  },
  {
    "folder": "20261109-example",
    "title": "案例：带图片的帖子",
    "author": "秋云",
    "date": "2026-11-09",
    "content": "这是一个完整的案例帖子，用来演示固定格式。\n\n文件夹结构：\n20261109-example/\n├── post.json\n├── 1.jpg\n└── 2.jpg\n\n把整个文件夹拖到网页评论区，就会立即出现这条帖子；图片顺序由 post.json 的 images 字段决定。",
    "tags": [
      "案例",
      "图片"
    ],
    "images": [
      "1.jpg",
      "2.jpg"
    ]
  }
];
