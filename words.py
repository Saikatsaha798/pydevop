# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 11:31:47 2020

@author: Saikat
"""

def DISPLAYWORDS():
    with open('STORY.TXT','r') as fr:
        l1 = fr.readlines()
        for i in l1:    
            a = i.split(' ')
            for j in a:
                if len(j)<4:
                    print(j)
        fr.close()

DISPLAYWORDS()
