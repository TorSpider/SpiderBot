#!/bin/bash

rm logs/SpiderBot.log
./SpiderBot.py
rm -fr __pycache__
rm -fr */__pycache__
