#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for sequential_verb

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict,
        refDICT       dict,
        pattern       str

    Output:
        resultDICT    dict
"""

from random import sample
import json
import os
import re
from ArticutAPI import Articut
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAT = re.compile("<ACTION_(verb|quantifiedVerb)>([^<]+)\\2(\\2\\2)?</ACTION_(verb|quantifiedVerb)><ACTION_(verb|quantifiedVerb)>\\2(到|\\2)?</ACTION_(verb|quantifiedVerb)>|<ACTION_verb>([^<]+)</ACTION_verb><ACTION_verb>\\4</ACTION_verb>|(<ACTION_verb>[^<]+</ACTION_verb>)\\9\\9?")
try:
    accountInfo = json.load(open(os.path.join(BASE_PATH, "account.info"), encoding="utf-8"))
    USERNAME = accountInfo["username"]
    API_KEY = accountInfo["api_key"]
except Exception as e:
    print("[ERROR] AccountInfo => {}".format(str(e)))
    USERNAME = ""
    API_KEY = ""

articut = Articut(USERNAME, API_KEY)

DEBUG = True
CHATBOT_MODE = False

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_sequential_verb.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG:
        print("[sequential_verb] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT, pattern=""):
    debugInfo(inputSTR, utterance)
    if utterance == "去鐵路上載客人":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            try:
                resultPOS = articut.parse(inputSTR)["result_pos"][0]
                if PAT.match(resultPOS):
                    pass
                else:
                    resultDICT["連謂/兼語"].append(1)
            except:
                pass

    if utterance == "你先去外面等一下":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["連謂/兼語"].append(1)

    if utterance == "我等一下可以玩第三籃嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["連謂/兼語"].append(1)

    if utterance == "媽媽幫我拿":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["連謂/兼語"].append(1)

    if utterance == "出去玩":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["連謂/兼語"].append(1)

    if utterance == "你幫我曡高高":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["連謂/兼語"].append(1)

    if utterance == "給你吃":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["連謂/兼語"].append(1)

    if utterance == "來幫忙":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["連謂/兼語"].append(1)

    if utterance == "保證他不會倒":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["連謂/兼語"].append(1)

    if utterance == "喝開水噎到了":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["連謂/兼語"].append(1)

    if utterance == "帶他們兩個來":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["連謂/兼語"].append(1)

    if utterance == "幫你多吃":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["連謂/兼語"].append(1)

    if utterance == "幫小豬打針":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["連謂/兼語"].append(1)

    if utterance == "打開看":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["連謂/兼語"].append(1)

    if utterance == "教你怎麼蓋":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["連謂/兼語"].append(1)

    if utterance == "爬上去走一走":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["連謂/兼語"].append(1)

    if utterance == "等一下可以玩":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["連謂/兼語"].append(1)

    if utterance == "給人家坐":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["連謂/兼語"].append(1)

    if utterance == "給公主住":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["連謂/兼語"].append(1)

    if utterance == "要剪掉":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["連謂/兼語"].append(1)

    if utterance == "要進去了":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["連謂/兼語"].append(1)

    if utterance == "開始玩了":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["連謂/兼語"].append(1)

    if utterance == "開始要用":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["連謂/兼語"].append(1)

    if utterance == "幫我的連起來":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["連謂/兼語"].append(1)

    return resultDICT