#!/usr/bin/env python3

from subprocess import Popen
import os
import subprocess

if __name__ == "__main__":
    try:
        scrapyd_log = open("scrapyd.log", mode="at", encoding="utf8")
        spiderkeeper_log = open("spiderkeeper.log", mode="at", encoding="utf8")

        print("start scrapyd.")
        proc_scrapyd = Popen(args=["scrapyd", "-d", os.path.abspath('./')],
                            stdout=scrapyd_log, stderr=scrapyd_log)

        print("start spiderkeeper.")
        proc_spiderkeeper = Popen(args=["spiderkeeper", "--host=127.0.0.1", "--port=5000"],
                                stdout=spiderkeeper_log,
                                stderr=spiderkeeper_log)

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
