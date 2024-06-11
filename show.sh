#!/bin/sh
# lunch=`python3 /Users/weixiang/what-to-eat/main.py`
lunch=`python ./gaode.py`
osascript -e "display notification \"$lunch\" with title \"今天吃什么?\""
# 我叫 Mac 唸給妳聽！
# say $lunch
