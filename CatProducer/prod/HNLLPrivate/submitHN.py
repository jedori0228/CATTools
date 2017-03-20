import os,sys


channels = ["EpMum", "EpEm", "MupMum", "MupEm" ,"EmMup", "EmEp", "MumMup", "MumEp", "EpMup", "EpEp", "MupMup", "MupEp", "EmMum", "EmEm", "MumMum", "MumEm"]

masses = [ "40", "50","60", "100", "200", "500", "1100", "1500"]

catversion="v8-0-6"

os.system("bash /cvmfs/cms.cern.ch/crab3/crab.sh ")


notallsubmitted=True
while notallsubmitted:
    for channel in channels:
        for mass in masses:

            if os.path.exists("crab_MajoranaNeutrinoTo"+channel+"_Schannel_M-"+mass+"_"+catversion+"//.requestcache"):
                continue
            if os.path.exists("crab_MajoranaNeutrinoTo"+channel+"_Schannel_M-"+mass+"_"+catversion+"/"):
                os.system("rm -rf crab_MajoranaNeutrinoTo"+channel+"_Schannel_M-"+mass+"_"+catversion+"/")

            crabHNfile = open("crabConfigHN_"+channel+"_"+mass+".py","w")

            read_file_def = open("crabConfigHN.py","r")
            for line in read_file_def:
                if "config.General.requestName" in line:
                    crabHNfile.write("config.General.requestName = 'MajoranaNeutrinoTo"+channel+"_Schannel_M-"+mass+"_"+catversion+"'\n")
                elif "config.Data.inputDatase" in line:
                    crabHNfile.write("config.Data.inputDataset = '/MajoranaNeutrinoTo"+channel+"_Schannel_M-"+mass+"/jalmond-CMSSW_8_0_21_MiniAOD-28028af67189b3de7224b79195bd0e1d/USER'\n")
                else:
                    crabHNfile.write(line+"\n")
            read_file_def.close()
            crabHNfile.close()
            os.system("crab submit -c crabConfigHN_"+channel+"_"+mass+".py")
    notallsubmitted=False
    for channel in channels:
        for mass in masses:      
            if not os.path.exists("crab_MajoranaNeutrinoTo"+channel+"_Schannel_M-"+mass+"_"+catversion+"//.requestcache"):
                notallsubmitted=True
                
