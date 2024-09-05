#!/bin/sh
# lunch=`python3 /Users/weixiang/what-to-eat/main.py`
lunch=`/Users/weixiang/what-to-eat/venv/bin/python3 ./gaode.py`
osascript -e "display notification \"$lunch\" with title \"今天吃什么?\""
