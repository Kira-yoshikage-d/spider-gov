import logging

logging.getLogger('parso.cache').disabled=True
logging.getLogger('parso.cache.pickle').disabled=True
logging.getLogger('parso.python.diff').disabled=True

with open("./keywords.txt", mode="rt", encoding='utf8') as f:
    g_keywords = [w.strip() for w in f]

g_keywords = g_keywords

