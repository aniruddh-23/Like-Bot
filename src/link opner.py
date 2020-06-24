# -*- coding: utf-8 -*-
"""
Created on Wed May 27 13:40:50 2020

@author: Aayu
"""
import webbrowser

def extract(link_list):
    ll=[]
    for l in link_list:
        ll.append(l.split(' ')[1])
    return ll

    
links = open("ig_links.txt","r")
ll=[]
for i in links:
    ll.append(i)
ll=extract(ll)
c=0
for i in ll:
    c+=1
    if c>50:
        c=0
        input()
    webbrowser.open(i)
print("complete")