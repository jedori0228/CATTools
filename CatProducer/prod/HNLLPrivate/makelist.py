import os,sys


channels = ["EpMum", "EpEm", "MupMum", "MupEm" ,"EmMup", "EmEp", "MumMup", "MumEp", "EpMup", "EpEp", "MupMup", "MupEp", "EmMum", "EmEm", "MumMum", "MumEm"]

masses = [ "40", "50","60", "100", "200", "500", "1100", "1500"]

xsec_m = [6.103,4.292,2.415,0.01581,6.435E-04,1.618E-05,4.357E-07,7.980E-08]
xsec_p = [8.387,5.921,3.324, 0.02299, 0.001055, 3.304E-05, 1.123E-06, 2.228E-07]

catversion="v8-0-6"

os.system("bash /cvmfs/cms.cern.ch/crab3/crab.sh ")
for channel in channels:
    for m in range(0, len(masses)):
        mass = masses[m]
        xsec = xsec_p[m]
        if "um" in channel:
            xsec = xsec_m[m]
            
        tag=""
        os.system("ls -lth  /xrootd/store/user/jalmond/MajoranaNeutrinoTo"+channel+"_Schannel_M-"+mass+"/crab_MajoranaNeutrinoTo"+channel+"_Schannel_M-"+mass+"_"+ catversion+"/ >> log1.txt" )
        readlog1 = open("log1.txt","r")
        for line in readlog1:
            if "bestman" in line:
                sline = line.split()
                if len(sline) == 9:
                    tag=sline[8]
        readlog1.close()

        
        os.system("ls -lth  /xrootd/store/user/jalmond/MajoranaNeutrinoTo"+channel+"_Schannel_M-"+mass+"/crab_MajoranaNeutrinoTo"+channel+"_Schannel_M-"+mass+"_"+ catversion+"/"+tag + "/ > log1b.txt")
        readlog1b = open("log1b.txt","r")
        nlines=0
        for line in readlog1b:
            sline = line.split()
            if len(sline) == 9:
                nlines=nlines+1
        readlog1b.close()
                
        if nlines > 1:
            sys.exit()

        os.system("ls -lth  /xrootd/store/user/jalmond/MajoranaNeutrinoTo"+channel+"_Schannel_M-"+mass+"/crab_MajoranaNeutrinoTo"+channel+"_Schannel_M-"+mass+"_"+ catversion+"/"+tag + "/0000/ > log2.txt")
        os.system("ls -lth  /xrootd/store/user/jalmond/MajoranaNeutrinoTo"+channel+"_Schannel_M-"+mass+"/crab_MajoranaNeutrinoTo"+channel+"_Schannel_M-"+mass+"_"+ catversion+"/"+tag + "/0000/")
        readlog2 = open("log2.txt","r")
        listfile = open("/cms/scratch/SNU/datasets_"+catversion+"/dataset_HN"+channel+"_"+mass+".txt","w")
        listfile.write("# DataSetName = MajoranaNeutrinoTo"+channel+"_Schannel_M-"+mass+"\n")
        listfile.write("# xsec = "+str(xsec)+"\n")
        listfile.write("# catversion = " + catversion + "\n")
        listfile.write("# name = HN"+channel+"_"+mass +  "\n")
        for line in readlog2:
            if "bestman" in line:
                sline =line.split()
                if len(sline) == 9:
                    filename=sline[8]
                    listfile.write("root://cms-xrdr.sdfarm.kr:1094///xrd/store/user/jalmond/MajoranaNeutrinoTo"+channel+"_Schannel_M-"+mass+"/crab_MajoranaNeutrinoTo"+channel+"_Schannel_M-"+mass+"_"+ catversion+"/"+tag + "/0000/"+filename+"\n")
        readlog2.close()
        listfile.close()
        os.system("rm log1.txt")
        os.system("rm log2.txt")
