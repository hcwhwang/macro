# !/usr/bin/python

from ROOT import *
from array import array
binning = [0,10,50,100]

h = TH1F("h","h",3,array('d',binning))

r = TRandom()

for i in range(1000):
	rN = 100.*r.Uniform()
	h.Fill(rN)

c = TCanvas("c","c",500,500)
h.Draw()
