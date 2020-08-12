#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from base import BaseFeedBook, URLOpener, string_of_tag

def getBook():
    return VNExpress

class VNExpress(BaseFeedBook):
    title                 = 'VNExpress'
    description           = 'Báo tiếng Việt nhiều người xem nhất.'
    language              = 'vi'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_vnexpress.gif"
    coverfile             = "cv_vnexpress.jpg"
    deliver_days          = ['Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday']
    
    remove_classes = ['ec-messages',]
    feeds = [
        ('Thế giới', 'https://vnexpress.net/rss/the-gioi.rss'),
        ('Thời sự', 'https://vnexpress.net/rss/thoi-su.rss'),
        ('Kinh doanh', 'https://vnexpress.net/rss/kinh-doanh.rss'),
        ('Startup', 'https://vnexpress.net/rss/startup.rss'),
        ('Giải trí', 'https://vnexpress.net/rss/giai-tri.rss'),
        ('Thể thao', 'https://vnexpress.net/rss/the-thao.rss'),
        ('Pháp luật', 'https://vnexpress.net/rss/phap-luat.rss'),
        ('Giáo dục', 'https://vnexpress.net/rss/giao-duc.rss'),
        ('Sức khoẻ', 'https://vnexpress.net/rss/suc-khoe.rss'),
        ('Đời sống', 'https://vnexpress.net/rss/gia-dinh.rss'),
        ('Du lịch', 'https://vnexpress.net/rss/du-lich.rss'),
        ('Khoa học', 'https://vnexpress.net/rss/khoa-hoc.rss'),
        ('Số hoá', 'https://vnexpress.net/rss/so-hoa.rss'),
        ('Xe', 'https://vnexpress.net/rss/oto-xe-may.rss'),
        ('Ý kiến', 'https://vnexpress.net/rss/y-kien.rss'),
        ('Tâm sự', 'https://vnexpress.net/rss/tam-su.rss'),
        ('Cười', 'https://vnexpress.net/rss/cuoi.rss'),
        ]
    