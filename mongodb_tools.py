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

# 保存问题
def save_question(question):
    try:
        question_collection.insert_one(question)
    except RuntimeError as e:
        logging.error("保存问题失败:"+str(e))

# 保存用户信息
def save_user(user):
    try:
        user_collection.insert_one(user)
    except RuntimeError as e:
        logging.error("保存用户失败:"+str(e))

# 保存评论
def save_comment(comment):
    try:
        comment_collection.insert_one(comment)
    except RuntimeError as e:
        logging.error("保存评论失败:"+str(e))

# 保存回答
def save_answer(answer):
    try:
        answer_collection.insert_one(answer)
    except RuntimeError as e:
        logging.error("保存回答失败:"+str(e))


def get_question_by_qid(qid):
    try:
        return question_collection.find_one({"qid":qid})
    except RuntimeError as e:
        logging.error("查询问题失败:" + str(e))
    pass

def get_answer_by_answer_id(answer_id):
    try:
        return answer_collection.find_one({"ansid":answer_id})
    except RuntimeError as e:
        logging.error("查询问题失败:" + str(e))


if __name__ == '__main__':
    print(get_answer_by_answer_id('6426163854085980418'))
    print(get_question_by_qid('6428893512418197761'))

