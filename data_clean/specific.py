#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
import pandas as pd

file_name = f"./data/{argv[1]}.csv"

df = pd.read_csv(file_name).convert_dtypes()

df['keywords'] = df['keywords'].str.split().map(lambda x: ' '.join(set(x)))
