# -*- coding: utf-8 -*-
import scrapy


class PostsSpider(scrapy.Spider):
    name = 'posts'
    allowed_domains = ['vaguntrader.com/forums/ubbthreads.php/forums/3/2/Handguns_-_VIRGINIA_ONLY']
    start_urls = ['https://vaguntrader.com/forums/ubbthreads.php/forums/3/2/Handguns_-_VIRGINIA_ONLY/']

    #known URI's:
    #vaguntrader.com.../forums/3/<insert page number here>/Handguns_-_VIRGINIA_ONLY
    def parse(self, response):
    	# topicsubject is interchanged with alt-topicsubject
    	posts = response.xpath('.//*[@class="topicsubject"]')
    	times = response.xpath('.//*[@class="topicsubject"]')
        # WORKS - locations = response.xpath('.//*[@class="topic-label"]/a/text()').extract()[i]
        page = 2
        i = 0
        print '\n############### STARTING SPIDER ###############\n'
        for post in posts:
       		location = response.xpath('.//span/a/text()').extract()[i]
       		#prints date in increments of 1
       		#Date is not aligned correctly bc of their "...ago" addition
       		# class date and time only exist for last posts past class new-alt-topictime
       		# for second /3/2 the times are out of order
       		postDate = response.xpath('.//*[@class="date"]/text()').extract()[i]

       		postTime = response.xpath('.//*[@class="time"]/text()').extract()[i]
       		i += 1
       		postTitle = response.xpath('.//span/a/text()').extract()[i]
       		i += 1

       		print location
       		print postTitle
       		print 'Posted ' + postDate + ' ' + postTime
       		print '\n----------------------------------------------\n'

       	print '\n############### CLOSING SPIDER ###############\n'

       	next_page_url = response.urljoin('https://vaguntrader.com/forums/ubbthreads.php/forums/3/3/Handguns_-_VIRGINIA_ONLY/')
       	yield scrapy.Request(next_page_url)
