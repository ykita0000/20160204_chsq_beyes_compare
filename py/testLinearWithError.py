#!/usr/bin/python
#coding:utf-8
'''
name   : testLinearWithError.py
author : ykita
date   : Sat Feb  6 12:14:58 JST 2016
memo   :  
'''
import os, os.path
import sys
import ROOT
from ROOT import *
import numpy as np

def errorFunc(mean=.0,sigma=.5):
    return gRandom.Gaus(mean,sigma)

def func(x,a,b,error=0.):
    return a*x+b+error

gROOT.SetBatch(1)
n = 10000
x = np.random.normal(0.,5.,(n))

mean = 0.
sigma = 5.
y = map(lambda xx:func(xx,1,0,error=errorFunc(mean,sigma)),x)

g = TGraphErrors(n)
for i,(xx,yy) in enumerate(zip(x,y)):
    g.SetPoint(i,xx,yy)
    g.SetPointError(i,0,sigma)
    
gROOT.SetBatch(0)
c = TCanvas("c","",512,512)
gPad.SetGrid(1)
g.Fit('pol1')
g.Draw('AP')
c.Update()
raw_input('>')
 

