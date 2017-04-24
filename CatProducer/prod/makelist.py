import os,sys

datasetname = [ 
    ["/DYToEE_NNPDF30_13TeV-powheg-pythia8/RunIISummer16MiniAODv2-EGM0_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "DYtoEE", 1997.0],
    ["/WZG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "WZG",                           0.04123],
    ["/WWG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "WWG",                       0.2147], 
    ["/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1/MINIAODSIM", "ttZToLL_M-10", 0.2529],
    ["/GluGluHToWWTo2L2Nu_M125_13TeV_powheg_JHUgen_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "ggHtoWW",            43.92],
    ["/VBFHToWWTo2L2Nu_M125_13TeV_powheg_JHUgen_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "vbfHtoWW",              3.748],
    ["/QCD_Pt_15to20_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "qcd_15to20_bctoe",1272980000*0.0002],
    ["/QCD_Pt_20to30_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "qcd_20to30_bctoe",557627000*0.00059],
    ["/QCD_Pt_30to80_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "qcd_30to80_bctoe",159068000*0.00255],
    ["/QCD_Pt_80to170_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "qcd_80to170_bctoe",3221000*0.01183],
    ["/QCD_Pt_170to250_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "qcd_170to250_bctoe",105771*0.02492],
    ["/QCD_Pt_250toInf_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "qcd_250toinf_bctoe",21094.1*0.03375],
    ["/WW_DoubleScattering_13TeV-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM", "ww_ds",1.61704],
    ["/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "ggHtoZZ",0.01181],
    ["/TGJets_TuneCUETP8M1_13TeV_amcatnlo_madspin_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "TG",2.967],
    ["/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "TTG",3.697],
    ["/tZq_ll_4f_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM", "tZq",0.0758],
    ["/VBF_HToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"              , "vbhHtoZZ",0.001034],
    
    
    #     1.1 brings pp->ZZ from NLO to NNLO (http://arxiv.org/abs/1405.2219)
    #     1.7 brings gg->ZZ from LO to NLO (http://arxiv.org/abs/1509.06734)
    #         (since it is gg it is already kind of NLO though so it is more like "nlo" to "nnlo")
    
    ["/ZZTo2L2Nu_13TeV_powheg_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "ZZTo2L2Nu_Powheg",0.564],
    ["/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "ZZTo2L2Q_Powheg",3.22],
    ["/GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "ggZZto2e2mu",0.003194 ],
    #### Need to find xsec for Z->ll Z->nunu ggZ samples
    ["/GluGluToContinToZZTo2e2nu_13TeV_MCFM701_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "ggZZto2e2nu", 0.01899 ],
    ["/GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "ggZZto2e2tau",0.003194 ],
    ["/GluGluToContinToZZTo2mu2nu_13TeV_MCFM701_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "ggZZto2mu2nu",0.01899 ],
    ["/GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "ggZZto2mu2tau",0.003194 ],
    ["/GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "ggZZto4e",0.001586 ],
    ["/GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "ggZZto4mu",0.001586 ],
    ["/GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "ggZZto4tau",0.001586 ],
    ["/GluGluWWTo2L2Nu_MCFM_13TeV/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "ggWWto2L2Nu",0.84365],
    ["/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "WZto2L2Q_amcatnlo",5.595],
    ["/QCD_Pt-30to40_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "QCD_DoubleEMEnriched_30-40_mgg80toinf",108000000*0.000225],
    ["/QCD_Pt-30toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "QCD_DoubleEMEnriched_30-inf_mgg40to80",162060000*0.0016],
    ["/QCD_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "QCD_DoubleEMEnriched_40-inf_mgg80toinf",54120000*0.002],
    ["/ZZTo4L_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "ZZTo4L_amcatnlo" , 1.212]
    ]

catversion="v8-0-6"


os.system("bash /cvmfs/cms.cern.ch/crab3/crab.sh ")


for m in range(0, len(datasetname)):

    print datasetname[m]
    dataset = datasetname[m][0]

    tmpdataset = dataset.replace("/"," ")
    tmpdataset=tmpdataset.split()
    
    pdataset = tmpdataset[0]
    ixsec = datasetname[m][2]
    name = datasetname[m][1]
    tag=""
    os.system("ls -lth  /xrootd/store/user/jalmond/"+pdataset + "/crab_"+pdataset + "_"+catversion+"/>> log1.txt" )

    readlog1 = open("log1.txt","r")
    for line in readlog1:
        if "bestman" in line:
            sline = line.split()
            if len(sline) == 9:
                tag=sline[8]
    readlog1.close()
    
        
    os.system("ls -lth  /xrootd/store/user/jalmond/"+pdataset + "/crab_"+pdataset + "_"+catversion+"/"+tag + "/ > log1b.txt")
    
    readlog1b = open("log1b.txt","r")
    nlines=0
    for line in readlog1b:
        sline = line.split()
        if len(sline) == 9:
            nlines=nlines+1
    readlog1b.close()
               
    if nlines > 1:
        sys.exit()
        
    os.system("ls -lth  /xrootd/store/user/jalmond/"+pdataset + "/crab_"+pdataset + "_"+catversion+"/"+tag + "/0000/ > log2.txt")
    os.system("ls -lth  /xrootd/store/user/jalmond/"+pdataset + "/crab_"+pdataset + "_"+catversion+"/"+tag + "/0000/")

    readlog2 = open("log2.txt","r")
    listfile = open("/cms/scratch/SNU/datasets_"+catversion+"/dataset_"+ name + ".txt","w")
    listfile.write("# DataSetName = " + dataset + "\n") 
    listfile.write("# xsec = "+str(ixsec)+"\n")
    listfile.write("# catversion = " + catversion + "\n")
    listfile.write("# name = " + name +  "\n")   
    for line in readlog2:
        if "bestman" in line:
            sline =line.split()
            if len(sline) == 9:
                filename=sline[8]
                
                listfile.write("root://cms-xrdr.sdfarm.kr:1094///xrd/store/user/jalmond//"+pdataset + "/crab_"+pdataset + "_"+catversion+"/"+tag + "/0000/"+filename+"\n") 

    readlog2.close()
    listfile.close()
    os.system("rm log1.txt")
    os.system("rm log2.txt")
