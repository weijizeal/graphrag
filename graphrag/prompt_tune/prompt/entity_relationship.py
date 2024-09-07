# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""实体关系生成的微调提示。"""

ENTITY_RELATIONSHIPS_GENERATION_PROMPT = """
-目标-
给定可能与此活动相关的文本文档和实体类型列表，从文本中识别这些类型的所有实体以及已识别实体之间的所有关系。

-步骤-
1. 识别所有实体。对于每个已识别的实体，提取以下信息:
- entity_name: 实体名称
- entity_type: 以下类型之一: [{entity_types}]
- entity_description: 实体属性和活动的综合描述
将每个实体格式化为("entity"{{tuple_delimiter}}<entity_name>{{tuple_delimiter}}<entity_type>{{tuple_delimiter}}<entity_description>)

2. 从步骤1中确定的实体中，确定彼此“明显相关”的所有实体对(source_entity, target_entity) 。
对于每对相关实体，提取如下信息:
- source_entity: 源实体的名称，与步骤1中识别的相同
- target_entity: 目标实体的名称，与步骤1中识别的名称相同
- relationship_description: 对于源实体和目标实体之间存在关联的原因的解释
- relationship_strength: 表示源实体与目标实体之间的关系强度
将每个关系格式化为("relationship"{{tuple_delimiter}}<source_entity>{{tuple_delimiter}}<target_entity>{{tuple_delimiter}}<relationship_description>{{tuple_delimiter}}<relationship_strength>)

3. 返回步骤1和步骤2中识别出的所有实体和关系的单个列表。使用{{record_delimiter}}作为列表分隔符。

4. 完成后，输出{{completion_delimiter}}。

######################
-示例-
######################
示例 1:
实体类型: 组织, 人
文本: 
Verdantis的中央机构计划在周一和周四举行会议，该机构计划在周四下午1:30（PDT）发布最新的政策决议，随后中央机构主席马丁·史密斯将举行新闻发布会并回答问题。投资者预计市场战略委员会将把基准利率维持在3.5%-3.75%的区间内。
######################
输出:
("entity"{{tuple_delimiter}}中央机构{{tuple_delimiter}}组织{{tuple_delimiter}}中央机构是Verdantis的联邦储备，负责在周一和周四设定利率) 
{{record_delimiter}}
("entity"{{tuple_delimiter}}马丁·史密斯{{tuple_delimiter}}人{{tuple_delimiter}}马丁·史密斯是中央机构的主席) {{record_delimiter}} 
("entity"{{tuple_delimiter}}市场战略委员会{{tuple_delimiter}}组织{{tuple_delimiter}}中央机构的委员会负责做出关于利率和Verdantis货币供应增长的关键决策) 
{{record_delimiter}} 
("relationship"{{tuple_delimiter}}马丁·史密斯{{tuple_delimiter}}中央机构{{tuple_delimiter}}马丁·史密斯是中央机构的主席，并将在新闻发布会上回答问题{{tuple_delimiter}}9)
{{completion_delimiter}}

######################
示例 2: 
实体类型: 组织
文本:
TechGlobal（TG）的股票在周四全球交易所上市首日暴涨。然而，IPO专家警告称，这家半导体公司的首次公开募股表现并不代表其他新上市公司的表现。

TechGlobal是一家曾经公开上市的公司，2014年被Vision Holdings私有化。这家知名的芯片设计公司声称其芯片为85%的高端智能手机提供动力。
######################
输出: 
("entity"{{tuple_delimiter}}TechGlobal{{tuple_delimiter}}组织{{tuple_delimiter}}TechGlobal是一家现在在全球交易所上市的公司，为85%的高端智能手机提供动力) 
{{record_delimiter}}
("entity"{{tuple_delimiter}}Vision Holdings{{tuple_delimiter}}组织{{tuple_delimiter}}Vision Holdings是一家曾经拥有TechGlobal的公司)
{{record_delimiter}}
("relationship"{{tuple_delimiter}}TechGlobal{{tuple_delimiter}}Vision Holdings{{tuple_delimiter}}Vision Holdings从2014年起曾拥有TechGlobal{{tuple_delimiter}}5) 
{{completion_delimiter}}

######################
示例 3:
实体类型: 组织,地理位置,人物 
文本: 五名奥雷利亚人因被视为人质在菲鲁扎巴德被判8年监禁，目前他们正在返回奥雷利亚的途中。
在奎塔拉的调解下，当80亿美元的菲鲁兹资金被转移到奎塔拉首都克罗哈拉的金融机构时，交换正式完成。
交换在菲鲁扎巴德的首都提鲁齐亚启动，四名男子和一名女性（他们也是菲鲁兹国民）登上了前往克罗哈拉的包机。
他们受到了奥雷利亚高级官员的欢迎，目前正前往奥雷利亚首都卡申。
这些奥雷利亚人包括39岁的商人塞缪尔·纳马拉，他曾被关押在提鲁齐亚的阿尔哈米亚监狱，以及59岁的记者杜尔克·巴塔格拉尼和53岁的环保人士梅吉·塔兹巴，她同时也拥有布拉提纳斯国籍。 
###################### 
# 输出:
("entity"{{tuple_delimiter}}FIRUZABAD{{tuple_delimiter}}地理位置{{tuple_delimiter}}菲鲁扎巴德关押了奥雷利亚人作为人质) {{record_delimiter}} 
("entity"{{tuple_delimiter}}AURELIA{{tuple_delimiter}}地理位置{{tuple_delimiter}}寻求释放人质的国家) {{record_delimiter}} 
("entity"{{tuple_delimiter}}QUINTARA{{tuple_delimiter}}地理位置{{tuple_delimiter}}调解人质交换的国家，用金钱换取人质) {{record_delimiter}} 
("entity"{{tuple_delimiter}}TIRUZIA{{tuple_delimiter}}地理位置{{tuple_delimiter}}菲鲁扎巴德的首都，奥雷利亚人被关押的地方) {{record_delimiter}}
("entity"{{tuple_delimiter}}KROHAARA{{tuple_delimiter}}地理位置{{tuple_delimiter}}奎塔拉的首都)
{{record_delimiter}} 
("entity"{{tuple_delimiter}}CASHION{{tuple_delimiter}}地理位置{{tuple_delimiter}}奥雷利亚的首都) {{record_delimiter}} 
("entity"{{tuple_delimiter}}SAMUEL NAMARA{{tuple_delimiter}}人物{{tuple_delimiter}}奥雷利亚人，曾在提鲁齐亚的阿尔哈米亚监狱服刑) 
{{record_delimiter}} 
("entity"{{tuple_delimiter}}ALHAMIA PRISON{{tuple_delimiter}}地理位置{{tuple_delimiter}}提鲁齐亚的监狱) {{record_delimiter}} 
("entity"{{tuple_delimiter}}DURKE BATAGLANI{{tuple_delimiter}}人物{{tuple_delimiter}}奥雷利亚记者，曾作为人质被关押) {{record_delimiter}}
("entity"{{tuple_delimiter}}MEGGIE TAZBAH{{tuple_delimiter}}人物{{tuple_delimiter}}布拉提纳斯国籍的环保人士，曾作为人质被关押) 
{{record_delimiter}}
("relationship"{{tuple_delimiter}}FIRUZABAD{{tuple_delimiter}}AURELIA{{tuple_delimiter}}菲鲁扎巴德与奥雷利亚协商了人质交换{{tuple_delimiter}}2) 
{{record_delimiter}} 
("relationship"{{tuple_delimiter}}QUINTARA{{tuple_delimiter}}AURELIA{{tuple_delimiter}}奎塔拉调解了菲鲁扎巴德与奥雷利亚之间的人质交换{{tuple_delimiter}}2) 
{{record_delimiter}} 
("relationship"{{tuple_delimiter}}QUINTARA{{tuple_delimiter}}FIRUZABAD{{tuple_delimiter}}奎塔拉调解了菲鲁扎巴德与奥雷利亚之间的人质交换{{tuple_delimiter}}2) 
{{record_delimiter}} 
("relationship"{{tuple_delimiter}}SAMUEL NAMARA{{tuple_delimiter}}ALHAMIA PRISON{{tuple_delimiter}}塞缪尔·纳马拉曾是阿尔哈米亚监狱的囚犯{{tuple_delimiter}}8) 
{{record_delimiter}} 
("relationship"{{tuple_delimiter}}SAMUEL NAMARA{{tuple_delimiter}}MEGGIE TAZBAH{{tuple_delimiter}}塞缪尔·纳马拉与梅吉·塔兹巴在同一次人质释放中被交换{{tuple_delimiter}}2)
{{record_delimiter}} 
("relationship"{{tuple_delimiter}}SAMUEL NAMARA{{tuple_delimiter}}DURKE BATAGLANI{{tuple_delimiter}}塞缪尔·纳马拉与杜尔克·巴塔格拉尼在同一次人质释放中被交换{{tuple_delimiter}}2) 
{{record_delimiter}}
("relationship"{{tuple_delimiter}}MEGGIE TAZBAH{{tuple_delimiter}}DURKE BATAGLANI{{tuple_delimiter}}梅吉·塔兹巴与杜尔克·巴塔格拉尼在同一次人质释放中被交换{{tuple_delimiter}}2)
{{record_delimiter}} 
("relationship"{{tuple_delimiter}}SAMUEL NAMARA{{tuple_delimiter}}FIRUZABAD{{tuple_delimiter}}塞缪尔·纳马拉是菲鲁扎巴德的人质{{tuple_delimiter}}2) 
{{record_delimiter}}
("relationship"{{tuple_delimiter}}MEGGIE TAZBAH{{tuple_delimiter}}FIRUZABAD{{tuple_delimiter}}梅吉·塔兹巴是菲鲁扎巴德的人质{{tuple_delimiter}}2)
{{record_delimiter}} 
("relationship"{{tuple_delimiter}}DURKE BATAGLANI{{tuple_delimiter}}FIRUZABAD{{tuple_delimiter}}杜尔克·巴塔格拉尼是菲鲁扎巴德的人质{{tuple_delimiter}}2) 
{{completion_delimiter}}

-真实数据-
######################
实体类型: {entity_types}
文本: {input_text}
######################
输出:
"""

ENTITY_RELATIONSHIPS_GENERATION_JSON_PROMPT = """
-目标- 
给定一个可能与此活动相关的文本文件和一个实体类型列表，从文本中识别出这些类型的所有实体以及它们之间的所有关系。

-步骤-
1. 识别所有实体。对于每个识别出的实体，提取以下信息：
entity_name: 实体的名称，首字母大写
entity_type: 实体的类型之一：[{entity_types}]
entity_description: 该实体的属性和活动的详细描述
每个实体的输出格式如下：
{{"name": <实体名称>, "type": <实体类型>, "description": <实体描述>}}
2. 从第1步中识别出的实体中，找出所有明确相关的实体对(source_entity, target_entity)。
对于每一对相关实体，提取以下信息：
source_entity: 第1步中识别出的源实体的名称
target_entity: 第1步中识别出的目标实体的名称
relationship_description: 解释为什么你认为源实体和目标实体是相关的
relationship_strength: 一个介于1到10之间的整数，表示源实体与目标实体之间关系的强度
每个关系的输出格式如下：
{{"source": <源实体>, "target": <目标实体>, "relationship": <关系描述>, "relationship_strength": <关系强度>}}
3.返回步骤1和步骤2中识别的所有实体和关系的JSON列表。

###################### 
-示例-
###################### 
示例 1: 
文本:
维丹提斯中央机构计划在周一和周四召开会议，周四下午1:30（太平洋时间）将发布其最新的政策决定，随后中央机构主席马丁·史密斯将在新闻发布会上回答问题。投资者预计市场策略委员会将维持基准利率在3.5%-3.75%的范围内不变。 ###################### 
输出: 
[ {{"name": "中央机构", "type": "组织", "description": "中央机构是维丹提斯的联邦储备，负责在周一和周四设定利率"}}, {{"name": "马丁·史密斯", "type": "人物", "description": "马丁·史密斯是中央机构的主席"}}, {{"name": "市场策略委员会", "type": "组织", "description": "中央机构的委员会负责决定利率以及维丹提斯货币供应的增长"}}, {{"source": "马丁·史密斯", "target": "中央机构", "relationship": "马丁·史密斯是中央机构的主席，并将在新闻发布会上回答问题", "relationship_strength": 9}} ]

###################### 
示例 2: 
文本: 
TechGlobal（TG）股票在周四于全球交易所上市的第一天大幅上涨。但IPO专家警告，这家半导体公司在公开市场上的首秀并不能代表其他新上市公司的表现。

TechGlobal曾是一家上市公司，2014年被Vision Holdings私有化。这家知名的芯片设计公司称其为85%的高端智能手机提供动力。 ###################### 
输出: 
[ {{"name": "TechGlobal", "type": "组织", "description": "TechGlobal是一只现在在全球交易所上市的股票，为85%的高端智能手机提供动力"}}, {{"name": "Vision Holdings", "type": "组织", "description": "Vision Holdings是一家曾经拥有TechGlobal的公司"}}, {{"source": "TechGlobal", "target": "Vision Holdings", "relationship": "Vision Holdings从2014年开始曾拥有TechGlobal", "relationship_strength": 5}} ]

###################### 
示例 3: 
文本: 
五名奥雷利亚人因被视为人质在菲鲁扎巴德被判8年监禁，目前他们正在返回奥雷利亚的途中。
在奎塔拉的调解下，当80亿美元的菲鲁兹资金被转移到奎塔拉首都克罗哈拉的金融机构时，交换正式完成。
交换在菲鲁扎巴德的首都提鲁齐亚启动，四名男子和一名女性（他们也是菲鲁兹国民）登上了前往克罗哈拉的包机。
他们受到了奥雷利亚高级官员的欢迎，目前正前往奥雷利亚首都卡申。
这些奥雷利亚人包括39岁的商人塞缪尔·纳马拉，他曾被关押在提鲁齐亚的阿尔哈米亚监狱，以及59岁的记者杜尔克·巴塔格拉尼和53岁的环保人士梅吉·塔兹巴，她同时也拥有布拉提纳斯国籍。 
###################### 
输出: 
[ {{"name": "菲鲁扎巴德", "type": "地理位置", "description": "菲鲁扎巴德关押了奥雷利亚人作为人质"}}, 
{{"name": "奥雷利亚", "type": "地理位置", "description": "寻求释放人质的国家"}},
{{"name": "奎塔拉", "type": "地理位置", "description": "调解人质交换的国家，用金钱换取人质"}},
{{"name": "提鲁齐亚", "type": "地理位置", "description": "菲鲁扎巴德的首都，奥雷利亚人被关押的地方"}},
{{"name": "克罗哈拉", "type": "地理位置", "description": "奎塔拉的首都"}}, 
{{"name": "卡申", "type": "地理位置", "description": "奥雷利亚的首都"}},
{{"name": "塞缪尔·纳马拉", "type": "人物", "description": "奥雷利亚人，曾在提鲁齐亚的阿尔哈米亚监狱服刑"}}, 
{{"name": "阿尔哈米亚监狱", "type": "地理位置", "description": "提鲁齐亚的监狱"}},
{{"name": "杜尔克·巴塔格拉尼", "type": "人物", "description": "奥雷利亚记者，曾作为人质被关押"}},
{{"name": "梅吉·塔兹巴", "type": "人物", "description": "布拉提纳斯国籍的环保人士，曾作为人质被关押"}}, 
{{"source": "菲鲁扎巴德", "target": "奥雷利亚", "relationship": "菲鲁扎巴德与奥雷利亚协商了人质交换", "relationship_strength": 2}},
{{"source": "奎塔拉", "target": "奥雷利亚", "relationship": "奎塔拉调解了菲鲁扎巴德与奥雷利亚之间的人质交换", "relationship_strength": 2}}, 
{{"source": "奎塔拉", "target": "菲鲁扎巴德", "relationship": "奎塔拉调解了菲鲁扎巴德与奥雷利亚之间的人质交换", "relationship_strength": 2}}, 
{{"source": "塞缪尔·纳马拉", "target": "阿尔哈米亚监狱", "relationship": "塞缪尔·纳马拉曾是阿尔哈米亚监狱的囚犯", "relationship_strength": 8}},
{{"source": "塞缪尔·纳马拉", "target": "梅吉·塔兹巴", "relationship": "塞缪尔·纳马拉与梅吉·塔兹巴在同一次人质释放中被交换", "relationship_strength": 2}},
{{"source": "塞缪尔·纳马拉", "target": "杜尔克·巴塔格拉尼", "relationship": "塞缪尔·纳马拉与杜尔克·巴塔格拉尼在同一次人质释放中被交换", "relationship_strength": 2}}, 
{{"source": "梅吉·塔兹巴", "target": "杜尔克·巴塔格拉尼", "relationship": "梅吉·塔兹巴与杜尔克·巴塔格拉尼在同一次人质释放中被交换", "relationship_strength": 2}}, 
{{"source": "塞缪尔·纳马拉", "target": "菲鲁扎巴德", "relationship": "塞缪尔·纳马拉是菲鲁扎巴德的人质", "relationship_strength": 2}}, 
{{"source": "梅吉·塔兹巴", "target": "菲鲁扎巴德", "relationship": "梅吉·塔兹巴是菲鲁扎巴德的人质", "relationship_strength": 2}},
{{"source": "杜尔克·巴塔格拉尼", "target": "菲鲁扎巴德", "relationship": "杜尔克·巴塔格拉尼是菲鲁扎巴德的人质", "relationship_strength": 2}} ]

-真实数据-
######################
实体类型: {entity_types}
文本: {input_text}
######################
输出:
"""

UNTYPED_ENTITY_RELATIONSHIPS_GENERATION_PROMPT = """
-目标-
给定一个可能与此活动相关的文本文档，首先从文本中识别出捕捉文本信息和思想所需的所有实体。
接下来，报告已识别实体之间的所有关系。

-步骤-
1. 识别所有实体。对于每个识别出的实体，提取以下信息：
entity_name: 实体的名称
entity_type: 为实体建议多个标签或类别，类别应尽可能广泛，不要太具体。
entity_description: 对实体的属性和活动进行全面描述
2. 格式化每个实体为 ("entity"{{tuple_delimiter}}<entity_name>{{tuple_delimiter}}<entity_type>{{tuple_delimiter}}<entity_description>)
从步骤1中识别的实体中，识别所有明确相关的（source_entity, target_entity）对。
对于每对相关的实体，提取以下信息：
source_entity: 在步骤1中识别的源实体名称
target_entity: 在步骤1中识别的目标实体名称
relationship_description: 解释为什么你认为源实体和目标实体相互关联
relationship_strength: 一个数值评分，指示源实体和目标实体之间关系的强度
格式化每个关系为 ("relationship"{{tuple_delimiter}}<source_entity>{{tuple_delimiter}}<target_entity>{{tuple_delimiter}}<relationship_description>{{tuple_delimiter}}<relationship_strength>)
3. 返回第1和第2步中识别的所有实体和关系的单一列表。使用 {{record_delimiter}} 作为列表的分隔符。
4. 完成后输出{{completion_delimiter}}。

######################
-示例-
######################
示例1:
文本:
Verdantis的中央机构定于周一和周四开会，该机构计划在周四下午1:30 PDT发布其最新的政策决定，随后举行新闻发布会，中央机构主席Martin Smith将接受提问。投资者预计市场战略委员会将在3.5%-3.75%的范围内保持基准利率不变。
######################
输出:
("entity"{{tuple_delimiter}}CENTRAL INSTITUTION{{tuple_delimiter}}ORGANIZATION{{tuple_delimiter}}中央机构是Verdantis的联邦储备系统，负责在周一和周四设定利率)
{{record_delimiter}}
("entity"{{tuple_delimiter}}MARTIN SMITH{{tuple_delimiter}}PERSON{{tuple_delimiter}}Martin Smith是中央机构的主席)
{{record_delimiter}}
("entity"{{tuple_delimiter}}MARKET STRATEGY COMMITTEE{{tuple_delimiter}}ORGANIZATION{{tuple_delimiter}}中央机构的委员会负责关于利率和Verdantis货币供应增长的关键决策)
{{record_delimiter}}
("relationship"{{tuple_delimiter}}MARTIN SMITH{{tuple_delimiter}}CENTRAL INSTITUTION{{tuple_delimiter}}Martin Smith是中央机构的主席，将在新闻发布会上回答问题{{tuple_delimiter}}9)
{{completion_delimiter}}

######################
示例2:
文本:
TechGlobal的股票在周四的全球交易所开盘首日飙升。但IPO专家警告说，这家半导体公司在公共市场的首次亮相并不代表其他新上市公司可能的表现。

TechGlobal曾是一家上市公司，2014年被Vision Holdings私有化。这家著名的芯片设计公司声称其为85%的高端智能手机提供动力。
######################
输出:
("entity"{{tuple_delimiter}}TECHGLOBAL{{tuple_delimiter}}ORGANIZATION{{tuple_delimiter}}TechGlobal现在在全球交易所上市，提供85%的高端智能手机动力)
{{record_delimiter}}
("entity"{{tuple_delimiter}}VISION HOLDINGS{{tuple_delimiter}}ORGANIZATION{{tuple_delimiter}}Vision Holdings曾在2014年将TechGlobal私有化)
{{record_delimiter}}
("relationship"{{tuple_delimiter}}TECHGLOBAL{{tuple_delimiter}}VISION HOLDINGS{{tuple_delimiter}}Vision Holdings在2014年到现在曾拥有TechGlobal{{tuple_delimiter}}5)
{{completion_delimiter}}

######################
示例3:
文本:
五名被Firuzabad囚禁8年的Aurelians被广泛认为是人质，现在正在回家的路上。
由Quintara策划的交换在80亿美元的Firuz资金转移到Quintara首都Krohaara的金融机构时最终完成。
交换在Firuzabad首都Tiruzia发起，四名男子和一名女子，均为Firuz国民，登上了飞往Krohaara的包机。
他们受到了Aurelian高级官员的欢迎，现在正在前往Aurelia首都Cashion的路上。
这些Aurelians包括39岁的商人Samuel Namara，他曾被关押在Tiruzia的Alhamia监狱，59岁的记者Durke Bataglani，以及53岁的环保主义者Meggie Tazbah，后者也拥有Bratinas国籍。
######################
输出:
("entity"{{tuple_delimiter}}FIRUZABAD{{tuple_delimiter}}GEO{{tuple_delimiter}}Firuzabad关押了Aurelians作为人质)
{{record_delimiter}}
("entity"{{tuple_delimiter}}AURELIA{{tuple_delimiter}}GEO{{tuple_delimiter}}寻求释放人质的国家)
{{record_delimiter}}
("entity"{{tuple_delimiter}}QUINTARA{{tuple_delimiter}}GEO{{tuple_delimiter}}通过金钱交换人质的国家)
{{record_delimiter}}
("entity"{{tuple_delimiter}}TIRUZIA{{tuple_delimiter}}GEO{{tuple_delimiter}}Firuzabad的首都，是Aurelians被关押的地方)
{{record_delimiter}}
("entity"{{tuple_delimiter}}KROHAARA{{tuple_delimiter}}GEO{{tuple_delimiter}}Quintara的首都)
{{record_delimiter}}
("entity"{{tuple_delimiter}}CASHION{{tuple_delimiter}}GEO{{tuple_delimiter}}Aurelia的首都)
{{record_delimiter}}
("entity"{{tuple_delimiter}}SAMUEL NAMARA{{tuple_delimiter}}PERSON{{tuple_delimiter}}曾被关押在Tiruzia的Alhamia监狱的Aurelian商人)
{{record_delimiter}}
("entity"{{tuple_delimiter}}ALHAMIA PRISON{{tuple_delimiter}}GEO{{tuple_delimiter}}Tiruzia的监狱)
{{record_delimiter}}
("entity"{{tuple_delimiter}}DURKE BATAGLANI{{tuple_delimiter}}PERSON{{tuple_delimiter}}被关押的人质之一Aurelian记者)
{{record_delimiter}}
("entity"{{tuple_delimiter}}MEGGIE TAZBAH{{tuple_delimiter}}PERSON{{tuple_delimiter}}也拥有Bratinas国籍的环保主义者)
{{record_delimiter}}
("relationship"{{tuple_delimiter}}FIRUZABAD{{tuple_delimiter}}AURELIA{{tuple_delimiter}}Firuzabad与Aurelia谈判了人质交换{{tuple_delimiter}}2)
{{record_delimiter}}
("relationship"{{tuple_delimiter}}QUINTARA{{tuple_delimiter}}AURELIA{{tuple_delimiter}}Quintara促成了Firuzabad和Aurelia之间的人质交换{{tuple_delimiter}}2)
{{record_delimiter}}
("relationship"{{tuple_delimiter}}QUINTARA{{tuple_delimiter}}FIRUZABAD{{tuple_delimiter}}Quintara促成了Firuzabad和Aurelia之间的人质交换{{tuple_delimiter}}2)
{{record_delimiter}}
("relationship"{{tuple_delimiter}}SAMUEL NAMARA{{tuple_delimiter}}ALHAMIA PRISON{{tuple_delimiter}}Samuel Namara曾是Alhamia监狱的囚犯{{tuple_delimiter}}8)
{{record_delimiter}}
("relationship"{{tuple_delimiter}}SAMUEL NAMARA{{tuple_delimiter}}MEGGIE TAZBAH{{tuple_delimiter}}Samuel Namara和Meggie Tazbah在同一次人质释放中被交换{{tuple_delimiter}}2)
{{record_delimiter}}
("relationship"{{tuple_delimiter}}SAMUEL NAMARA{{tuple_delimiter}}DURKE BATAGLANI{{tuple_delimiter}}Samuel Namara和Durke Bataglani在同一次人质释放中被交换{{tuple_delimiter}}2)
{{record_delimiter}}
("relationship"{{tuple_delimiter}}MEGGIE TAZBAH{{tuple_delimiter}}DURKE BATAGLANI{{tuple_delimiter}}Meggie Tazbah和Durke Bataglani在同一次人质释放中被交换{{tuple_delimiter}}2)
{{record_delimiter}}
("relationship"{{tuple_delimiter}}SAMUEL NAMARA{{tuple_delimiter}}FIRUZABAD{{tuple_delimiter}}Samuel Namara曾是Firuzabad的人质{{tuple_delimiter}}2)
{{record_delimiter}}
("relationship"{{tuple_delimiter}}MEGGIE TAZBAH{{tuple_delimiter}}FIRUZABAD{{tuple_delimiter}}Meggie Tazbah曾是Firuzabad的人质{{tuple_delimiter}}2)
{{record_delimiter}}
("relationship"{{tuple_delimiter}}DURKE BATAGLANI{{tuple_delimiter}}FIRUZABAD{{tuple_delimiter}}Durke Bataglani曾是Firuzabad的人质{{tuple_delimiter}}2)
{{completion_delimiter}}

######################
-真实数据-
######################
文本: {input_text}
######################
输出:
"""
