#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for directional

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
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_directional.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG:
        print("[directional] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT, pattern=""):
    debugInfo(inputSTR, utterance)
    if utterance == "房間外面":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["方位"].append(1)
            #try:
                #resultPOS = articut.parse(inputSTR)["result_pos"][0]
                #if resultPOS.startswith("<ENTITY") or resultPOS.startswith("<LOCATION"):
                    #resultDICT["方位"].append(1)
                #elif "</ENTITY_nounHead><RANGE_locality>" in resultPOS:
                    #resultDICT["方位"].append(1)
                #elif "</ENTITY_nouny><RANGE_locality>" in resultPOS:
                    #resultDICT["方位"].append(1)
                #elif "</ENTITY_noun><RANGE_locality>" in resultPOS:
                    #resultDICT["方位"].append(1)
                #elif "</ENTITY_oov><RANGE_locality>" in resultPOS:
                    #resultDICT["方位"].append(1)
                #elif "</ENTITY_pronoun><RANGE_locality>" in resultPOS:
                    #resultDICT["方位"].append(1)
                #else:
                    #pass
            #except:
                #pass

    if utterance == "這邊":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["方位"].append(1)

    if utterance == "這上面":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["方位"].append(1)

    if utterance == "這下頭":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["方位"].append(1)

    if utterance == "上面":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["方位"].append(1)

    if utterance == "這裡的":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["方位"].append(1)

    if utterance == "是上面":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["方位"].append(1)

    if utterance == "放下面":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["方位"].append(1)

    if utterance == "裡面":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if inputSTR == "後面":
                pass
            else:
                resultDICT["方位"].append(1)

    if utterance == "這裡面":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["方位"].append(1)

    if utterance == "這個下面":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["方位"].append(1)

    if utterance == "的後面":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["方位"].append(1)

    if utterance == "兩邊":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["方位"].append(1)

    if utterance == "另外一邊":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["方位"].append(1)

    if utterance == "哪裡":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["方位"].append(1)

    if utterance == "在後面":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["方位"].append(1)

    if utterance == "坐另外一邊":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["方位"].append(1)

    if utterance == "貼在這個上":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["方位"].append(1)

    if utterance == "他前面上車":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["方位"].append(1)

    if utterance == "他哪裡要":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["方位"].append(1)

    if utterance == "你哪裡有":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["方位"].append(1)

    if utterance == "前面也一樣":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["方位"].append(1)

    if utterance == "在哪邊":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["方位"].append(1)

    if utterance == "在手上":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["方位"].append(1)

    if utterance == "在裡面跳舞":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["方位"].append(1)

    if utterance == "在這裡":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["方位"].append(1)

    if utterance == "寶盒裡面有":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["方位"].append(1)

    if utterance == "打他哪裡":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["方位"].append(1)

    if utterance == "放這邊短":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["方位"].append(1)

    if utterance == "旁邊要有":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["方位"].append(1)

    if utterance == "是這邊":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["方位"].append(1)

    if utterance == "裡面有":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["方位"].append(1)

    if utterance == "這裡也可以":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["方位"].append(1)

    if utterance == "這裡也是":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["方位"].append(1)

    if utterance == "這邊再兩個":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["方位"].append(1)

    if utterance == "短扁放這邊短":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["方位"].append(1)

    if utterance == "旁邊要":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["方位"].append(1)
    return resultDICT