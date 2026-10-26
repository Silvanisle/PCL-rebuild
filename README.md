# Plain Craft Launcher rebuild

This repository is a third-party modified build of [Meloong-Git/PCL](https://github.com/Meloong-Git/PCL).

## Status

- This is **not an official PCL distribution** and is not endorsed or maintained by the original author.
- The current modification restores the Minecraft download page by building the source with `RestrictMcDownload = False`.
- The repository and build workflow are currently for the owner's personal use only. **Do not download, redistribute, mirror, or publish the build artifacts.**
- No CurseForge API key or Microsoft client credential is included in the source or build artifacts.

## Build output

GitHub Actions builds the Release configuration on Windows and uploads an artifact named:

```text
Plain Craft Launcher rebuild [full version]
```

The full version is read from the four-part `AssemblyFileVersion`, for example `2.99.0.1`.

## Attribution

Plain Craft Launcher and its source code are created by the original PCL authors. Special thanks to **龙腾猫跃 (LTCatt)**, the original author and maintainer.

Support the original author through the official sponsorship page:

https://meloong.com/afd/a/LTCat

Original repository:

https://github.com/Meloong-Git/PCL

The upstream `LICENCE` and the upstream reasonable-use guidance are retained in this repository. Review them before any use beyond private testing.

## Upstream resources

- [Official PCL download](https://meloong.com/pcl)
- [PCL discussions](https://github.com/Meloong-Git/PCL/discussions)
- [PCL help repository](https://github.com/LTCatt/PCL2Help)
