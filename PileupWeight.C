#include "TFile.h"
#include "TTree.h"

using namespace std;

void PileupWeight() {

  gStyle->SetOptStat(0);
  float puweight1;
  int nvertex1, nvertex2;
  int channel1, channel2;
  bool step1_1, step1_2;
  const char* input1 = "cattree_ttbb_MuonEG_2015D.root";
  const char* input2 = "cattree_ttbb_MuonEG_2015Dprompt.root";
  const char* input3 = "cattree_ttbb_DoubleEG_2015D.root";
  const char* input4 = "cattree_ttbb_DoubleEG_2015Dprompt.root";
  const char* input5 = "cattree_ttbb_DoubleMuon_2015D.root";
  const char* input6 = "cattree_ttbb_DoubleMuon_2015Dprompt.root";
  const char* input7 = "cattree_ttbb_DYJets.root";
  const char* input8 = "cattree_ttbb_TTJets_aMC.root";

  TFile* f1 = TFile::Open(input8);
  TTree* ttree1 = (TTree*)f1->Get("cattree/tree");

  ttree1->SetBranchAddress("puweight", &puweight1);
  ttree1->SetBranchAddress("nvertex", &nvertex1);
  ttree1->SetBranchAddress("step1", &step1_1);
  ttree1->SetBranchAddress("channel", &channel1);

  TCanvas* c = new TCanvas("c","c",500,500);
  //c->SetLogy();
  TH1F* hNPVwPU = new TH1F("hNPVwPU","nPV with PU;nPV;Events",50,0,50);
  TH1F* hNPVwoPU = new TH1F("hNPVwoPU","nPV without PU;nPV;Events",50,0,50);
  TH1F* hNPVRD = new TH1F("hNPVRD","nPV;nPV;Events",50,0,50);


  hNPVwPU->SetLineColor(kBlue);
  hNPVwPU->SetLineWidth(2);
  hNPVwoPU->SetLineColor(kRed);
  hNPVwoPU->SetLineWidth(2);
  hNPVRD->SetLineColor(kBlack);
  hNPVRD->SetMarkerStyle(kFullCircle);
  const int nEntry1 = ttree1->GetEntries();
  float puWTot = 0;
  for (int iEntry = 0; iEntry < nEntry1; ++iEntry) {
    ttree1->GetEntry(iEntry);
    //if (!step1_1) continue;
    //if (channel1!=1) continue;
    hNPVwPU->Fill(nvertex1,puweight1);
    hNPVwoPU->Fill(nvertex1);
    puWTot += puweight1;
  }
  cout << puWTot/hNPVwoPU->Integral() << endl;

  TFile* f2 = TFile::Open(input5);
  TTree* ttree2 = (TTree*)f2->Get("cattree/tree");

  ttree2->SetBranchAddress("nvertex", &nvertex2);
  ttree2->SetBranchAddress("step1", &step1_2);
  ttree2->SetBranchAddress("channel", &channel2);

  const int nEntry2 = ttree2->GetEntries();
  for (int iEntry = 0; iEntry < nEntry2; ++iEntry) {
    ttree2->GetEntry(iEntry);
    //if (!step1_2) continue;
    //if (channel2!=1) continue;
    hNPVRD->Fill(nvertex2);
  }
  //hNPVRD->DrawNormalized("e");
  //hNPVwPU->DrawNormalized("samehist");
  hNPVwPU->Draw("samehist");
  //hNPVwoPU->DrawNormalized("same");
  hNPVwoPU->Draw("same");
  
  TLegend *l = new TLegend(0.6, 0.65, 0.88, 0.85);
  l->AddEntry(hNPVRD,"Data");
  l->AddEntry(hNPVwPU,"MC with PU");
  l->AddEntry(hNPVwoPU,"MC w/o PU");
  l->Draw();
  cout << hNPVwPU->Integral() << "  " << hNPVwoPU->Integral() << endl;
}
