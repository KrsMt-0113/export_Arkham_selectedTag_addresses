# Arkham addresses crawler

Get all addresses tagged with selected Arkham tag, e.g. `cex`(centralized exchanges).

[Here](https://docs.google.com/spreadsheets/d/1Dgp8_6r7W1gBjr_eug7c9HUFdc47luB77In6qLYK0r4/edit?usp=sharing) is the tag list.


> **ATTENTION**: Though there are only 10k+ addresses tagged "`cex`", **`9,223,372,036,854,775,807`** pages are there to fetch. It's your mission to solve the problem, GOODLUCK!

---

# Arkham 特定标签地址采集

获取所有给定标签下的地址，例如`cex`(中心化交易所)。

在[这里](https://docs.google.com/spreadsheets/d/1Dgp8_6r7W1gBjr_eug7c9HUFdc47luB77In6qLYK0r4/edit?usp=sharing)查看标签列表。


> **注意**：尽管在 Arkham 上属于 `cex` 标签的地址仅有一万多个，但所使用的查询路径总共有 **`9,223,372,036,854,775,807`** 页数据，大部分是重复内容。至于 Arkham 为何要这样重复记录地址，我毫无头绪。同样的情况还发生在 `dex-aggregator` 标签上（19位数的总页面），但在标签 `trump-dinner` 下数据的存储又是正常的，到第九页就返回空白并显示 **`"allAddressesFetched": true`**。
