#!/usr/bin/python
#coding:utf-8
'''
name   : testChisqLinearDataset.py
author : ykita
date   : Sat Feb  6 22:55:41 JST 2016
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


N = 10000
n = 100
x = np.random.normal(0.,1.,(N,n))

mean = 0.
sigma = 1.
y = map(lambda xx:func(xx,1,0,error=0),x)


g = TGraphErrors(n)
f = TF1('f','pol1')
h = TH1D('h','',20,0,2)

for i,(xx,yy) in enumerate(zip(x,y)):
    g.Set(0)
    for j,(xxx,yyy) in enumerate(zip(xx,yy)):
        g.SetPoint(j,xxx,yyy+errorFunc(mean,sigma))
        g.SetPointError(j,0,sigma)
    g.Fit(f)
    h.Fill(f.GetChisquare()/(n-2))

gROOT.SetBatch(0)
c = TCanvas("c","",512,512)
gPad.SetGrid(1)
h.Draw()
c.Update()

raw_input('>')

