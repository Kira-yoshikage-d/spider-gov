#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

rex_chengde = re.compile(r'^.TRS_Editor.+}|var(?:.|\n)+?isAppendSpace\(5\);|^．TRS＿Editor.+｝')

def main(df):
    df['content'] = df['content'].str.replace(rex_chengde, '')
    df['date'] = df['date'].str.split(' ').map(lambda x: x[0])
    return df

