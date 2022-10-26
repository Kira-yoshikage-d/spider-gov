#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

def main(df):
    # 剔除无用符号
    df['content'] = df['content'].str.replace('_x000D_', '')
    df['content'] = df['content'].str.replace('[打印页面 | 关闭页面]', '', regex=False)

    # 格式化日期
    df['date'] = pd.to_datetime(
        df['date'].map(lambda x: x.split()[0])
    )
    return df
