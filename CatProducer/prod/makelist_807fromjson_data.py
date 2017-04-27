import os,sys

from cattuplelist_data import *



tmpdatasetname = list

datasets = ["DoubleMuon","DoubleEG","SingleElectron","SingleMuon","MuonEG"]
datasetname=[]
for l in datasets:
    for x in tmpdatasetname:
        datasetname.append([l,x[0],x[1]])


for x in datasetname:
    print x


catversion="v8-0-7"
readfromcatversion="v8-0-6"
newfilename=""
users=[ "jalmond"]

os.system("bash /cvmfs/cms.cern.ch/crab3/crab.sh ")

listtag='Add to Setup.py : mcsampledir = ['

xsec_list=[]
missing_samples=[]
for m in range(0, len(datasetname)):
    print "--"*50
    print datasetname[m]
    pdataset = datasetname[m][0]
    period = datasetname[m][1]
    prodtag= datasetname[m][2]
    


    if prodtag == "":
        print "WARNING no prodtag  set. Will use first in list"
    
    if os.path.exists("list.txt"):
        os.system("rm list.txt")
    
    
    file_old = open ("/cms/scratch/SNU/datasets_v8-0-6/dataset_DoubleEG_Run2016B.txt","r")
    fornewfile=[]
    for line in file_old:
        if ".root" in line:
            break
        fornewfile.append(line)

    os.system("ls -lth  /xrootd/store/user/jalmond/"+pdataset+"/"+prodtag+ "  > log1.txt" )

    timestamp=""
    readlog1 = open("log1.txt","r")
    for line in readlog1:
        sline = line.split()
        if len(sline) == 9:
            timestamp = sline[8]
    readlog1.close()
    os.system("rm log1.txt")
    print "prodtag = " + prodtag
    if not os.path.exists( "/xrootd/store/user/jalmond/"+pdataset+"/"+prodtag + "/"+timestamp + "/"):
        print "prodtag = " + prodtag + " is wrong"
        sys.exit()

    os.system("ls -lth  /xrootd/store/user/jalmond/"+pdataset+"/"+prodtag + "/"+timestamp + "/  > log1b.txt")
    
    readlog1b = open("log1b.txt","r")
    nlists=[]
    for line in readlog1b:
        sline = line.split()
        if len(sline) == 9:
            nlists.append(sline[8])
            
    readlog1b.close()
    os.system("rm log1b.txt")
    
    newfilename="/cms/scratch/SNU/datasets_"+catversion+"/dataset_"+pdataset+"_Run2016"+period+".txt"
    print newfilename

    for l in nlists:
        print "Adding  /xrootd/store/user/jalmond/"+pdataset+"/"+prodtag + "/" +timestamp   + "/" + l

    filelist=[]
    for l in nlists:
        if os.path.exists("log2.txt"):
            os.system("rm log2.txt")

        os.system("ls -lth  /xrootd/store/user/jalmond/"+pdataset+"/"+prodtag + "/" +timestamp   + "/"  +l+"/ > log2.txt")

        readlog2 = open("log2.txt","r")
            
        for line in readlog2:
            if "bestman" in line:
                sline =line.split()
                if len(sline) == 9:
                    filename=sline[8]
                    filelist.append("root://cms-xrdr.sdfarm.kr:1094///xrd/store/user/jalmond/"+pdataset + "/"+ prodtag + "/"+ timestamp + "/"+ l + "/"+filename+"\n") 

        readlog2.close()

        os.system("rm log2.txt")

    
    listfile = open(newfilename,"w")
    for coline in fornewfile:
        if "path " in coline:
            listfile.write("# path =  /xrootd/store/user/jalmond/"+pdataset+"/"+prodtag + "/"+timestamp + "/" + "\n" )
        else:
            listfile.write(coline)
    for fileline in filelist:
        listfile.write(fileline)
    listfile.close()
    os.system("chmod 777 " + newfilename)


    print "--"*50
    print "File --> " + newfilename
    print "--"*50

print "--"*50
print "--"*50
print listtag+"]"


print "--"*50
print "--"*50
