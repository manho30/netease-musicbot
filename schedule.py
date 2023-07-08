#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@Description : Cron job scheduler
@File        : schedule.py
@IDE         : PyCharm
@Date        : 7/7/2023 23:25
"""
import os

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger

# delete ./musics/*.mp3 and ./thumbnail/*.jpg every 24 hours
def delete_files():
    os.system('rm -rf ./musics/*.mp3')
    os.system('rm -rf ./thumbnail/*.jpg')

# run every 24 hours
def run():
    print('Cron job scheduler started...')
    scheduler = BlockingScheduler()
    scheduler.add_job(delete_files, CronTrigger.from_crontab('0 0 * * *'))
    scheduler.start()

if __name__ == '__main__':
    print('You should not run this file directly. Please run bot.py instead.')