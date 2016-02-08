#!/usr/bin/python
#coding:utf-8
'''
name   : testErrorTerm.py
author : ykita
date   : Sat Feb  6 10:20:34 JST 2016
memo   :  
'''
import os, os.path
import sys
import ROOT
from ROOT import *
import numpy as np

def errorFunc(mean=.0,sigma=.5):
    return gRandom.Gaus(mean,sigma)

def func(x,a,b):
    return a*x+b+errorFunc()

n = 200
listIn = np.linspace(0,20,n)
listOut = map(lambda x:func(x,1,0),listIn)
g = TGraph(n)
for i,(x,xx) in enumerate(zip(listIn,listOut)):
    print x,xx
    g.SetPoint(i,x,xx)

g.Fit('pol1')
g.Draw('APL')
raw_input('>')
 
