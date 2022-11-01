#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import pandas as pd
rex_change = re.compile(r'^(目.+?录)')


def main(df: pd.DataFrame) -> pd.DataFrame:
    df['date'] = df['date'].str.split('：').map(lambda x: x[1])
    df['date'] = df['date'].str.replace('.', '-')
    df['content'] = df['content'].str.replace('聊城政务信息第72期聊城市人民政府办公室                 ', '')
    df['content'] = df['content'].str.replace(rex_change, '')
    return df
