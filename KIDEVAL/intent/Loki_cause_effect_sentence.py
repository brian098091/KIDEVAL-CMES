#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for cause_effect_sentence

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
from ArticutAPI import Articut
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
try:
    accountDICT = json.load(open("../account.info", encoding="utf-8"))
    articut = Articut(username=accountDICT["username"], apikey=accountDICT["apikey"])
except:
    #pass
    articut = Articut()

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_cause_effect_sentence.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG:
        print("[cause_effect_sentence] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT, pattern=""):
    debugInfo(inputSTR, utterance)
    if utterance == "下雨然後放晴":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["帶連詞複句"].append(1)

    if utterance == "但都不知道在那":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["帶連詞複句"].append(1)

    if utterance == "只要下雨我就出門":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["帶連詞複句"].append(1)

    if utterance == "可是你的只有一個":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["帶連詞複句"].append(1)

    if utterance == "可是這":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["帶連詞複句"].append(1)

    if utterance == "因為下雨所以":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["帶連詞複句"].append(1)

    if utterance == "如果下雨":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["帶連詞複句"].append(1)

    if utterance == "對可是你剛才沒有打到":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["帶連詞複句"].append(1)

    if utterance == "所以":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            try:
                articutDICT = articut.parse(inputSTR)
                if articutDICT["status"] == True:
                    if "ACTION_" in articutDICT["result_pos"][0] or "VerbP" in articutDICT["result_pos"][0]:
                        resultDICT["帶連詞複句"].append(1)
                    else:
                        pass
            except:
                pass

    if utterance == "所以我":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["帶連詞複句"].append(1)

    if utterance == "然後":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if inputSTR == utterance:
                pass
            else:
                try:
                    articutDICT = articut.parse(inputSTR)
                    if articutDICT["status"] == True:
                        if "<ACTION_verb>爬<" in articutDICT["result_pos"][0] and articutDICT["result_pos"][0].count("<ACTION_verb")==1:
                            pass
                        elif "<ACTION_verb>跳<" in articutDICT["result_pos"][0] and articutDICT["result_pos"][0].count("<ACTION_verb")==1:
                            pass
                        elif "<ACTION_verb>住<" in articutDICT["result_pos"][0] and articutDICT["result_pos"][0].count("<ACTION_verb")==1:
                            pass
                        elif "<ACTION_verb>坐<" in articutDICT["result_pos"][0] and articutDICT["result_pos"][0].count("<ACTION_verb")==1:
                            pass
                        elif "<ACTION_verb>蓋" in articutDICT["result_pos"][0] and articutDICT["result_pos"][0].count("<ACTION_verb")==1:
                            pass
                        elif "<ACTION_verb>有<" in articutDICT["result_pos"][0] and articutDICT["result_pos"][0].count("<ACTION_verb")==1:
                            pass
                        elif "<ACTION_verb>擺<" in articutDICT["result_pos"][0] and articutDICT["result_pos"][0].count("<ACTION_verb")==1:
                            pass
                        elif "<ACTION_verb>放<" in articutDICT["result_pos"][0] and articutDICT["result_pos"][0].count("<ACTION_verb")==1:
                            pass
                        elif "<ACTION_verb>換<" in articutDICT["result_pos"][0] and articutDICT["result_pos"][0].count("<ACTION_verb")==1:
                            pass
                        elif "<ACTION_verb>拿<" in articutDICT["result_pos"][0] and articutDICT["result_pos"][0].count("<ACTION_verb")==1:
                            pass
                        elif "<ACTION_verb>按<" in articutDICT["result_pos"][0] and articutDICT["result_pos"][0].count("<ACTION_verb")==1:
                            pass
                        elif "<ACTION_verb>切<" in articutDICT["result_pos"][0] and articutDICT["result_pos"][0].count("<ACTION_verb")==1:
                            pass
                        elif "<ACTION_verb>變<" in articutDICT["result_pos"][0] and articutDICT["result_pos"][0].count("<ACTION_verb")==1:
                            pass
                        elif "<ACTION_verb>量<" in articutDICT["result_pos"][0] and articutDICT["result_pos"][0].count("<ACTION_verb")==1:
                            pass
                        elif "要</ACTION_verb>" in articutDICT["result_pos"][0] and articutDICT["result_pos"][0].count("<ACTION_verb")==1:
                            pass
                        elif "ACTION_" not in articutDICT["result_pos"][0]:
                            pass
                        else:
                            resultDICT["帶連詞複句"].append(1)
                except:
                    pass


    if utterance == "然後呢":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            if inputSTR.endswith(utterance):
                pass
            else:
                resultDICT["帶連詞複句"].append(1)

    if utterance == "然後我再":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["帶連詞複句"].append(1)

    if utterance == "然後我把":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["帶連詞複句"].append(1)

    if utterance == "如果有生病的":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["帶連詞複句"].append(1)

    if utterance == "可是也沒有藥膏":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["帶連詞複句"].append(1)

    if utterance == "可是只有一個":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["帶連詞複句"].append(1)

    if utterance == "可是我沒有叉子":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["帶連詞複句"].append(1)

    if utterance == "可是背又不是心臟":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["帶連詞複句"].append(1)

    if utterance == "可是這裡還沒有這一種":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["帶連詞複句"].append(1)

    if utterance == "囉可是不夠":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["帶連詞複句"].append(1)

    if utterance == "因為他不乖":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["帶連詞複句"].append(1)

    if utterance == "因為你很勇敢":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["帶連詞複句"].append(1)

    if utterance == "因為你的手比較大":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["帶連詞複句"].append(1)

    if utterance == "因為呢這個沒有顏色":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["帶連詞複句"].append(1)

    if utterance == "因為它就長啊":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["帶連詞複句"].append(1)

    if utterance == "因為我的花園在這裡":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["帶連詞複句"].append(1)

    if utterance == "因為這個下面是藍的":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["帶連詞複句"].append(1)

    if utterance == "因為這個本來就冰冰的":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["帶連詞複句"].append(1)

    if utterance == "因為這是一個魔法":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["帶連詞複句"].append(1)

    if utterance == "因為這是他的翅膀":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["帶連詞複句"].append(1)

    if utterance == "因為這樣子才可以":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["帶連詞複句"].append(1)

    if utterance == "因為這樣子才對":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["帶連詞複句"].append(1)

    if utterance == "因為這樣子是":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["帶連詞複句"].append(1)

    if utterance == "因為還有更多人":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["帶連詞複句"].append(1)

    if utterance == "因為那這樣就好喔":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["帶連詞複句"].append(1)

    if utterance == "所以不要":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["帶連詞複句"].append(1)

    if utterance == "所以沒有紅色":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["帶連詞複句"].append(1)

    if utterance == "然後再加藥水進去":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["帶連詞複句"].append(1)

    if utterance == "然後再蓋一個這個":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["帶連詞複句"].append(1)

    if utterance == "然後再量體溫一次":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["帶連詞複句"].append(1)

    if utterance == "然後如果":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["帶連詞複句"].append(1)

    return resultDICT