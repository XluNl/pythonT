#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#print(BASE_DIR)
sys.path.append(BASE_DIR)

from src import service

if __name__ == "__main__":
    #service.MultiServer()