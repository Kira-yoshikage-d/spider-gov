#!/usr/bin/env python3

import click
import requests
import time
from subprocess import Popen
import os
from pathlib import Path
import subprocess
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from SpiderKeeper.app.spider.model import Project, SpiderInstance


engine = create_engine("sqlite+pysqlite:///" + os.path.join(os.path.abspath('.'), 'SpiderKeeper.db'))
session = Session(engine)

def get_spiders_list(project):
    resp = requests.get(f"http://127.0.0.1:6800/listspiders.json?project={project.project_name}")
    spiders = resp.json()["spiders"]
    return [SpiderInstance(spider_name=spider, project_id=project.id) for spider in spiders]

def get_projects_list():
    resp = requests.get("http://127.0.0.1:6800/listprojects.json")
    projects = resp.json()["projects"]
    return [Project(project_name=project) for project in projects]

def sync_to_spiderkeeper():
    proc_spiderkeeper = Popen(args=["spiderkeeper", "--host=127.0.0.1", "--port=5000"],
                            stdout=subprocess.DEVNULL,
                            stderr=subprocess.DEVNULL,
                            cwd=os.path.abspath('./'))
    time.sleep(3)
    proc_spiderkeeper.terminate()
    projects = get_projects_list()
    for project in projects:
        session.add(project)
        print(f"Project: {project}")
    session.commit()
    spiders_lists = [get_spiders_list(project) for project in projects]
    for spiders_list in spiders_lists:
        for spider in spiders_list:
            session.add(spider)
            print(f"Spider: {spider}")
    session.commit()

@click.group
def launch():
    pass

@launch.command
def deploy():
    """
    部署
    """
    root_dir = Path('../')
    search_engine_path = (root_dir / 'search_engine').absolute()
    article_crawler_path = (root_dir / 'article_crawler').absolute()
    p = subprocess.Popen(["scrapyd", "-d", os.path.abspath('./')],
                         stdout=subprocess.DEVNULL,
                         stderr=subprocess.DEVNULL,
                         cwd=os.path.abspath('./'))
    time.sleep(3)
    subprocess.run(["scrapyd-deploy", "local"], cwd=search_engine_path)
    subprocess.run(["scrapyd-deploy", "local"], cwd=article_crawler_path)

    sync_to_spiderkeeper()

    p.terminate()

@launch.command
def check():
    pass

@launch.command
def start():
    try:
        scrapyd_log = open("scrapyd.log", mode="at", encoding="utf8")
        spiderkeeper_log = open("spiderkeeper.log", mode="at", encoding="utf8")

        print("start scrapyd.")
        proc_scrapyd = Popen(args=["scrapyd", "-d", os.path.abspath('./')],
                            stdout=scrapyd_log, stderr=scrapyd_log, cwd=os.path.abspath('./'))

        print("start spiderkeeper.")
        proc_spiderkeeper = Popen(args=["spiderkeeper", "--host=127.0.0.1", "--port=5000"],
                                stdout=spiderkeeper_log,
                                stderr=spiderkeeper_log,
                                cwd=os.path.abspath('./'))

        print("open http://127.0.0.1:5000, default user: admin, password: admin.")

        print("wait for ending.")

        proc_scrapyd.wait()
        proc_spiderkeeper.wait()
    except:
        print("terminating...")
        print("terminate scrapyd.")
        proc_scrapyd.terminate()
        print("terminate spiderkeeper")
        proc_spiderkeeper.terminate()
        scrapyd_log.close()
        spiderkeeper_log.close()


if __name__ == "__main__":
    launch()
