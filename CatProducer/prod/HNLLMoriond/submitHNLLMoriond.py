import os,sys


catversion="v8-0-6"

channels = ["EpMup", "EpEp", "MupMup", "MupEp", "EmMum", "EmEm", "MumMum", "MumEm"]

masses = [ "50", "100", "200", "500", "1100"]


os.system("bash /cvmfs/cms.cern.ch/crab3/crab.sh ")

notallsubmitted=True
while notallsubmitted:
    for channel in channels:
        for mass in masses:

            if os.path.exists("crab_MajoranaNeutrinoTo"+channel+"_Schannel_M-"+mass+"_TuneCUETP8M1_13TeV_"+catversion+"//.requestcache"):
                continue
            if os.path.exists("crab_MajoranaNeutrinoTo"+channel+"_Schannel_M-"+mass+"_TuneCUETP8M1_13TeV_"+catversion+"/"):
                os.system("rm -rf crab_MajoranaNeutrinoTo"+channel+"_Schannel_M-"+mass+"_TuneCUETP8M1_13TeV_"+catversion+"/")

            print "Making file crabConfig_official_moriod17HNLL_"+channel+"_"+mass+".py"
            if not os.path.exists("crabConfig_official_moriod17HNLL_"+channel+"_"+mass+".py"):
                crabHNfile = open("crabConfig_official_moriod17HNLL_"+channel+"_"+mass+".py","w")

                read_file_def = open("crabConfigOfficialHN.py","r")
                for line in read_file_def:
                    if "config.General.requestName" in line:
                        crabHNfile.write("config.General.requestName = 'MajoranaNeutrinoTo"+channel+"_Schannel_M-"+mass+"_TuneCUETP8M1_13TeV_"+catversion+"'\n")
                    elif "config.Data.inputDatase" in line:
                        crabHNfile.write("config.Data.inputDataset = '/MajoranaNeutrinoTo"+channel+"_Schannel_M-"+mass+"_TuneCUETP8M1_13TeV-amcatnlo/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'\n")
                    else:
                        crabHNfile.write(line+"\n")
                read_file_def.close()
                crabHNfile.close()
                
            os.system("crab submit -c crabConfig_official_moriod17HNLL_"+channel+"_"+mass+".py")

    notallsubmitted=False
    for channel in channels:
        for mass in masses:      
            if not os.path.exists("crab_MajoranaNeutrinoTo"+channel+"_Schannel_M-"+mass+"_TuneCUETP8M1_13TeV_"+catversion+"//.requestcache"):
                notallsubmitted=True
