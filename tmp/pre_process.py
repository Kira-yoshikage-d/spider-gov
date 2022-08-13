#!/usr/bin/env python3
import pandas as pd
import sys
import os.path

df = pd.read_csv(sys.argv[1])

df = df.sort_values(by=['url', 'keyword'])
df = df.drop_duplicates()
df = df.groupby('url').apply(lambda x: ','.join(x['keyword']))
df = pd.DataFrame({'url': df.index, 'keyword': df.values})

df.to_csv('uniq_'+sys.argv[1], index=None, header=None)
