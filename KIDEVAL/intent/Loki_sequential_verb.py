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
            pat = re.compile("<ACTION_quantifiedVerb>([^<])\\1</ACTION_quantifiedVerb><ACTION_verb>\\1</ACTION_verb>")
            try:
                resultPOS = articut.parse(inputSTR)["result_pos"][0]
                if pat.match(resultPOS):
                    pass
                else:
                    resultDICT["連謂/兼語"].append(1)
            
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

    return resultDICT