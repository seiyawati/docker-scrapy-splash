# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class BuymaPipeline(object):
    def open_spider(self, spider):
        self.connection = pymysql.connect(
            host="localhost",
            user="buyma", # DBにあわせて変更
            passwd="buyma", # DBにあわせて変更
            database="buyma",
            charset="utf8mb4"
        )
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        # duplication check
        check_title_id = item["title"]
        find_qry = "SELECT `title` FROM `books` WHERE `title` = %s"
        is_done = self.cursor.execute(find_qry, check_title_id)

        # if already a record exists in database, return 1
        if is_done == 0:
            insert_qry = "INSERT INTO `books` (`title`, `price`, `detail_page_url`) VALUES (%s, %s, %s)"
            self.cursor.execute(insert_qry, (item["title"], item["price"], item["detail_page_url"]))
            self.connection.commit()
        else:
            pass

        return item

    def close_spider(self, spider):
        self.connection.close()