#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

rex_chengde = re.compile(r'^<!--[\s\S]*-->')

def main(df):
    df['content'] = df['content'].str.replace(rex_chengde, '')
    return df

