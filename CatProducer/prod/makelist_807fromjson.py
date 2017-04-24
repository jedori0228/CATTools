import os,sys

datasetname = [ 
    ["DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8" , ""]
    ]

catversion="v8-0-7"
readfromcatversion="v8-0-6"
newfilename=""
user=os.getenv("USER")
user="jskim"

os.system("bash /cvmfs/cms.cern.ch/crab3/crab.sh ")


for m in range(0, len(datasetname)):
    print "--"*50
    print datasetname[m]
    pdataset = datasetname[m][0]
    prodtag= datasetname[m][1]
    if prodtag == "":
        print "WARNING no prodtag  set. Will use first in list"
    
    if os.path.exists("list.txt"):
        os.system("rm list.txt")
    
    print "grep " + pdataset + " /cms/scratch/SNU/datasets_"+readfromcatversion+"/*.txt | grep catTuple_1.root > list.txt"
    os.system("grep " + pdataset + " /cms/scratch/SNU/datasets_"+readfromcatversion+"/*.txt | grep catTuple_1.root > list.txt")
    
    readlist= open("list.txt","r")
    fornewfile=[]
    for r in readlist:
        r=r.replace(":", " ")
        sr = r.split()
        oldfile= sr[0]
        print "reading from " + oldfile

        if not os.path.exists(oldfile):
            sys.exit()

        readoldfile = open(oldfile,"r")
        newfilename = oldfile.replace(readfromcatversion,catversion)
        for ro in readoldfile:
            if not ".root" in ro:
                fornewfile.append(ro)
                print (ro.split())

    os.system("ls -lth  /xrootd/store/user/"+user+"/"+pdataset+ "  > log1.txt" )

    readlog1 = open("log1.txt","r")
    MiniAODCampaign=""
    for line in readlog1:
        if "bestman" in line:
            sline = line.split()
            if len(sline) == 9:
                MiniAODCampaign=sline[8]
    readlog1.close()
    print "MiniAODCampaign = " + MiniAODCampaign
    
    if prodtag == "":
         os.system("ls -lth  /xrootd/store/user/"+user+"/"+pdataset + "/"+MiniAODCampaign + "/ >  log1b.txt")  
         readlog1b = open("log1b.txt","r")
         for line in readlog1b:
             sline = line.split()
             if len(sline) == 9:
                 prodtag = sline[8]
         readlog1b.close()
         os.system("rm log1b.txt")
         print "prodtag = " + prodtag
    os.system("ls -lth  /xrootd/store/user/"+user+"/"+pdataset + "/"+MiniAODCampaign + "/" + prodtag + " > log1b.txt")
    
    readlog1b = open("log1b.txt","r")
    nlists=[]
    for line in readlog1b:
        sline = line.split()
        if len(sline) == 9:
            nlists.append(sline[8])
            
    readlog1b.close()
    os.system("rm log1b.txt")
    
               
    for l in nlists:
        if os.path.exists("log2.txt"):
            os.system("rm log2.txt")

        os.system("ls -lth  /xrootd/store/user/"+user+"/"+pdataset + "/" +MiniAODCampaign   + "/" + prodtag + "/"+l+"/ > log2.txt")

        readlog2 = open("log2.txt","r")
        listfile = open(newfilename,"w")
        for coline in fornewfile:
            if "path " in coline:
                listfile.write("# path =  /xrootd/store/user/"+user+"/"+pdataset + "/"+MiniAODCampaign + "/" + prodtag + "\n" )
            else:
                listfile.write(coline)
            
        for line in readlog2:
            if "bestman" in line:
                sline =line.split()
                if len(sline) == 9:
                    filename=sline[8]
                    listfile.write("root://cms-xrdr.sdfarm.kr:1094///xrd/store/user/"+user+"//"+pdataset + "/"+ MiniAODCampaign + "/" + prodtag + "/"+ l + " /"+filename+"\n") 
        readlog2.close()
        listfile.close()
        os.system("rm log2.txt")
        os.system("chmod 777 " + newfilename)
    os.system("rm log1.txt")

    print "--"*50
    print "File --> " + newfilename
    print "--"*50
