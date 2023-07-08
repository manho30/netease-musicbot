#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@Description : Remove cache files
@File        : remove.py
@IDE         : PyCharm
@Date        : 8/7/2023 12:28
"""

import os

def remove():
    music_count = 0
    thumbnail_count = 0
    for file in os.listdir('musics'):
        if file.endswith('.mp3'):
            os.remove(f'./musics/{file}')
            music_count += 1
    for file in os.listdir('thumbnail'):
        if file.endswith('.jpg'):
            os.remove(f'./thumbnail/{file}')
            thumbnail_count += 1

    return music_count, thumbnail_count