import nltk
from nltk.corpus import words
from statistics import median, mode
from itertools import combinations
import sys
import csv

# 1. Avoid trap if possible
# 2. Break the trap early if possible 

trap_length= int(sys.argv[1])

def compare(w1, w2):
    c = 0
    for i in range(5):
        c += (w1[i] == w2[i])

    return c

def same_indx(w1, w2, indx):
    c = 0
    for i in indx:
        c += (w1[i] == w2[i])

    if c == trap_length:
        return True
    else:
        return False

def avg(w):
    return sum(map(len,w))/len(w)

def median_(w):
    return median(map(len,w))

def mode_(w):
    return mode(map(len,w))

worlde = [i.upper() for i in words.words() if len(i) == 5]

four_common = []
l = []
for i in worlde:
    if l: four_common.append(l)
    l = [i]
    for j in worlde:
        if i != j:
            if compare(i, j) == trap_length:
                l.append(j)

# Using that list, find combinations that are common in the same location
indices = list(combinations(range(5), trap_length))

fl = []

for i in four_common:
    if len(i) == 1:
        fl.append(i)
        continue

    first = i[0]
    for k in indices:
        l = [first]
        for j in i:
            if j!=first:
                if same_indx(first, j, k):
                    l.append(j)
        if len(l) > 1:
            fl.append(l)

print(avg(fl))
print(median_(fl))
print(mode_(fl))
