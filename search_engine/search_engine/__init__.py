import logging
from typing import List

logging.getLogger('parso.cache').disabled=True
logging.getLogger('parso.cache.pickle').disabled=True
logging.getLogger('parso.python.diff').disabled=True

with open("./keywords.txt", mode="rt", encoding='utf8') as f:
    g_keywords = [w.strip() for w in f]

g_keywords = g_keywords

g_keywords_dict = {
    "保定": "举报奖励资金",
    "Beijing": "量化问责,表彰先进,动态管理,督查考核,政绩突出,专项行动,信息通报,议事协调机构,挂职锻炼,绩效考核,定期通报,抽样检验,督导检查,竞赛活动,网格化环境监管,一案双查,双公示,行政培训,跟踪督办,执法协调,专项执法,联合执法,网络化管理,门前三包,检查联动机制,部门联动,效能督察,内部监督,干部轮岗,三方三级,监管联动,联动执法,分级督察,第三方核查,长效机制,创先争优,竞争性选拔,基层派驻纪检监察,行政问责制,一票表决制,动态跟踪管理,自我检查监督制度,标准化建设,沟通协调机制,定期会商研判制,移送制,通报曝光制度,联合发布信息制度,公平竞争审查制,整改落实机制,问责倒逼规范,每月例会机制,网格化规范建设",
    "唐山": "领导体制",
    "天津": "联防联控,量化问责,检举,控告,权责统一,专项资金,补助,典型经验,减排考核,交流会,示范基地,工作台账,信息报送,一把手负责制,应急联络网,纵横协管,网格监督员,共同责任,减排统计,信息公开属性源头认定,保密审查制度,双考核制度,例会",
    "孟村回族自治县": "部门联查",
    "Langfang": "环境保护目标,联动督查,定期督查,集中督查,综合督查,情况通报制度",
    "Chengde": "综合绩效评价,普查领导小组",
    "Cangzhou": "预考核",
    "河北": "联防联控,座谈会,通报排名,联合技术创新",
    "Shijiazhuang": "抽调,领导负责制,优选,公开遴选,分解任务,巡回检查,协调联动,媒体,明察暗访,分包责任,一盘棋,横向沟通,协调联络,压力传导,网格化监管,目标倒逼,示范引领",
    "Qinhuangdao": "行政首长负责制,综合执法",
    "Hengshui": "人才柔性流动,环保垂管,联合督导组,环境信息化建设",
    "Xingtai": "检查评比,分片包干制度",
    "Handan": "评先评优,网格职责",
}

for k, v in g_keywords_dict.items():
    g_keywords_dict[k] = [w.strip() for w in v.split(",")]

