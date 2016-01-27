import sys, os

cmd = "curl -L --cert /tmp/x509up_u57424 --key /tmp/x509up_u57424 -k https://cmsweb.cern.ch/dqm/offline/data/browse/ROOT/OfflineData/Run2012/SingleMu/000%sxx/DQM_V0001_R000%s__SingleMu__Run2012D-22Jan2013-v1__DQM.root -O"

inputFile = sys.argv[1]

list = open(inputFile)
numberOfGoodrun = 0
for line in list:
	if line[0] != '|': continue
	word = [x.strip() for x in line.strip().split("|")]
	#if len(word) < 12 : continue

	runNum = word[1][:6]
	if word[-2].upper() in ('GOOD', 'LONG', 'GOOD/LONG'):
	#if word[-2] == 'good' or word[-2] == 'Good' or word[-2] == 'GOOD' or word[-2] == 'Good/long' or word[-2] == 'Good/Long' or word[-2] == 'Long':
		numberOfGoodrun += 1
		prefix = runNum[:4]
		print (cmd % (prefix, runNum))	
	if word[-1] == 'Run' and word[-2] == 'Good/Long':
		numberOfGoodrun += 1
		prefix = runNum[:4]
		print (cmd % (prefix, runNum))	
		
