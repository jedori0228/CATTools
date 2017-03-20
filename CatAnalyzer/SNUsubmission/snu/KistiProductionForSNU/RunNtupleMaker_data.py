#!/usr/bin/python

import os, getpass, sys
import time
from functions import *
from Setup import *
import string


def CheckJobStatusAfterCrash(dirname, v):
    
    print "CheckJobStatusAfterCrash:"
    if not os.path.exists(dirname):
        return
    
    if os.path.exists(dirname + "/check_list_data.txt"):
        os.system("rm " + dirname +"/check_list_data.txt")

    os.system("ls " + dirname + "/* > " + dirname+ "/check_list_data.txt")
    logfile = open( dirname+"/check_list_data.txt", "r")
    njobs_x=0
    for i in logfile:
        if "_cfg.py" in i:
            njobs_x = njobs_x +1
    
    print "number of jobs =  " + str(njobs_x)
    os.system("rm " + dirname+"/check_list_data.txt")

    if os.path.exists(dirname+"/check_finished_data.txt"):
        os.system("rm " + dirname +"/check_finished_data.txt")
    os.system("grep FINISHED " + dirname + "/*.log > " + dirname +"/check_finished_data.txt")
    nfinishedjobs=0
    for j in range(0, njobs_x):
        jobcheck= "job_" + str(j) +".log"
        checkfile = open(dirname+"/check_finished_data.txt", "r")
        for line in checkfile:
            if jobcheck in line:
                nfinishedjobs=nfinishedjobs+1
    print "Number of finished jobs = " + str(nfinishedjobs)
    os.system("rm " + dirname +"/check_finished_data.txt")
    
    if nfinishedjobs != njobs_x:
        "Job is running already. Adding to list"
        return True
    else: 
        print "Removing dir since no jobs are running"
        return True
        os.system("rm -rf " + dirname)
         
    
        
    return False







def CheckJobStatus(submitted_list, v):

    mod_list =string.replace(submitted_list,"!", " ")
    split_list = mod_list.split()
    for x in split_list:
        print x


    new_submitted_list=submitted_list  
    print "Checking submitted jobs:"
    for i in split_list:
        period_list =string.replace(i,"_", " ")
        period_split_list = period_list.split()
        
        
        print period_split_list[0]
        print period_split_list[1]

        if os.path.exists("SNU_" + v+ "_" +i +"/check_list_data.txt"):
            os.system("rm SNU_" + v+ "_" +i +"/check_list_data.txt")

        os.system("ls SNU_" + v + "_" + i +"/* >  SNU_" + v+ "_" +i +"/check_list_data.txt")

        logfile = open( "SNU_" + v+ "_" +i +"/check_list_data.txt", "r")
        njobs_x=0
        for j in logfile:
            if "_cfg.py" in j:
                njobs_x = njobs_x +1
        print "number of jobs =  " + str(njobs_x)
        os.system("rm SNU_" + v+ "_" +i +"/check_list_data.txt")

        if os.path.exists("SNU_" + v+ "_" +i +"/check_finished_data.txt"):
            os.system("rm SNU_" + v+ "_" +i +"/check_finished_data.txt")

        os.system("grep FINISHED " + "SNU_" + v+ "_" +i +"/*.log > SNU_" + v+ "_" +i +"/check_finished_data.txt")
        os.system("grep TERMINATED " + "SNU_" + v+ "_" +i +"/*.log > SNU_" + v+ "_" +i +"/check_finished2_data.txt")
        
        nfinishedjobs=0
        for k in range(0, njobs_x):
            jobcheck= "job_" + str(k) +".log"
            checkfile = open("SNU_" + v+ "_" +i +"/check_finished_data.txt", "r")
            for line in checkfile:
                if jobcheck in line:
                    nfinishedjobs=nfinishedjobs+1

        print "Number of finished jobs = " + str(nfinishedjobs)
        os.system("rm SNU_" + v+ "_" +i +"/check_finished_data.txt")


        FailedJobs=False
        failed_jobs=[]
        if int(nfinishedjobs) != int(njobs_x):
            for k in range(0, njobs_x):
                jobcheck2= "job_" + str(k) +".log"
                checkfile2 = open("SNU_" + v+ "_" +i +"/check_finished2_data.txt", "r")
                for line2 in checkfile2:
                    if jobcheck2 in line2:
                        failed_jobs.append(k)
                        FailedJobs=True
                        nfinishedjobs=nfinishedjobs+1
                        
        if FailedJobs == True:
            print "Quiting script cos a job failed"
            failedlist = open("faileddatasettmp_" + i + "_Run2016"+ period + ".txt", "w")
            for x in failed_jobs:
                failedlist.write(x+"\n")
            failedlist.close()
                           

        FailedAndFinished=False
        if (int(nfinishedjobs)+len(failed_jobs)) == int(njobs_x):
            FailedAndFinished=True

        #if FailedJobs == True and FailedAndFinished:
        if False:
            for j in failed_jobs:
                
                print "resubmitting job " + str(j) 
                
                os.system("grep  root://cms-xrdr.sdfarm.kr:1094 " + os.getenv("CMSSW_BASE") + "/src/CATTools/CatAnalyzer/SNUsubmission/snu/KistiProductionForSNU/" + "SNU_" + v+ "_" +i +"/job_"+str(j)+"_cfg.py >> failed_SNU_" + v+ "_" +i +".txt")

                datasetpath = "/cms/scratch/SNU/datasets_" +v + "/dataset_" + i + "_Run2016"+ period + ".txt"                                                                                                                                                              
                newlist = open("datasettmp_" + i + "_Run2016"+ period + ".txt", "w")
                read_input_list = open(datasetpath, "r")
                for inputline in read_input_list:
                    if "root:" in inputline:
                        break
                    newlist.write(read_input_list)
                read_input_list.close()    

                read_failed_list = open("failed_SNU_" + v+ "_" +i +".txt")
                               
                for fline in read_failed_list:
                    fline = fline.replace("fileNames = cms.untracked.vstring(","")
                    fline = fline.replace("'","")
                    fline = fline.replace(",","")
                    fline = fline.replace(")","")
                    sfline - fline.split()
                    newlist.write(sfline[0] + "\n")
                read_failed_list.close()    
                
                newlist.close()
                
                
                os.system("source " + path_failedjob + " " + str(j))
                #quit() 

  
        if int(nfinishedjobs) == int(njobs_x):
            print "Job " + i + " is finished. Copying to SNU"


            if copy_cluster:
       
                print "ssh " + username_snu  + "@147.47.242.67  mkdir /data4/DATA/FlatCatuples/Data/" + v + "/" + period_split_list[0]  
                os.system("ssh " +  username_snu +"@147.47.242.67 mkdir /data4/DATA/FlatCatuples/Data/" + str(v))
                os.system("ssh " + username_snu  + "@147.47.242.67 mkdir /data4/DATA/FlatCatuples/Data/" + str(v) +"/" + period_split_list[0])
                if period_split_list[1] == "H":
                    #os.system("ssh " + username_snu  + "@147.47.242.67 rm -r /data4/DATA/FlatCatuples/Data/" + str(v) +"/" + period_split_list[0] + "/period" + period_split_list[1]+"_"+period_split_list[2])
                    os.system("ssh " + username_snu  + "@147.47.242.67 mkdir /data4/DATA/FlatCatuples/Data/" + str(v) +"/" + period_split_list[0] + "/period" + period_split_list[1]+"_"+period_split_list[2])


                    print "scp SNU_" + v+ "_" +i +"/*.root " + " " + username_snu  + "@147.47.242.67:/data4/DATA/FlatCatuples/Data/"  + str(v) + "/"  +"/" + period_split_list[0] + "/period" + period_split_list[1]+"_"+period_split_list[2]
                    
                    os.system("scp SNU_" + v+ "_" +i +"/*.root " + " " + username_snu  + "@147.47.242.67:/data4/DATA/FlatCatuples/Data/"  + str(v) + "/"  +"/" + period_split_list[0] + "/period" + period_split_list[1]+"_"+period_split_list[2] )
                else:
                    #os.system("ssh " + username_snu  + "@147.47.242.67 rm -r /data4/DATA/FlatCatuples/Data/" + str(v) +"/" + period_split_list[0] + "/period" + period_split_list[1])
                    os.system("ssh " + username_snu  + "@147.47.242.67 mkdir /data4/DATA/FlatCatuples/Data/" + str(v) +"/" + period_split_list[0] + "/period" + period_split_list[1])

                    print "scp SNU_" + v+ "_" +i +"/*.root " + " " + username_snu  + "@147.47.242.67:/data4/DATA/FlatCatuples/Data/"  + str(v) + "/"  +"/" + period_split_list[0] + "/period" + period_split_list[1]
                    os.system("scp SNU_" + v+ "_" +i +"/*.root " + " " + username_snu  + "@147.47.242.67:/data4/DATA/FlatCatuples/Data/"  + str(v) + "/"  +"/" + period_split_list[0] + "/period" + period_split_list[1])
            if copy_cms1:   
                print "ssh " + username_snu  + "@147.47.242.42 mkdir /data2/DATA/cattoflat/Data/" + v + "/" + period_split_list[0]
                os.system("ssh " +  username_snu +"@147.47.242.42 mkdir /data2/DATA/cattoflat/Data/" + str(v))
                os.system("ssh " + username_snu  + "@147.47.242.42 mkdir /data2/DATA/cattoflat/Data/" + str(v) +"/" + period_split_list[0])

                if period_split_list[1] == "H":
                    #os.system("ssh " + username_snu  + "@147.47.242.42 rm -r /data2/DATA/cattoflat/Data/" + str(v) +"/" + period_split_list[0] + "/period" + period_split_list[1]+"_"+period_split_list[2])
                    os.system("ssh " + username_snu  + "@147.47.242.42 mkdir /data2/DATA/cattoflat/Data/" + str(v) +"/" + period_split_list[0] + "/period" + period_split_list[1]+"_"+period_split_list[2])
                    print "scp SNU_" + v+ "_" +i +"/*.root " + " " + username_snu  + "@147.47.242.42:/data2/DATA/cattoflat/Data/"  + str(v) + "/"  +"/" + period_split_list[0] + "/period" + period_split_list[1]+"_"+period_split_list[2]
                    
                    os.system("scp SNU_" + v+ "_" +i +"/*.root " + " " + username_snu  + "@147.47.242.42:/data2/DATA/cattoflat/Data/"  + str(v) + "/"  +"/" + period_split_list[0] + "/period" + period_split_list[1] +"_"+period_split_list[2])

                else:
                    #os.system("ssh " + username_snu  + "@147.47.242.42 rm -r /data2/DATA/cattoflat/Data/" + str(v) +"/" + period_split_list[0] + "/period" + period_split_list[1] )
                    os.system("ssh " + username_snu  + "@147.47.242.42 mkdir /data2/DATA/cattoflat/Data/" + str(v) +"/" + period_split_list[0] + "/period" + period_split_list[1] )
                    
                    print "scp SNU_" + v+ "_" +i +"/*.root " + " " + username_snu  + "@147.47.242.42:/data2/DATA/cattoflat/Data/"  + str(v) + "/"  +"/" + period_split_list[0] + "/period" + period_split_list[1]

                    os.system("scp SNU_" + v+ "_" +i +"/*.root " + " " + username_snu  + "@147.47.242.42:/data2/DATA/cattoflat/Data/"  + str(v) + "/"  +"/" + period_split_list[0] + "/period" + period_split_list[1] )

            print "submitted_list = " + submitted_list + " is set to: "
            new_submitted_list = string.replace(submitted_list, i+"!" , "")
            print new_submitted_list
            print "Deleting directory SNU_" + v+ "_" +i +"/"
            os.system("rm -r   SNU_" + v+ "_" +i +"/*.root")
            return new_submitted_list


    return new_submitted_list

if not os.path.exists(str(cmssw_dir)+"/src/CATTools/CatAnalyzer/SNUsubmission/snu/KistiProductionForSNU/jobcheck"):
    os.system("mkdir " + str(cmssw_dir)+"/src/CATTools/CatAnalyzer/SNUsubmission/snu/KistiProductionForSNU/jobcheck")

######## True runs default list of all samples available
ALLSamples= False
periods = []
if len(datasampledir) == 0:
    ALLSamples=True
    periods = ["B" , "C", "D", "E","F","G","H_v2","H_v3"]
else:
    periods = data_periods
    

if len(periods) ==0:
    print "Now data period was chosed to process. Fix this."
    quit()
####### make sure this file is being run at kisti                                                                                                                                                                                           
host=os.getenv("HOSTNAME")
if not "ui10" in host:
    quit()

if os.path.exists("cat.txt"):
    os.system("rm cat.txt")
os.system("source "+str(cmssw_dir)+"/src/CATTools/CommonTools/test/snu/catversion.sh > cat.txt")



catfile = open("cat.txt",'r')
vcat=""
for line in catfile:
    vcat = line    
    if vcat == "":
        print "version not set"
        quit()
    if not "v8-" in vcat:
        print "version does not have v8- in name " 
        quit()

print "Cat version = " + version 


if not k_user in kisti_output_default:
    print "kisti_output_default should container username in the path. Fix this."
    quit()

if not (os.path.exists(kisti_output_default)):
    os.system("mkdir " + kisti_output_default)
    if not (os.path.exists(kisti_output_default)):
        print "Problem making directory for kisti_output_default. Process is quitting. Before running again type"
        print "mkdir " + kisti_output_default
        quit()
else:
    os.system("rm -r " + kisti_output_default)
    os.system("mkdir " + kisti_output_default)

print "Output directory is " + kisti_output_default        

    

os.system("ls /tmp/ > check_snu_connection.txt")
snu_connect = open("check_snu_connection.txt",'r')
connected_cms3=False
for line in snu_connect:
    if "ssh-" +k_user +"@147.47.242.4" in line:
        connected_cms3=True
            
os.system("rm check_snu_connection.txt")    
if connected_cms3 == False:    
    print "No connection to cms3: please make connection in screen and run script again"
    quit()



## Make a list of samples to process

sampledir = ["DoubleMuon" , "MuonEG", "DoubleEG", "SingleElectron", "SingleMuon"]

periods = ["B", "C", "D","E","F","G","H_v2","H_v3"]

if not ALLSamples == True:
    sampledir = datasampledir


# njob set to 40: if n root files < 40 njobs = #rootfiles
njob=100
njobs_submitted=0
string_of_submitted=""
skip_first=0
samples_processed=0
dataset_tag=""
for i in sampledir:
    
    runtrig=False
    if "DoubleEG" in i:
        runtrig=True
        #runtrig true means more triggers are available in catuples              

    if "SingleEl" in i:
        runtrig=True
    
    for period in periods:
        print "period = " + period
        samples_processed=samples_processed+1
        if samples_processed < skip_first+1:
            continue

        njob=100
        output=i
        kisti_output=kisti_output_default+output+"/"
        print "Making dir: " + kisti_output

        if not (os.path.exists(kisti_output)):
            os.system("mkdir " + kisti_output)
        else:
            os.system("rm " + kisti_output + "/*")

        datasetpath = "/cms/scratch/SNU/datasets_" +version + "/dataset_" + i + "_Run2016"+ period + ".txt"

        datasetfile = open(datasetpath, 'r')
        for line in datasetfile:
            if "DataSetName" in line:
                splitline  = line.split()
                datasetname= splitline[3].replace("/"," ")
                split_datasetname = datasetname.split()
                dataset_tag =split_datasetname[0]
        datasetfile.close()
        samples_processed=samples_processed+1 
        if samples_processed < skip_first+1:
            continue


        ## Set the number of jobs and files per job                                                                                                            
        fr = open(datasetpath,'r')

        count=0
        nfilesperjob=0
        for line in fr:
            if ".root" in line:
                count+=1
        fr.close()

        if njob > count:
            njob=count

        for k in range(1,count+1):
            if not k%njob:
                nfilesperjob+=1
            
        if nfilesperjob > 20:
            nfilesperjob = 20
            njob=0
            for l in range(1,count+1):
                if not l%nfilesperjob:
                    njob+=1

            files_torun= nfilesperjob*njob
            remainder= count - files_torun
            if remainder != 0:
                njob = njob +1
        else:
            files_torun= nfilesperjob*njob
            remainder= count - files_torun
            extrajobs=0
            while remainder > 0:
                extrajobs=extrajobs+1
                remainder = remainder - nfilesperjob
            
            njob=njob + extrajobs   

        print "njob = " + str(njob) + " and nfilesperjob = " + str(nfilesperjob) + " : total number of files = " + str(count)
        
        print "Number of jobs to process is " + str(njob)

        print "Each job will process  " + str(nfilesperjob) + "/" + str(count) + " files"
    

        jobname = "SNU_" + version + "_" + i + "_" + period

        datasetlist= "dataset_" + i + "_Run2016" + period +".txt"
        cfgfile="run_ntupleMaker_snu_data_cfg.py"
        if runtrig == True:
            cfgfile="run_ntupleMaker_snu_data_fulltrig_cfg.py"


        isjobrunning=False
        print "Running : CheckJobStatusAfterCrash"
        isjobrunning = CheckJobStatusAfterCrash(jobname, version)

        if isjobrunning == True:
        
            print "CheckJobStatusAfterCrash = True"
            string_of_submitted= string_of_submitted +  i + "_" + period+ "!"
            continue

        print "CheckJobStatusAfterCrash = False"

        runcommand="create-batch  --jobName " + jobname + " --fileList  /cms/scratch/SNU/datasets_" +version + "/" + datasetlist +"  --maxFiles " + str(nfilesperjob) + "  --cfg ../" + cfgfile  + "   --queue batch6  --transferDest /xrootd/store/user/" + k_user + "/"
        
        print runcommand
        os.system(runcommand)
    
        string_of_submitted= string_of_submitted +  i + "_" + period+ "!"
    
        njobs_submitted= int(njobs_submitted)+int(njob)
    
        check_njob_submitted=0
        while check_njob_submitted == 0:
            import platform
        
            os.system("condor_q " + k_user + " &>  jobcheck/runningcheck_data.txt")
            fcheck = open("jobcheck/runningcheck_data.txt",'r')
            for line in fcheck:
                if "completed" in line:
                    if "removed" in line:
                        linesplit = line.split()
                        print linesplit[0]
                        njobs_submitted = int(linesplit[0])
            print "Number of subjobs submitted = " + str(njobs_submitted)
    
            if int(njobs_submitted) > 1000:
                print "nsubjobs > 1000" 
                print "waiting 1 minute before checking if #subjobs  < 1000. If this is true will submit more."
                time.sleep(60.)
                string_of_submitted=CheckJobStatus(string_of_submitted, version)

            if int(njobs_submitted) < 1000:
                print "Number of jobs < 1000. Will check if any jobs are finished"
                check_njob_submitted = 1
                string_of_submitted=CheckJobStatus(string_of_submitted, version)
        
    ###    check if jobs are complete: If true send to SNU and delete local dir 

print "All samples are submitted. Now checking if jobs are finished."            
FilesAllCopied=False
while FilesAllCopied == False:
    tmp_string_of_submitted = string_of_submitted
    string_of_submitted=CheckJobStatus(tmp_string_of_submitted, version)

    if string_of_submitted == "":
        FilesAllCopied = True
    else:
        time.sleep(60.)


        

