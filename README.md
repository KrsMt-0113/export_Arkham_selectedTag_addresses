# Arkham addresses crawler

Get all addresses tagged with selected Arkham tag, e.g. `cex`(centralized exchanges).

[Here](https://docs.google.com/spreadsheets/d/1Dgp8_6r7W1gBjr_eug7c9HUFdc47luB77In6qLYK0r4/edit?usp=sharing) is the tag list.


> **Note**: Although there are only a little over ten thousand addresses under the `cex` label on Arkham, the query path used returns a total of **`9,223,372,036,854,775,807`** pages of data, most of which are duplicates. I have no idea why Arkham would repeatedly record addresses like this. The same situation occurs under the `dex-aggregator` label (with a 19-digit total page count), yet for the `trump-dinner` label the data storage behaves normally, returning blank after the ninth page and showing `"allAddressesFetched": true`. Perhaps Arkham does NOT actually store all addresses here. They might be betting that users will not have the patience to click “load more” dozens of times, so after several dozen pages they start returning previously displayed data in random order. If so, they should not have written this path into the API documentation.

---

# Arkham 特定标签地址采集

获取所有给定标签下的地址，例如`cex`(中心化交易所)。

在[这里](https://docs.google.com/spreadsheets/d/1Dgp8_6r7W1gBjr_eug7c9HUFdc47luB77In6qLYK0r4/edit?usp=sharing)查看标签列表。


> **注意**：尽管在 Arkham 上属于 `cex` 标签的地址仅有一万多个，但所使用的查询路径总共有 **`9,223,372,036,854,775,807`** 页数据，大部分是重复内容。至于 Arkham 为何要这样重复记录地址，我毫无头绪。同样的情况还发生在 `dex-aggregator` 标签上（19位数的总页面），但在标签 `trump-dinner` 下数据的存储又是正常的，到第九页就返回空白并显示 **`"allAddressesFetched": true`**。也许 Arkham 并没有在这里真正存储所有的地址，他们打赌用户没有耐心点几十次以上的“继续加载”，所以在第几十页之后就开始乱序返回前面显示过的数据。如果是这样，他们就不应该将这一路径写入 API 文档。
