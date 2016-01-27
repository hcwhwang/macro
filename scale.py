# !/bin/usr/python

from ROOT import *

h1 = TH1F("h1","h1",100,-5,5)
h2 = TH1F("h2","h2",100,-5,5)
h3 = TH1F("h3","h3",100,-5,5)

h1.FillRandom("gaus")
h2.FillRandom("gaus")
h3.FillRandom("gaus")

h1.Chi2Test(h1,"UUP")
print h1.Chi2Test(h2,"UUWWCHI2/NDF")
c1 = TCanvas("c1","c1",500,500)
h1.Draw("e")
print "Normal : ", h1.Integral()
c2 = TCanvas("c2","c2",500,500)
h2.DrawNormalized("e")
print "DrawNormalized : ", h2.Integral()
c3 = TCanvas("c3","c3",500,500)
h3.Scale(1./h3.Integral())
h3.Sumw2()
h3.Draw("e")
print "Scale : ", h3.Integral()

