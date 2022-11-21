#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

def main(df: pd.DataFrame) -> pd.DataFrame:
    df['content'] = df['content'].str.replace('_x000D_', '')

    df['content'] = df['content'].str.replace('[打印页面 | 关闭页面]', '', regex=False)
    df['date'] = df['date'].str.split(':').map(lambda x: x[1])
    return df
