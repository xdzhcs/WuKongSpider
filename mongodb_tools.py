#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.wukong
question_collection = db.question
user_collection = db.user
answer_collection = db.answer
comment_collection = db.comment


def save_question(question):
    try:
        question_collection.insert_one(question)
    except RuntimeError as e:
        logging.error("保存问题失败:"+str(e))


def save_user(user):
    try:
        user_collection.insert_one(user)
    except RuntimeError as e:
        logging.error("保存用户失败:"+str(e))


def save_comment(comment):
    try:
        comment_collection.insert_one(comment)
    except RuntimeError as e:
        logging.error("保存评论失败:"+str(e))


def save_answer(answer):
    try:
        answer_collection.insert_one(answer)
    except RuntimeError as e:
        logging.error("保存回答失败:"+str(e))




