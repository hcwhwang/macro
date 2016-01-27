import sys, os
from ROOT import *
from array import array

contours = array('i', [kGreen+1, kBlue, kYellow, kOrange+1, kMagenta, kRed, kCyan])
gStyle.SetPalette(len(contours), contours)

gStyle.SetOptStat(0)
totRunNumber = 0
for line in sorted(os.listdir(".")):
        if not line.endswith(".root") or not line.startswith("DQM_"): continue
        totRunNumber += 1

diskNXBin = 36
#diskNYBin = 2
diskNYBin = 6
wheelNXBin = 12
#wheelNYBin = 10
wheelNYBin = 21

hRunVsDM1 = TH2F("hRunVsDM1","disk-1;Run number index;Roll index",totRunNumber,1,totRunNumber+1,diskNXBin*diskNYBin,0,diskNXBin*diskNYBin)
hRunVsDM2 = TH2F("hRunVsDM2","disk-2;Run number index;Roll index",totRunNumber,1,totRunNumber+1,diskNXBin*diskNYBin,0,diskNXBin*diskNYBin)
hRunVsDM3 = TH2F("hRunVsDM3","disk-3;Run number index;Roll index",totRunNumber,1,totRunNumber+1,diskNXBin*diskNYBin,0,diskNXBin*diskNYBin)
hRunVsDP1 = TH2F("hRunVsDP1","disk1;Run number index;Roll index",totRunNumber,1,totRunNumber+1,diskNXBin*diskNYBin,0,diskNXBin*diskNYBin)
hRunVsDP2 = TH2F("hRunVsDP2","disk2;Run number index;Roll index",totRunNumber,1,totRunNumber+1,diskNXBin*diskNYBin,0,diskNXBin*diskNYBin)
hRunVsDP3 = TH2F("hRunVsDP3","disk3;Run number index;Roll index",totRunNumber,1,totRunNumber+1,diskNXBin*diskNYBin,0,diskNXBin*diskNYBin)

hDiskBookList = [hRunVsDM1,hRunVsDM2,hRunVsDM3,hRunVsDP1,hRunVsDP2,hRunVsDP3]

hRunVsWM1 = TH2F("hRunVsWM1","wheel-1;Run number index;Roll index",totRunNumber,1,totRunNumber+1,wheelNXBin*wheelNYBin,0,wheelNXBin*wheelNYBin)
hRunVsWM2 = TH2F("hRunVsWM2","wheel-2;Run number index;Roll index",totRunNumber,1,totRunNumber+1,wheelNXBin*wheelNYBin,0,wheelNXBin*wheelNYBin)
hRunVsW00 = TH2F("hRunVsW00","wheel0;Run number index;Roll index",totRunNumber,1,totRunNumber+1,wheelNXBin*wheelNYBin,0,wheelNXBin*wheelNYBin)
hRunVsWP1 = TH2F("hRunVsWP1","wheel1;Run number index;Roll index",totRunNumber,1,totRunNumber+1,wheelNXBin*wheelNYBin,0,wheelNXBin*wheelNYBin)
hRunVsWP2 = TH2F("hRunVsWP2","wheel2;Run number index;Roll index",totRunNumber,1,totRunNumber+1,wheelNXBin*wheelNYBin,0,wheelNXBin*wheelNYBin)

hWheelBookList = [hRunVsWM1,hRunVsWM2,hRunVsW00,hRunVsWP1,hRunVsWP2]

levels = array('d', [x+0.5 for x in range(8)])
for h in hDiskBookList + hWheelBookList:
	h.SetContour(len(levels), levels)

lineNumber = 0
for line in sorted(os.listdir(".")):
        if not line.endswith(".root") or not line.startswith("DQM_"): continue

        runNumber = line.split("_")[2][4:]
	lineNumber += 1	

        f = TFile.Open(line)
        hDM1 = f.Get("DQMData/Run %s/RPC/Run summary/Muon/SummaryHistograms/RPCChamberQuality_Ring_vs_Segment_Disk-1" % runNumber)
        hDM2 = f.Get("DQMData/Run %s/RPC/Run summary/Muon/SummaryHistograms/RPCChamberQuality_Ring_vs_Segment_Disk-2" % runNumber)
        hDM3 = f.Get("DQMData/Run %s/RPC/Run summary/Muon/SummaryHistograms/RPCChamberQuality_Ring_vs_Segment_Disk-3" % runNumber)
        hDP1 = f.Get("DQMData/Run %s/RPC/Run summary/Muon/SummaryHistograms/RPCChamberQuality_Ring_vs_Segment_Disk1" % runNumber)
        hDP2 = f.Get("DQMData/Run %s/RPC/Run summary/Muon/SummaryHistograms/RPCChamberQuality_Ring_vs_Segment_Disk2" % runNumber)
        hDP3 = f.Get("DQMData/Run %s/RPC/Run summary/Muon/SummaryHistograms/RPCChamberQuality_Ring_vs_Segment_Disk3" % runNumber)
        hWM1 = f.Get("DQMData/Run %s/RPC/Run summary/Muon/SummaryHistograms/RPCChamberQuality_Roll_vs_Sector_Wheel-1" % runNumber)
        hWM2 = f.Get("DQMData/Run %s/RPC/Run summary/Muon/SummaryHistograms/RPCChamberQuality_Roll_vs_Sector_Wheel-2" % runNumber)
        hW00 = f.Get("DQMData/Run %s/RPC/Run summary/Muon/SummaryHistograms/RPCChamberQuality_Roll_vs_Sector_Wheel0" % runNumber)
        hWP1 = f.Get("DQMData/Run %s/RPC/Run summary/Muon/SummaryHistograms/RPCChamberQuality_Roll_vs_Sector_Wheel1" % runNumber)
        hWP2 = f.Get("DQMData/Run %s/RPC/Run summary/Muon/SummaryHistograms/RPCChamberQuality_Roll_vs_Sector_Wheel2" % runNumber)
        hDiskList = [hDM1,hDM2,hDM3,hDP1,hDP2,hDP3]
	hWheelList = [hWM1,hWM2,hW00,hWP1,hWP2]
        hOrder = 0
        for h in hDiskList:
                yBinOrder = 0
		for j in range(6):
			for i in range(36):
                                if  not h.GetXaxis().GetBinLabel(i+1) or not h.GetYaxis().GetBinLabel(j+1): continue
				value = h.GetBinContent(i+1,j+1)
				if value == 0: continue
                                yBinOrder += 1
                                hDiskBookList[hOrder].SetBinContent(lineNumber,yBinOrder,value)
				hDiskBookList[hOrder].GetXaxis().SetBinLabel(lineNumber,runNumber)
				hDiskBookList[hOrder].GetYaxis().SetBinLabel(yBinOrder,str( h.GetXaxis().GetBinLabel(i+1))+":"+h.GetYaxis().GetBinLabel(j+1))
		hOrder += 1
	hOrder = 0
        for h in hWheelList:
                yBinOrder = 0
		for j in range(21):
			for i in range(12):
                                if  not h.GetXaxis().GetBinLabel(i+1) or not h.GetYaxis().GetBinLabel(j+1): continue
				value = h.GetBinContent(i+1,j+1)
				if value == 0: continue
                                yBinOrder += 1
                                hWheelBookList[hOrder].SetBinContent(lineNumber,yBinOrder,value)
				hWheelBookList[hOrder].GetXaxis().SetBinLabel(lineNumber,runNumber)
				hWheelBookList[hOrder].GetYaxis().SetBinLabel(yBinOrder,str( h.GetYaxis().GetBinLabel(j+1))+":"+h.GetXaxis().GetBinLabel(i+1))
                hOrder += 1
hBookList = [hRunVsDM1,hRunVsDM2,hRunVsDM3,hRunVsDP1,hRunVsDP2,hRunVsDP3,hRunVsWM1,hRunVsWM2,hRunVsW00,hRunVsWP1,hRunVsWP2]
for h in hBookList:
	listArray = []
	fileName = str(h.GetTitle())+".txt"
	f = open(fileName,"w")
	for rollOrder in range(1,h.GetYaxis().GetNbins()+1):
		rollArray = []
		nBad = 0
		for runOrder in range(1,h.GetXaxis().GetNbins()+1):
			if h.GetBinContent(runOrder,rollOrder)==6 or h.GetBinContent(runOrder,rollOrder)==5 : nBad += 1
		#rollArray.append(rollOrder)
		rollArray.append(h.GetYaxis().GetBinLabel(rollOrder))
		rollArray.append(nBad)
		listArray.append(rollArray)
	#for line in sorted(listArray, key=lambda word: -word[2]):
	for line in sorted(listArray, key=lambda word: -word[1]):
		for i in range(len(line)):
			toString = str(line[i])
			if i == len(line)-1:
				toString += "\n"
			else : toString += "    "
			f.write(toString)
	f.close()
c1 = TCanvas("c1","c1",500,500)
hRunVsDM1.Draw("colz")
c1.SaveAs("runNumber_vs_disk-1.png")
c2 = TCanvas("c2","c2",500,500)
hRunVsDM2.Draw("colz")
c2.SaveAs("runNumber_vs_disk-2.png")
c3 = TCanvas("c3","c3",500,500)
hRunVsDM3.Draw("colz")
c3.SaveAs("runNumber_vs_disk-3.png")
c4 = TCanvas("c4","c4",500,500)
hRunVsDP1.Draw("colz")
c4.SaveAs("runNumber_vs_disk1.png")
c5 = TCanvas("c5","c5",500,500)
hRunVsDP2.Draw("colz")
c5.SaveAs("runNumber_vs_disk2.png")
c6 = TCanvas("c6","c6",500,500)
hRunVsDP3.Draw("colz")
c6.SaveAs("runNumber_vs_disk3.png")
c7 = TCanvas("c7","c7",500,500)
hRunVsWM1.Draw("colz")
c7.SaveAs("runNumber_vs_wheel-1.png")
c8 = TCanvas("c8","c8",500,500)
hRunVsWM2.Draw("colz")
c8.SaveAs("runNumber_vs_wheel-2.png")
c9 = TCanvas("c9","c9",500,500)
hRunVsW00.Draw("colz")
c9.SaveAs("runNumber_vs_wheel 0.png")
c10 = TCanvas("c10","c10",500,500)
hRunVsWP1.Draw("colz")
c10.SaveAs("runNumber_vs_wheel 1.png")
c11 = TCanvas("c11","c11",500,500)
hRunVsWP2.Draw("colz")
c11.SaveAs("runNumber_vs_wheel 2.png")
