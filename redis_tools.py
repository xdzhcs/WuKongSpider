#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import redis
import logging
import time
import constant as CONST

logging.basicConfig( level=logging.INFO)

r = None
try:
    pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    logging.info('redis连接正常')
except RuntimeError as e:
    logging.error('redis连接失败')


# 添加已经爬取过的问题id
def add_clawed_question_id(qid):
    t = int(time.time())
    r.zadd(CONST.REDIS_CLAWED_QUESTION_IDS,qid,t)
    pass


# 添加已经爬取过的回答id
def add_clawed_answer_id(ans_id):
    t = int(time.time())
    r.zadd(CONST.REDIS_CLAWED_ANSWER_IDS,ans_id,t)


# 添加已经爬取过的回答id
def add_clawed_comment_id(ans_id):
    t = int(time.time())
    r.zadd(CONST.REDIS_CLAWED_COMMENT_IDS,ans_id,t)


# 添加已经爬取过的用户id
def add_clawed_user_id(ans_id):
    t = int(time.time())
    r.zadd(CONST.REDIS_CLAWED_COMMENT_IDS,ans_id,t)


# 添加到问题队列中
def add_to_question_queue(qid):
    t = int(time.time())
    r.lpush(CONST.REDIS_TOCLAW_QUESTION_IDS,qid)


# 添加到评论队列中
def add_to_comment_queue(comment_id):
    t = int(time.time())
    r.lpush(CONST.REDIS_TOCLAW_QUESTION_IDS,comment_id)


# 添加到回答队列中
def add_to_answer_queue(answer_id):
    t = int(time.time())
    r.lpush(CONST.REDIS_CLAWED_ANSWER_IDS,answer_id)

