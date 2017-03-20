import os,sys


channels = ["EpMum", "EpEm", "MupMum", "MupEm" ,"EmMup", "EmEp", "MumMup", "MumEp", "EpMup", "EpEp", "MupMup", "MupEp", "EmMum", "EmEm", "MumMum", "MumEm"]

masses = [ "40", "50","60", "100", "200", "500", "1100", "1500"]

catversion="v8-0-6"

onlystatus=False

os.system("bash /cvmfs/cms.cern.ch/crab3/crab.sh ")
for channel in channels:
    for mass in masses:

        if onlystatus:
             os.system("crab status -d crab_MajoranaNeutrinoTo"+channel+"_Schannel_M-"+mass+"_"+catversion+"/")
             continue

        os.system("crab status -d crab_MajoranaNeutrinoTo"+channel+"_Schannel_M-"+mass+"_"+catversion+"/  >> jobstatus.log")
        

        jobfile = open("jobstatus.log","r")
        
        doresubmit=False
        for line in jobfile:
            if "FAILED" in line:

                doresubmit=True
        jobfile.close()

        os.system("rm jobstatus.log")
        if doresubmit:
            os.system("crab resubmit -d crab_MajoranaNeutrinoTo"+channel+"_Schannel_M-"+mass+"_"+catversion+"/")

        
