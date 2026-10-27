# Plain Craft Launcher rebuild

本仓库使用GPT-6.1-sol模型、Hermes客户端搭建。

这是基于 [Meloong-Git/PCL](https://github.com/Meloong-Git/PCL) 源码独立修改并构建的第三方版本，**不是官方 PCL，也不代表或暗示原作者对本项目的认可、担保或维护**。

## 免责声明
本仓库为个人基于开源软件修改版本搭建的自动构建仓库，非官方发布，与原作者、贡献者及官方项目无任何关联。
本仓库及所有自动构建产物**仅供本人个人学习、测试使用，请勿下载、传播、分发、商用或用于生产环境**。
任何人私自下载、使用、修改、分发或以其他方式使用本仓库内容及构建产物，均属个人行为，风险自担；由此造成的一切后果与原作者、贡献者及本仓库所有者无关。
本仓库所有者不对构建产物的完整性、安全性、合法性或可用性作任何担保，不承担任何直接或间接责任。
如相关权利人认为本仓库内容不当，请通知我，我将及时删除或处理。

## 使用范围

- 当前仓库及自动构建仅供本人学习测试使用，请勿分发。
- 当前源码修改仅恢复原版Minecraft下载入口。
- 源码和构建产物均不包含CurseForge API Key或Microsoft客户端凭据。

## 自动构建

GitHub Actions 在 Windows runner 上构建 Release 版本。构建产物名称格式为：

```text
Plain Craft Launcher rebuild [完整版本号]
```

完整版本号从四段式 `AssemblyFileVersion` 读取。

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
