#!/usr/bin/python

import sys
from statistics import mode
from collections import Counter
import pickle

# url = 'https://s3.amazonaws.com/cs205amazonreview/data.p'
url = './data.p'
prev_text = None
scores = []
#print('score,text')
for line in sys.stdin:
    try:
        text, score = line.split( '\t' )
        
        if text!=prev_text:
            if prev_text is not None:
                c = Counter(scores)
                top_scores = c.most_common(5)
                top_scores.sort()
                # print(top_scores[0][0] + ',' + prev_text)
                s = top_scores[0][0] + '\t' + prev_text
                pickle.dump(s, url)
            prev_text = text
            scores = []
        scores.append(score[:-1])
    except ValueError: pass

top_scores = c.most_common(5)
top_scores.sort()
# print(top_scores[0][0] + ',' + prev_text)
s = top_scores[0][0] + '\t' + prev_text
pickle.dump(s, url)