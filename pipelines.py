# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
import importlib
import sys
importlib.reload(sys)


class Meiju110Pipeline(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y%m%d', time.localtime())
        fileName = today + 'movie.txt'
        with open(fileName,  'a', encoding='utf-8') as fp:
            # fp.write(item['storyName'] + '\t' + item['storyState'] + '\t' + item['storyCatagory'] + '\t' + item['tvStation'] + '\t' + item['updateTime'] + '\n')
            fp.write(item['storyName'][0] + '\t' + item['storyState'][0]  + '\t' + item['storyCatagory'][0] + '\t' + item['tvStation'][0] + '\t' + item['updateTime'][0] + '\n')

        fp.close()
        return item









