#!/usr/bin/python
#coding:utf-8
'''
name   : bayesSample01.py
author : ykita
date   : 
memo   :  
'''
import os, os.path
import sys
import pymc
import mymodel

S = pymc.MCMC(mymodel,db='pickle')
S.sample(iter=10000,burn=5000,thin=2)
pymc.Matplot.plot(S)
