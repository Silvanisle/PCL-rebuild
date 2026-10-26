# Plain Craft Launcher rebuild

这是基于 [Meloong-Git/PCL](https://github.com/Meloong-Git/PCL) 源码独立修改并构建的第三方版本，**不是官方 PCL，也不代表或暗示原作者对本项目的认可、担保或维护**。

## 使用范围

- 当前仓库及自动构建仅供仓库所有者本人测试使用。
- **请勿下载、分发、镜像、转存或公开发布本仓库构建的客户端。**
- 当前源码修改是将 `RestrictMcDownload` 设为 `False`，用于恢复原版 Minecraft 下载入口。
- 源码和构建产物均不包含 CurseForge API Key 或 Microsoft 客户端凭据。

## 自动构建

GitHub Actions 在 Windows runner 上构建 Release 版本。构建产物名称格式为：

```text
Plain Craft Launcher rebuild [完整版本号]
```

完整版本号从四段式 `AssemblyFileVersion` 读取，例如 `2.99.0.1`。打版本标签会创建 GitHub **草稿 Release**；在授权与分发范围确认前不会自动公开发布。

## 致谢

感谢 PCL 原作者 **龙腾猫跃（LTCatt）** 及 PCL 社区的长期维护与贡献。

原作者赞助链接：

https://meloong.com/afd/a/LTCat

上游源码仓库：

https://github.com/Meloong-Git/PCL

本仓库保留上游 `LICENCE` 文件。修改、使用或分发前，请阅读上游许可及其引用的合理使用说明；本项目说明不替代法律意见。

## 上游资源

- [PCL 官方下载](https://meloong.com/pcl)
- [PCL 讨论区](https://github.com/Meloong-Git/PCL/discussions)
- [PCL 帮助文档仓库](https://github.com/LTCatt/PCL2Help)
