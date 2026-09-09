# Moments · Photo Gallery

一个极简静态照片画廊，适合部署到 GitHub Pages。

## 本地预览

在此文件夹打开终端：

```bash
python update_gallery.py
python -m http.server 8000
```

然后浏览器打开 `http://localhost:8000`。

## 后续新增照片

最简单的方法是在 GitHub 仓库中进入 `photos/` 文件夹，点击 **Add file → Upload files**，上传新照片并提交到 `main`。

仓库中的 GitHub Actions 会自动：

1. 重新生成 `gallery.json`；
2. 重新部署 GitHub Pages。

因此无需手动修改网页代码。

## GitHub Pages

仓库 **Settings → Pages → Build and deployment → Source → GitHub Actions**。

首次部署成功后，地址通常为：

`https://你的GitHub用户名.github.io/仓库名/`

## 已支持

- 竖版 3:4 照片窗口
- 淡紫色背景
- 左右箭头切换
- 手机左右滑动
- 键盘方向键
- 当前照片页码
- 小圆点进度
- 点击放大
- 横图/竖图自适应
- 响应式手机布局
