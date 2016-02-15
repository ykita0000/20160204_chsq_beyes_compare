#!/usr/bin/python
#coding:utf-8
'''
name   : testGaussianSquareSum.py
author : ykita
date   : Mon Feb  8 12:48:02 JST 2016
memo   :  
'''
import os, os.path
import sys
import ROOT
from ROOT import *
import numpy as np

N     = 10000
n     = 5
mean  = 0.
sigma = 1.
x = np.random.normal(mean,sigma,(N,n))

hChisq = TH1D('h','',100,0.,8.)
for xx in x:
    Z = np.sum(np.square(xx))
    hChisq.Fill(Z/(n-1)/(sigma*sigma))

c = TCanvas('c','',512,512)
gPad.SetGrid(1)
c.Draw()
# f = TF1('f','ROOT::Math::chisquared_pdf(x,[0],[1])',0,8)
# f.SetParameters(5,0)
# hChisq.Fit(f,"","",0,8)
hChisq.Draw()
c.Update()
raw_input('>')
