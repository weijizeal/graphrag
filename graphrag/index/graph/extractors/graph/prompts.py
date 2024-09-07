# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""A file containing prompts definition."""

GRAPH_EXTRACTION_PROMPT = """
-目标-
给定一个可能与此活动相关的文本文档以及一系列实体类型，从文本中识别所有这些类型的实体以及所有已识别实体之间的关系。

-步骤-
1. 识别所有实体。对于每个识别出的实体，提取以下信息：
- entity_name: 实体的名称
- entity_type: 以下类型之一：[{entity_types}]
- entity_description: 实体的属性和活动的全面描述
每个实体的格式为 ("entity"{tuple_delimiter}<entity_name>{tuple_delimiter}<entity_type>{tuple_delimiter}<entity_description>)

 
2. 从步骤1中识别的实体中，识别所有*明确相关*的实体对 (source_entity, target_entity)。
对于每对相关的实体，提取以下信息：
- source_entity: 在步骤1中识别的源实体名称
- target_entity: 在步骤1中识别的目标实体名称
- relationship_description: 解释你认为源实体和目标实体为何相关
- relationship_strength: 一个表示源实体与目标实体之间关系强度的数值
每个关系的格式为 ("relationship"{tuple_delimiter}<source_entity>{tuple_delimiter}<target_entity>{tuple_delimiter}<relationship_description>{tuple_delimiter}<relationship_strength>)

3. 返回步骤1和2中识别的所有实体和关系的单一列表，使用 **{record_delimiter}** 作为列表分隔符。

4. 完成后输出 {completion_delimiter}
 
######################
-示例-
######################
示例 1:
实体类型: 组织, 人物
文本:
Verdantis 中央机构计划于周一和周四召开会议，计划在周四下午 1:30 PDT 发布最新的政策决策，随后中央机构主席 马丁·史密斯 将出席新闻发布会回答问题。投资者预计市场战略委员会将维持其基准利率在 3.5%-3.75% 的区间内。

######################
输出:
("entity"{tuple_delimiter}中央机构{tuple_delimiter}组织{tuple_delimiter}中央机构是Verdantis的联邦储备，负责设定利率)
{record_delimiter}
("entity"{tuple_delimiter}马丁·史密斯{tuple_delimiter}人物{tuple_delimiter}马丁·史密斯是中央机构的主席)
{record_delimiter}
("entity"{tuple_delimiter}市场战略委员会{tuple_delimiter}组织{tuple_delimiter}中央机构委员会负责决定利率和Verdantis的货币供应增长)
{record_delimiter}
("relationship"{tuple_delimiter}马丁·史密斯{tuple_delimiter}中央机构{tuple_delimiter}马丁·史密斯是中央机构的主席，并将在新闻发布会上回答问题{tuple_delimiter}9)
{completion_delimiter}

######################
示例 2:
实体类型: 组织
文本:
全球科技 (TG) 的股票在周四的全球交易所开盘日飙升。但IPO专家警告称，这家半导体公司的首次公开募股表现并不能代表其他新上市公司可能的表现。

全球科技是一家曾经上市的公司，2014年被远见控股私有化。这家知名的芯片设计公司称其为85%的高端智能手机提供动力。

######################
输出:
("entity"{tuple_delimiter}全球科技{tuple_delimiter}组织{tuple_delimiter}全球科技 是一家现在在全球交易所上市的公司，负责为85%的高端智能手机提供动力)
{record_delimiter}
("entity"{tuple_delimiter}远见控股{tuple_delimiter}组织{tuple_delimiter}远见控股是一家曾经拥有全球科技的公司)
{record_delimiter}
("relationship"{tuple_delimiter}全球科技{tuple_delimiter}远见控股{tuple_delimiter}远见控股在2014年之前拥有全球科技{tuple_delimiter}5)
{completion_delimiter}

######################
示例 3:
实体类型: 组织, 地理位置, 人物
文本:
五名奥雷利亚人在Firuzabad被关押了8年，被广泛认为是人质，现正返回奥雷利亚。

交换由昆塔拉促成，当Firuzis的80亿美元资金被转移到昆塔拉首都克罗哈拉的金融机构时，交换完成。

交换是在Firuzabad的首都蒂鲁齐亚启动的，四名男子和一名女子也拥有Firuzis国籍，他们登上了一架包机前往克罗哈拉。

他们受到了奥雷利亚高级官员的欢迎，现在正返回奥雷利亚的首都卡希翁。

这些奥雷利亚人包括39岁的商人塞缪尔·纳马拉，他曾被关押在蒂鲁齐亚的阿尔哈米亚监狱，记者杜尔克·巴塔格拉尼，59岁，以及53岁的环保人士梅吉·塔兹巴，她也拥有Bratinas国籍。

######################
输出:
("entity"{tuple_delimiter}Firuzabad{tuple_delimiter}地理位置{tuple_delimiter}Firuzabad拘留了奥雷利亚人作为人质)
{record_delimiter}
("entity"{tuple_delimiter}奥雷利亚{tuple_delimiter}地理位置{tuple_delimiter}寻求释放人质的国家)
{record_delimiter}
("entity"{tuple_delimiter}昆塔拉{tuple_delimiter}地理位置{tuple_delimiter}促成金钱交换人质的国家)
{record_delimiter}
("entity"{tuple_delimiter}蒂鲁齐亚{tuple_delimiter}地理位置{tuple_delimiter}Firuzabad的首都，奥雷利亚人在此被关押)
{record_delimiter}
("entity"{tuple_delimiter}克罗哈拉{tuple_delimiter}地理位置{tuple_delimiter}昆塔拉的首都)
{record_delimiter}
("entity"{tuple_delimiter}卡希翁{tuple_delimiter}地理位置{tuple_delimiter}奥雷利亚的首都)
{record_delimiter}
("entity"{tuple_delimiter}塞缪尔·纳马拉{tuple_delimiter}人物{tuple_delimiter}曾被关押在蒂鲁齐亚的阿尔哈米亚监狱的奥雷利亚人)
{record_delimiter}
("entity"{tuple_delimiter}阿尔哈米亚监狱{tuple_delimiter}地理位置{tuple_delimiter}蒂鲁齐亚的一所监狱)
{record_delimiter}
("entity"{tuple_delimiter}杜尔克·巴塔格拉尼{tuple_delimiter}人物{tuple_delimiter}被扣为人质的奥雷利亚记者)
{record_delimiter}
("entity"{tuple_delimiter}梅吉·塔兹巴{tuple_delimiter}人物{tuple_delimiter}Bratinas国籍的环保人士，被扣为人质)
{record_delimiter}
("relationship"{tuple_delimiter}Firuzabad{tuple_delimiter}奥雷利亚{tuple_delimiter}Firuzabad与奥雷利亚协商人质交换{tuple_delimiter}2)
{record_delimiter}
("relationship"{tuple_delimiter}昆塔拉{tuple_delimiter}奥雷利亚{tuple_delimiter}昆塔拉促成了Firuzabad和奥雷利亚之间的人质交换{tuple_delimiter}2)
{record_delimiter}
("relationship"{tuple_delimiter}昆塔拉{tuple_delimiter}Firuzabad{tuple_delimiter}昆塔拉促成了Firuzabad和奥雷利亚之间的人质交换{tuple_delimiter}2)
{record_delimiter}
("relationship"{tuple_delimiter}塞缪尔·纳马拉{tuple_delimiter}阿尔哈米亚监狱{tuple_delimiter}塞缪尔·纳马拉曾是阿尔哈米亚监狱的囚犯{tuple_delimiter}8)
{record_delimiter}
("relationship"{tuple_delimiter}塞缪尔·纳马拉{tuple_delimiter}梅吉·塔兹巴{tuple_delimiter}塞缪尔·纳马拉和梅吉·塔兹巴在同一次人质释放中被交换{tuple_delimiter}2)
{record_delimiter}
("relationship"{tuple_delimiter}塞缪尔·纳马拉{tuple_delimiter}杜尔克·巴塔格拉尼{tuple_delimiter}塞缪尔·纳马拉和杜尔克·巴塔格拉尼在同一次人质释放中被交换{tuple_delimiter}2)
{record_delimiter}
("relationship"{tuple_delimiter}梅吉·塔兹巴{tuple_delimiter}杜尔克·巴塔格拉尼{tuple_delimiter}梅吉·塔兹巴和杜尔克·巴塔格拉尼在同一次人质释放中被交换{tuple_delimiter}2)
{record_delimiter}
("relationship"{tuple_delimiter}塞缪尔·纳马拉{tuple_delimiter}Firuzabad{tuple_delimiter}塞缪尔·纳马拉曾是Firuzabad的人质{tuple_delimiter}2)
{record_delimiter}
("relationship"{tuple_delimiter}梅吉·塔兹巴{tuple_delimiter}Firuzabad{tuple_delimiter}梅吉·塔兹巴曾是Firuzabad的人质{tuple_delimiter}2)
{record_delimiter}
("relationship"{tuple_delimiter}杜尔克·巴塔格拉尼{tuple_delimiter}Firuzabad{tuple_delimiter}杜尔克·巴塔格拉尼曾是Firuzabad的人质{tuple_delimiter}2)
{completion_delimiter}

######################
-真实数据-
######################
实体类型: {entity_types}
实体名称: {input_text}
######################
输出:"""

CONTINUE_PROMPT = "上次提取中遗漏了许多实体和关系。请记住，仅提取与之前提取类型匹配的实体。使用相同的格式将它们添加在下面：\n"
LOOP_PROMPT = "似乎仍然有一些实体和关系可能被遗漏了。请回答YES 或NO，是否仍有需要添加的实体或关系。\n"
