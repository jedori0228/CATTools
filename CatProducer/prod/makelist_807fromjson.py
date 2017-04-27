import os,sys

from cattuplelist_ja import *



datasetname = list

for l in datasetname:
    print l



catversion="v8-0-7"
readfromcatversion="v8-0-6"
newfilename=""
users=[ os.getenv("USER") , "jskim","shjeon"]

os.system("bash /cvmfs/cms.cern.ch/crab3/crab.sh ")

listtag='Add to Setup.py : mcsampledir = ['

xsec_list=[]
missing_samples=[]
for m in range(0, len(datasetname)):
    print "--"*50
    print datasetname[m]
    pdataset = datasetname[m][0]
    prodtag= datasetname[m][1]
    ssample=datasetname[m][2]
    
    sxsec = datasetname[m][3]
    if prodtag == "":
        print "WARNING no prodtag  set. Will use first in list"
    
    if os.path.exists("list.txt"):
        os.system("rm list.txt")
    
    
    filefound=False
    nfile=0
    while not filefound:
        nfile=nfile+1
        print "grep " + pdataset + " /cms/scratch/SNU/datasets_"+readfromcatversion+"/*.txt | grep catTuple_"+str(nfile)+".root > list.txt"
        os.system("grep " + pdataset + " /cms/scratch/SNU/datasets_"+readfromcatversion+"/*.txt | grep catTuple_"+str(nfile)+".root > list.txt")
         
   
        readlist= open("list.txt","r")
        fornewfile=[]
        for r in readlist:
            if not ssample+".txt" in r: 
                for x in range(0,10):
                    print "#########"*10
                    print "file found in wrong list"
                    print r
                for x in range(0,10):
                    print "#########"*10
                continue
            
            if ".root" in r:
                filefound=True
            r=r.replace(":", " ")
            sr = r.split()
            oldfile= sr[0]
            print "reading from " + oldfile
            
            if not os.path.exists(oldfile):
                sys.exit()

            subname= oldfile.replace(".txt","")
            subname = subname.replace("/cms/scratch/SNU/datasets_v8-0-6/dataset_","")

            if m == 0:
                listtag+='"'+subname+'"'
            else:
                listtag+=',"'+subname+'"'
                               

            readoldfile = open(oldfile,"r")
            newfilename = oldfile.replace(readfromcatversion,catversion)
            for ro in readoldfile:
                if not ".root" in ro:
                    fornewfile.append(ro)
                    print (ro.split())
        readlist.close()


    user_sample=""

    sample_imissing=False
    for it_user in range(0, len(users)):
        if not os.path.exists( "/xrootd/store/user/"+users[it_user]+"/"+pdataset):
            continue
        user_sample=users[it_user]
        break


    if user_sample == "":
        missing_samples.append(pdataset)
        continue

    os.system("ls -lth  /xrootd/store/user/"+user_sample+"/"+pdataset+ "  > log1.txt" )

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
         os.system("ls -lth  /xrootd/store/user/"+user_sample+"/"+pdataset + "/"+MiniAODCampaign + "/ >  log1b.txt")  
         readlog1b = open("log1b.txt","r")
         for line in readlog1b:
             sline = line.split()
             if len(sline) == 9:
                 prodtag = sline[8]
         readlog1b.close()
         os.system("rm log1b.txt")
         print "prodtag = " + prodtag
    if not os.path.exists( "/xrootd/store/user/"+user_sample+"/"+pdataset + "/"+MiniAODCampaign + "/"+prodtag):
        print "prodtag = " + prodtag + " is wrong"
        sys.exit()

    os.system("ls -lth  /xrootd/store/user/"+user_sample+"/"+pdataset + "/"+MiniAODCampaign + "/" + prodtag + " > log1b.txt")
    
    readlog1b = open("log1b.txt","r")
    nlists=[]
    for line in readlog1b:
        sline = line.split()
        if len(sline) == 9:
            nlists.append(sline[8])
            
    readlog1b.close()
    os.system("rm log1b.txt")
    
    print newfilename

    for l in nlists:
        print "Adding  /xrootd/store/user/"+user_sample+"/"+pdataset + "/" +MiniAODCampaign   + "/" + prodtag + "/"+l

    filelist=[]
    for l in nlists:
        if os.path.exists("log2.txt"):
            os.system("rm log2.txt")

        os.system("ls -lth  /xrootd/store/user/"+user_sample+"/"+pdataset + "/" +MiniAODCampaign   + "/" + prodtag + "/"+l+"/ > log2.txt")

        readlog2 = open("log2.txt","r")
            
        for line in readlog2:
            if "bestman" in line:
                sline =line.split()
                if len(sline) == 9:
                    filename=sline[8]
                    filelist.append("root://cms-xrdr.sdfarm.kr:1094///xrd/store/user/"+user_sample+"//"+pdataset + "/"+ MiniAODCampaign + "/" + prodtag + "/"+ l + "/"+filename+"\n") 

        readlog2.close()

        os.system("rm log2.txt")

    
    listfile = open(newfilename,"w")
    for coline in fornewfile:
        if "path " in coline:
            listfile.write("# path =  /xrootd/store/user/"+user_sample+"/"+pdataset + "/"+MiniAODCampaign + "/" + prodtag + "\n" )
        elif "catversion " in coline:
            listfile.write("# catversion =  v8-0-7\n")
        else:
            if "xsec" in coline:
                scoline = coline.split()
                xsec= scoline[3]
                if float(xsec) != float(sxsec):
                    print "XSEC " + str(sxsec) + " is diffent to what is in 806 : " + str(xsec)
                    xsec_list.append([sxsec,xsec,pdataset])
            listfile.write(coline)
    for fileline in filelist:
        listfile.write(fileline)
    listfile.close()
    os.system("chmod 777 " + newfilename)
    os.system("rm log1.txt")

    print "--"*50
    print "File --> " + newfilename
    print "--"*50

print "--"*50
print "--"*50
print listtag+"]"


print "--"*50
print "--"*50

for m in  missing_samples:
    print m + " is missing"


for x in range(0, len(xsec_list)):
    print str(xsec_list[x][2]) + "  " + str(xsec_list[x][0]) +  " : " + str(xsec_list[x][1])
    
