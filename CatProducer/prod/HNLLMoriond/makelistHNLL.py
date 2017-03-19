import os,sys

channels = ["EpMup", "EpEp", "MupMup", "MupEp", "EmMum", "EmEm", "MumMum", "MumEm"]

masses = [ "50", "100", "200", "500", "1100"]

catversion="v8-0-6"

xsec_m = [4.292, 0.01581, 6.435E-04, 1.618E-05, 4.357E-07]
xsec_p = [5.921, 0.02299, 0.001055, 3.304E-05, 1.123E-06]

os.system("bash /cvmfs/cms.cern.ch/crab3/crab.sh ")
for channel in channels:
    for m in range(0, len(masses)):
        mass = masses[m]
        xsec = xsec_p[m]
        if "um" in channel:
            xsec = xsec_m[m]
        tag=""
        os.system("ls -lth  /xrootd/store/user/jalmond/MajoranaNeutrinoTo"+channel+"_Schannel_M-"+mass+"_TuneCUETP8M1_13TeV-amcatnlo/crab_MajoranaNeutrinoTo"+channel+"_Schannel_M-"+mass+"_TuneCUETP8M1_13TeV_"+catversion+"/>> log1.txt" )
        readlog1 = open("log1.txt","r")
        for line in readlog1:
            if "bestman" in line:
                sline = line.split()
                if len(sline) == 9:
                    tag=sline[8]
        readlog1.close()

        
        os.system("ls -lth  /xrootd/store/user/jalmond/MajoranaNeutrinoTo"+channel+"_Schannel_M-"+mass+"_TuneCUETP8M1_13TeV-amcatnlo/crab_MajoranaNeutrinoTo"+channel+"_Schannel_M-"+mass+"_TuneCUETP8M1_13TeV_"+catversion+"/"+tag + "/ > log1b.txt")

        readlog1b = open("log1b.txt","r")
        nlines=0
        for line in readlog1b:
            sline = line.split()
            if len(sline) == 9:
                nlines=nlines+1
        readlog1b.close()
                
        if nlines > 1:
            sys.exit()

        os.system("ls -lth   /xrootd/store/user/jalmond/MajoranaNeutrinoTo"+channel+"_Schannel_M-"+mass+"_TuneCUETP8M1_13TeV-amcatnlo/crab_MajoranaNeutrinoTo"+channel+"_Schannel_M-"+mass+"_TuneCUETP8M1_13TeV_"+catversion+"/"+tag   + "/0000/ > log2.txt")
        os.system("ls -lth   /xrootd/store/user/jalmond/MajoranaNeutrinoTo"+channel+"_Schannel_M-"+mass+"_TuneCUETP8M1_13TeV-amcatnlo/crab_MajoranaNeutrinoTo"+channel+"_Schannel_M-"+mass+"_TuneCUETP8M1_13TeV_"+catversion+"/"+tag   + "/0000/")
        readlog2 = open("log2.txt","r")
        listfile = open("/cms/scratch/SNU/datasets_"+catversion+"/dataset_HNMoriondLL"+channel+"_"+mass+".txt","w")
        listfile.write("# DataSetName = HNMajoranaNeutrinoTo"+channel+"_Schannel_M-"+mass+"\n")
        listfile.write("# xsec = "+str(xsec)+"\n")
        listfile.write("# catversion = " + catversion + "\n")
        listfile.write("# name = HNMoriondLL"+channel+"_"+mass +  "\n")
        for line in readlog2:
            if "bestman" in line:
                sline =line.split()
                if len(sline) == 9:
                    filename=sline[8]
                    listfile.write("root://cms-xrdr.sdfarm.kr:1094///xrd/store/user/jalmond/MajoranaNeutrinoTo"+channel+"_Schannel_M-"+mass+"_TuneCUETP8M1_13TeV-amcatnlo/crab_MajoranaNeutrinoTo"+channel+"_Schannel_M-"+mass+"_TuneCUETP8M1_13TeV_"+catversion+"/"+tag   + "/0000/"+filename+"\n")

        readlog2.close()
        listfile.close()
        os.system("rm log1.txt")
        os.system("rm log2.txt")
