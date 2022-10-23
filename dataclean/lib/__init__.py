#!/usr/bin/env python
# -*- coding: utf-8 -*-

import importlib
from glob import glob
from pathlib import PurePath
SOUR_DIR = PurePath("./data/source")
DEST_DIR = PurePath("./data/cleaned")
_verbose = False
data_clean_funcs = {}
keywords = '大气,污染,扬尘,空气,油烟,土壤,生态,青山,蓝天,绿水,低碳,压煤,降尘,控车,优企,减排,增绿,排污,水质,水资源,散煤,污水,绿色,低碳,河湖,河畅,水清,岸绿,景美,清淤,排污,粪便,粪污,节水,垃圾,噪音,噪声,绿化,地下水,节能,美丽,环保,高音,治水,雾霾,废物,废水,废气,重金属,尾气'.split(',')

def contain_keywords(x, keywords):
    for keyword in keywords:
        if keyword in x:
            return True
    return False

print("加载差异处理模块...")
for module_file in glob("./lib/*.py"):
    if "__init__.py" in module_file:
        continue
    module_name = PurePath(module_file).stem
    module_import_path = ".".join(["lib", module_name])
    module = importlib.import_module(module_import_path)
    try:
        data_clean_funcs[module_name] = module.main
        if _verbose:
            print(f"{module_import_path} has been loaded.")
    except:
        if _verbose:
            print(f"no main function in module: {module_import_path}")

