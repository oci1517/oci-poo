#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import time
import subprocess

while True:
    output = subprocess.check_output(["git", "diff"])
    if output != b'':
        os.system("git add .")
        os.system("make profhtml")

    time.sleep(0.2)

