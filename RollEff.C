#include <stdio.h>
#include <TH1F.h>

using namespace std;

class Eff
{
  public:
    void FillEff(TH1F* h,int i, char str);
};
void Eff::FillEff(TH1F* h,int i, char str);
{
  
}
void RollEff()
{
  TFile* output = TFile::Open("result.root","RECREATE");
  int nTotal = 1; int nRegion = 3; int nRing = 6; int nStation = 4;
  int nSector = 12; int nLayer = 2; int nSubsector = 6; int nRoll = 3;
 
  char* rootFile = "/afs/cern.ch/user/j/jhgoh/public/RPC/20151019_RPCEffic/ntuple.root";
  TFile* ntuple = TFile::Open(rootFile);
  TTree* rpc = ntuple->Get("trackRPC/tree");

  TH1F* hEffVsTotal = new TH1F("hEffVsTotal","Efficiency vs. Total;Total;Efficiency",nTotal,0,1);
  TH1F* hEffVsRegion = new TH1F("hEffVsRegion","Efficiency vs. Region;Region;Efficiency",nRegion,-1,2);
  TH1F* hEffVsRing = new TH1F("hEffVsRing","Efficiency vs. Ring;Ring;Efficiency",nRing,-2,4);
  TH1F* hEffVsStation = new TH1F("hEffVsStation","Efficiency vs. Station;Station;Efficiency",nStation,1,5);
  TH1F* hEffVsSector = new TH1F("hEffVsSector","Efficiency vs. Sector;Sector;Efficiency",nSector,1,13);
  TH1F* hEffVsLayer = new TH1F("hEffVsLayer","Efficiency vs. Layer;Layer;Efficiency",nLayer,1,3);
  TH1F* hEffVsSubsector = new TH1F("hEffVsSubsector","Efficiency vs. Subsector;Subsector;Efficiency",nSubsector,1,7);
  TH1F* hEffVsRoll = new TH1F("hEffVsRoll","Efficiency vs. Roll;Roll;Efficiency",nRoll,1,4);
  Eff eff;
  eff.FillEff(hEffVsTotal,1,"1");
  //Eff(hEffVsTotal,1,"1");
}
