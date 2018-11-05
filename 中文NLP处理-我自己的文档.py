# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 17:30:51 2018

@author: freeze
"""

#import os
import jieba
import re
from gensim.models import word2vec
filepath="C:\\Users\\freeze\\Desktop\\freeze的故事.txt"
pattern=re.compile(r'\S')
pa=re.compile(r'\，|\。|；|“|”|！|？|：|《|》|（|）|\n')
f=open(filepath)


content=[]
split_content=[]
line=f.readline()
#读入文件内容
while line:
    if(re.search(pattern,line)):
        content.append(re.sub(pa,'',line))
    line=f.readline()
#形成二维的分词列表 
for s in content:
    seg=jieba.cut(s,cut_all=True)
    List=[]
    for s in seg:
        if(re.search(pattern,s)):
            List.append(s)
    split_content.append(List)
#导入模型
model=word2vec.Word2Vec(split_content,size=10,min_count=1,window=15)
model.wv['魔鬼']
model.most_similar(['魔鬼'])




