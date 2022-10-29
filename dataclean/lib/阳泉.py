#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import pandas as pd

rex_chengde = re.compile(r'^——')


def main(df: pd.DataFrame):
    df['content'] = df['content'].str.replace(rex_chengde, '')
    return df
