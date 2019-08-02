import os
import jieba
import jieba.analyse
import numpy as np
import json

class simhash:

    def __init__(self, content):
        self.simhash = self.simhash(content)

    def __str__(self):
        return str(self.simhash)

    def simhash(self, content):
        dir = os.path.dirname(__file__)
        seg = jieba.cut(content)
        jieba.analyse.set_stop_words(os.path.join(dir, './stop_words.txt'))
        keyWord = jieba.analyse.extract_tags('|'.join(seg), topK = 20, withWeight = True, allowPOS = ())
        keyList = []

        for feature, weight in keyWord:
            weight = int(weight * 20) 
            feature = self.string_hash(feature) 
            temp = []

            for i in feature:
                if(i == '1'):
                    temp.append(weight)  
                else:
                    temp.append(-weight)

            keyList.append(temp)
        list1 = np.sum(np.array(keyList), axis=0)

        if(keyList == []):
            return '00'

        simhash = ''

        for i in list1:
            if(i > 0):
                simhash = simhash + '1'
            else:
                simhash = simhash + '0'

        return simhash

    def string_hash(self, source):
        if source == "":
            return 0
        else:
            x = ord(source[0]) << 7
            m = 1000003
            mask = 2 ** 128 - 1

            for c in source:
                x = ((x * m) ^ ord(c)) & mask

            x ^= len(source)

            if x == -1:
                x = -2
            x = bin(x).replace('0b', '').zfill(64)[-64:]

            return str(x)

    def hammingDis(self, com):
        t1 = '0b' + self.simhash
        t2 = '0b' + com.simhash
        n = int(t1, 2) ^ int(t2, 2)
        i = 0

        while n:
            n &= (n-1)
            i += 1

        return i
