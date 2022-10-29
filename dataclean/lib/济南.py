#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import pandas as pd
rex_chengde = re.compile(r'^（.+?）|^\(.+?\)|^ZZCR—..........|^——|^▲.+?　|^△.+?　|&ldquo;.+?&rdquo;')


def main(df: pd.DataFrame):
    df['content'] = df['content'].str.replace('[打印页面 | 关闭页面]', '', regex=False)
    df['content'] = df['content'].str.replace(rex_chengde, '')
    return df
