#!/usr/bin/python
#coding:utf-8
'''
name   : testChisq.py
author : ykita
date   : Thu Feb  4 22:50:02 JST 2016
memo   : think mean of chisquare 
'''
import os, os.path
import sys
import ROOT
from ROOT import *

import numpy as np

N = 1000
n = 100

stack = np.random.normal(0,1.,(N,n))

hists = [ TH1D('h%03d'%i,"",30,-3,3) for i in range(N) ]
fs = [ TF1('f%03d'%i,"gaus",-2,2) for i in range(N) ]
h_chisq = TH1D('h_chisq','',50,0,30)
for i,(f,(hist,data)) in enumerate(zip(fs,(zip(hists,stack)))):
    # print data
    for x in data:
        hist.Fill(x)
    hist.Fit(f)
    h_chisq.Fill(f.GetChisquare()/6.)

c = TCanvas("c","",512,512)
gPad.SetGrid(1)
h_chisq.Draw()
c.SaveAs("byGaus.pdf")
raw_input('>')

