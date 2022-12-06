# adaway-hosts

[![Generate AdAway block hosts file](https://github.com/mrchi/adaway-hosts/actions/workflows/generate.yml/badge.svg)](https://github.com/mrchi/adaway-hosts/actions/workflows/generate.yml)

以 [privacy\-protection\-tools/anti\-AD](https://github.com/privacy-protection-tools/anti-AD) 项目为上游，生成 [AdAway](https://adaway.org/) 使用的 block host 列表。

---

- AdAway 是一款面向安卓设备的 FOSS 广告拦截 App，基于 Hosts 规则。
- anti-AD 是一个中文区比较流行的广告过滤列表。

anti-AD 没有提供对 AdAway 文件格式的支持，后续可能也不会有，见讨论 [请求新增Hosts格式 · Issue \#287 · privacy\-protection\-tools/anti\-AD](https://github.com/privacy-protection-tools/anti-AD/issues/287)）。

本项目基于 anti-AD 的 `anti-ad-domains.txt`，生成了 AdAway 可用的 block host 列表。由 GitHub actions 每天定时更新。

你可以通过以下链接订阅该列表

[https://raw.githubusercontent.com/mrchi/adaway-hosts/main/anti-ad-adaway.txt](https://raw.githubusercontent.com/mrchi/adaway-hosts/main/anti-ad-adaway.txt)
