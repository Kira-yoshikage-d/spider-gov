#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import pandas as pd
rex_change = re.compile(r'^(■.+?报讯　)|(来源：淮北日报)')


def main(df: pd.DataFrame):
    df['content'] = df['content'].str.replace(rex_change, '')
    return df


