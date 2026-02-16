#!/usr/bin/python3
s = open('dna.txt','r').read()
for n in ["A","C","G","T"]:
    print(s.count(n), end=' ')