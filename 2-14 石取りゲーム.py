#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 13 17:20:53 2021

@author: takematsutaiki
"""

stone=30
min=2
max=4

print('交互に'+str(min)+'-'+str(max)+'個の石を取っていき、最後の石を取った方の負けです')

def checkstone(player,stoneCount):
    if (stoneCount<=0):
        if (player=='you'):
            print('あなたの負けです')
        else:
            print('あなたの勝ちです')
        return True
    else:
        return False
    
def getyou():
    global stone
    your=int(input('あなたはいくつとりますか？'))
    
    if (your<min or your>max):
        print('それはダメ')
        return False
    stone -= your
    print('あなたは'+str(your)+'個とりました')
    return True

def getme():
    global stone
    mine=(stone-min)%(min+max)
    if (mine<min):
        mine=min
    if (mine>max):
        mine=max
        
    print('私は'+str(mine)+'個とりました')
    stone -= mine
    
while(stone>0):
    
    print(str(stone)+'個残っています')
    
    if (getyou()==False):
        continue
    
    if (checkstone('you',stone)):
        break
    
    print(str(stone)+'個残っています')
    
    getme()
    
    if (checkstone('me',stone)):
        break
    
print('おしまい')