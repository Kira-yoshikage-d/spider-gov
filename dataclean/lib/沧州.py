#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

def main(df: pd.DataFrame):
    df['content'] = df['content'].str.replace('[打印页面 | 关闭页面]', '')
    df['date'] = df['date'].str.replace('[年 ｜ 月]', '-').replace('日', '')
    df['date'] = pd.to_datetime(df['date'])
    return df
