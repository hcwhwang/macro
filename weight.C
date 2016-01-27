void weight()
{
  TH1F* hRD = new TH1F("hRD","hRD",30,0,30);
  TH1F* hMC = new TH1F("hMC","hMC",30,0,30);
  TH1F* hBefore = new TH1F("hBefore","hBefore",30,0,30);
  TH1F* hAfter = new TH1F("hAfter","hAfter",30,0,30);

  TH1F* hWgt = new TH1F("hWgt","hWgt",30,0,30);
  hRD->SetMinimum(0); 
  hMC->SetMinimum(0); 
 
  hRD->SetLineColor(kRed);
  hMC->SetLineColor(kBlue);

  hBefore->SetLineColor(kBlue);
  hAfter->SetLineColor(kRed);

  TRandom* t = new TRandom(); 
  for(int i=0; i<50000; ++i) {
    int r = t->Poisson(15);
    hRD->Fill(r);
    hMC->Fill(r+2);
  }
  double wTot = 0;
  for(int i=0; i<=hRD->GetNbinsX();++i) {
    if (hMC->GetBinContent(i+1) != 0 ) {
      float w = hRD->GetBinContent(i+1)/hMC->GetBinContent(i+1);
      w = w*hMC->Integral()/hRD->Integral();
      hWgt->SetBinContent(i+1,w);
//      wTot += w*hMC->GetBinContent(i+1);
    }
  }
  for(int i=0; i<50000; ++i) {
    int r = t->Poisson(15);
    hBefore->Fill(r+2); 
    hAfter->Fill(r+2,hWgt->GetBinContent((r+2)+1));
  }
  for(int i=0; i<=hBefore->GetNbinsX();++i) {
    if (hBefore->GetBinContent(i+1) != 0 ) {
      wTot += hWgt->GetBinContent(i+1)*hMC->GetBinContent(i+1);
    }
  }
  cout << wTot << endl;
  TCanvas* c1 = new TCanvas("c1","c1",500,500);
  hRD->Draw();
  hMC->Draw("same");
  TCanvas* c2 = new TCanvas("c2","c2",500,500);
  hWgt->Draw();
  TCanvas* c3 = new TCanvas("c3","c3",500,500);
  hAfter->Draw();
  hBefore->Draw("same");
  hRD->Draw("same");
  cout << hBefore->Integral() << endl;
  cout << hAfter->Integral() << endl;
}
