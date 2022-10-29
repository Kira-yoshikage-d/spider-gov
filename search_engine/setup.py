# Automatically created by: scrapyd-deploy

from setuptools import setup, find_packages

setup(
    name         = 'project',
    version      = '1.0',
    packages     = find_packages(),
    entry_points = {'scrapy': ['settings = search_engine.settings']},
    data_files   = [('', ['keywords.json'])],
    package_data = {
        '': ['keywords.json']
    }
)
