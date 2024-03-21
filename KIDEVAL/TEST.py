import pandas as pd

def convert_csv_to_dict(csv_file_path):
    df = pd.read_csv(csv_file_path)  # 直接跳过前两行

    structure_to_column = {
        '量-個': '名詞短語',
        '量-特': 'Unnamed: 3',
        'X的': 'Unnamed: 4',
        'X的Y': 'Unnamed: 5',
        '方位': 'Unnamed: 6',
        '體貌': '動詞短語',
        '結果補語': 'Unnamed: 8',
        '趨向補語': 'Unnamed: 9',
        '情態補語': 'Unnamed: 10',
        '可能補語': 'Unnamed: 11',
        '數量補語': 'Unnamed: 12',
        '動前介詞': '介詞短語',
        '動後介詞': 'Unnamed: 14',
        '把字句': '句子',
        '被字句': 'Unnamed: 16',
        '存現句': 'Unnamed: 17',
        '連謂/兼語': 'Unnamed: 18',
        '帶連詞複句': 'Unnamed: 19',
        '緊縮複句': 'Unnamed: 20',
        '感知/心理狀態': 'Unnamed: 21'
    }

    sentence_structure_dict = {}

    for _, row in df.iloc[2:].iterrows():
        sentence = row['Unnamed: 1'].replace(' ','').strip('.').strip('?') 
        if sentence:
            sentence_structure_dict[sentence] = {}
            for structure, column_name in structure_to_column.items():
                sentence_structure_dict[sentence][structure] = row[column_name] if pd.notna(row[column_name]) else ""

    return sentence_structure_dict

if __name__ == "__main__":
    csv_file_path = './語法指標語料.csv'  
    sentence_dict = convert_csv_to_dict(csv_file_path)
    #for key, value in sentence_dict.items():
        #print(f"'{key}': {value}")
        
    filterLIST = []
    splitLIST = ["！", "，", "。", "？", "!", ",", "\n", "；", "\u3000", ";"]
    # 設定參考資料
    # refDICT = {"key":[]} #refDICT 指定 key 需為字串 str，其值為一空列表 list
    refDICT = {
        '量-個': [],
        '量-特': [],
        'X的': [],
        'X的Y': [],
        '方位': [],
        '體貌': [],
        '結果補語': [],
        '趨向補語': [],
        '情態補語':[],
        '可能補語':[],
        '數量補語':[],
        '動前介詞':[],
        '動後介詞': [],
        '把字句': [],
        '被字句': [],
        '存現句': [],
        '連謂/兼語': [],
        '帶連詞複句': [],
        '緊縮複句': [],
        '感知/心理狀態': []
    }    
    from KIDEVAL import execLoki
    sentence_keys = list(sentence_dict.keys())
    false_list = []
    diff_dict_c = {}
    diff_dict_w = {}
    with open('wrong.txt', 'w',encoding='utf-8') as f:
        for inputSTR in sentence_keys:

            resultDICT = execLoki(content=inputSTR, splitLIST=splitLIST, refDICT=refDICT)

            itemScoreDICT = {}
            for i,k in zip(sentence_dict[inputSTR],refDICT):
                if sum(resultDICT[k])== 0:
                    itemScoreDICT[i] = ""
                else:
                    itemScoreDICT[i] = str(sum(resultDICT[k]))
            for key, value in sentence_dict[inputSTR].items():
                if key in itemScoreDICT:
                    if value != itemScoreDICT[key]:
                        false_list.append(key)
                        diff_dict_c[key] = value
                        diff_dict_w[key] = itemScoreDICT[key]
                        
            if(len(false_list) > 0):
                print(inputSTR,false_list,file=f)
                print("Correct",diff_dict_c,file=f)
                print("Wrong",diff_dict_w,file=f,end='\n\n')    
                false_list.clear() 
                diff_dict_c.clear()
                diff_dict_w.clear()  
