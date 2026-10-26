from pathlib import Path
import re

path = Path('Plain Craft Launcher 2/FormMain.xaml.vb')
text = path.read_text(encoding='utf-8-sig')
pattern = r'''(?m)^\s*'开源版本提示\r?\n\s*If VersionBranchMain = "OpenSource" Then\r?\n\s*MyMsgBox\(.*?, "开源版本说明"\)\r?\n\s*End If'''
replacement = '''            '修改版说明
            If VersionBranchMain = "OpenSource" Then
                MyMsgBox($"该版本基于PCL开源版本构建，修改内容为：恢复下载功能。{vbCrLf}以下是开源版本原始说明：{vbCrLf}该版本中无法使用以下特性：{vbCrLf}- CurseForge API 调用：需要自行申请 API Key，然后添加到 ModSecret.vb 的开头{vbCrLf}- 正版登录：需要自行向微软申请 Client ID，然后添加到 ModSecret.vb 的开头{vbCrLf}- 更新与联网通知：避免滥用隐患{vbCrLf}- 主题切换：这是需要赞助解锁的纪念性质的功能，别让赞助者太伤心啦……{vbCrLf}- 百宝箱：开发早期往里面塞了些开发工具，整理起来太麻烦了……", "修改版说明")
            End If'''
count = len(re.findall(pattern, text, flags=re.DOTALL))
if count == 1:
    text = re.sub(pattern, replacement, text, count=1, flags=re.DOTALL)
elif count == 0 and '该版本基于PCL开源版本构建，修改内容为：恢复下载功能。' in text and '"修改版说明")' in text:
    pass
else:
    raise SystemExit(f'Expected one original notice or an already-patched notice, found {count}; refusing to modify.')
path.write_text(text, encoding='utf-8-sig', newline='')
