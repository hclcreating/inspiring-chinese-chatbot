import jieba
import json

# 將佳句(responses.txt)中的句子拆解，去掉no_sense的字
# 將dictionary(key:關鍵字; value:出現的句子編號)寫入json
# dictionary e.g.:
# {"失敗":[0,3,5,23...], "成功":[4,6,7...]}
# 更新response就要執行一次

no_sence_words = []
with open("all_sentences/no_sence_word_list.txt") as f:
    no_sence = f.readlines()
    for word in no_sence:
        no_sence_words.append(word.strip())

response_dict = {}

with open("all_sentences/responses.txt") as f:
    response_list = f.readlines()
    for i in range(len(response_list)):
        words = jieba.cut(response_list[i], cut_all=False)
        for word in words:
            if word in no_sence_words:
                pass
            else:
                try:
                    response_dict[word].append(i)
                except Exception:
                    response_dict[word] = [i]

with open("response_dict.json", "w") as f:
    json.dump(response_dict, f)
