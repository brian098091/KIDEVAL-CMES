#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for existential_sentence

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
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_existential_sentence.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG:
        print("[existential_sentence] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT, pattern=""):
    debugInfo(inputSTR, utterance)
    if utterance == "有一瓶":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["存現句"].append(1)

    if utterance == "有錢":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["存現句"].append(1)

    if utterance == "住了很多公主":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["存現句"].append(1)

    if utterance == "地上躺著一隻狗":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["存現句"].append(1)

    if utterance == "還有車":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["存現句"].append(1)

    if utterance == "還有一個":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["存現句"].append(1)

    if utterance == "上面還有":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["存現句"].append(1)

    if utterance == "外面有一個":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["存現句"].append(1)

    if utterance == "我們家有":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["存現句"].append(1)

    if utterance == "有一個人":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["存現句"].append(1)

    if utterance == "裡面沒有":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["存現句"].append(1)

    if utterance == "這有":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["存現句"].append(1)

    if utterance == "這裡會有":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["存現句"].append(1)

    if utterance == "這裡有兩個":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["存現句"].append(1)

    if utterance == "這邊有":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["存現句"].append(1)

    if utterance == "還有一個車":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["存現句"].append(1)

    if utterance == "才有五個":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["存現句"].append(1)

    if utterance == "捷運站才有":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["存現句"].append(1)

    if utterance == "還有ok繃":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["存現句"].append(1)

    if utterance == "有一個細細長長的街":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["存現句"].append(1)

    if utterance == "有漱口水":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["存現句"].append(1)

    if utterance == "可以有一個":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["存現句"].append(1)

    if utterance == "這樣才有五個":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["存現句"].append(1)

    if utterance == "都要有三角形":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["存現句"].append(1)

    if utterance == "有車要進來了":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["存現句"].append(1)

    return resultDICT