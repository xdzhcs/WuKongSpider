#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import time
import user_agents as ua
import logging
import mongodb_tools as mg
import redis_tools as rds

logging.basicConfig( level=logging.INFO)


class QuestionSpider:

    @staticmethod
    def get_questions_by_tag():
        url = 'https://www.wukong.com/wenda/web/nativefeed/brow/'
        # https://www.wukong.com/wenda/web/nativefeed/brow/?concern_id=6215497899397089794&t=1515304700301&max_behot_time=1515296272&_signature=Uq7eCxATCQCcxVjZIMGTclKu3h
        para = {'concern_id':'6215497899397089794',
                '1515304700301':int(time.time()*1000),
                'max_behot_time':1515296272
                }
        r = requests.get(url,params=para)
        r.headers.update({'user-agent':ua.get_random_ua()})
        j = json.loads(r.text)

        # 解析json
        if j.get('err_no',-1) != 0:
            logging.error('获取问题列表信息错误错误，问题id')
            return

        if j.get('data',None):
            for q in j['data']:
                question = q['question']
                question['behot_time']=q['behot_time']
                answer = q['answer']
                mg.save_answer(answer)
                mg.save_question(question)
                # rds.add_to_question_queue(q['qid'])
                # rds.add_to_user_queue(q['question']['user']['user_id'])
                # rds.add_to_user_queue(q['question']['answer']['user']['user_id'])







class AnswerSpider:
    pass

class UserSpider:
    pass

class CommentSpider:
    pass


if __name__ == '__main__':
    QuestionSpider.get_questions_by_tag()