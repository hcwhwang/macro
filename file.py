#!/usr/bin/python
from operator import itemgetter
import os, sys
from urllib import urlopen
import csv
gdocurl = "https://docs.google.com/spreadsheets/d/1rWM3AlFKO8IJVaeoQkWZYWwSvicQ1QCXYSzH74QyZqE"
#gid = 519625370 #v7.4.5
gid = 1038794205 #v7.4.4
setCsv = "/pub?gid=%i&single=true&output=csv" % gid
path = "."
csvList = list(csv.reader(urlopen(gdocurl+setCsv).readlines()))

nameIndex = csvList[0].index("Name")
pathIndex = csvList[0].index("Path")

samplePathList = []

nameList = []
nameList.append("DoubleMuon_Run2015D")
nameList.append("DoubleEG_Run2015D")
nameList.append("MuonEG_Run2015D")
nameList.append("DYJets")
nameList.append("TTJets_aMC")
nameList.append("WJets")
nameList.append("ZZ")
nameList.append("TTJets_aMC")
nameList.append("TTJets_MG5")
nameList.append("TT_powheg")
for l in csvList[1:]:
  if l[nameIndex] in nameList:
    samplePathList.append("/xrd"+l[pathIndex]+"/0000")

#savePath = "."
savePath = "./744"
#savePath = "./745"
for i,path in enumerate(samplePathList):
  commandList = "xrd cms-xrdr.sdfarm.kr ls " + path + "> file.txt"
  os.system(commandList)
  rootFileList = open("file.txt","r")
  list = []
  for line in rootFileList:
    sampleLsBeforeSort = line.split()
    if len(sampleLsBeforeSort)!=0: list.append(sampleLsBeforeSort)
  list.sort(key=lambda size: len(size[1]))
  sampleFullName = list[-1][4]
  commandCopy = "xrdcp root://cms-xrdr.sdfarm.kr:1094//" + sampleFullName + " %s" % savePath
  os.system(commandCopy)
  sampleName = sampleFullName.split("/")[-1]
  os.system("cd %s" % savePath)
  commandNaming = "mv -f %s catTuple_%s.root" % (sampleName, nameList[i])
  os.system(commandNaming)
  os.system("cd")
  os.system("rm -f file.txt")
