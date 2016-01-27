void median()
{
  TH1F* hRandom = new TH1F("hRandom","test",100,-5,5);
  for ( int i=0; i<=1000; ++i) {
    hRandom->FillRandom("gaus");
  }

  double* integral = hRandom->GetIntegral();
  for ( int i=0; i<hRandom->GetNbinsX(); ++i) {
    //cout << *integral << endl;
    cout << i << "  " << integral[i] << endl;
  }
  hRandom->Draw();
}
