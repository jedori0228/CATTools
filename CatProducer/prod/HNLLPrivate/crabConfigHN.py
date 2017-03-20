from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import  getUsernameFromSiteDB

config = Configuration()

config.section_("General")
config.General.requestName = ''
config.General.transferLogs    = False
config.General.transferOutputs = True

config.section_("JobType")
config.JobType.pluginName  = 'Analysis'
config.JobType.psetName    = 'PAT2CAT_cfg.py'

config.section_("Data")
config.Data.publication  = False
#################################################################
# ALLOWS NON VALID DATASETS
config.Data.allowNonValidInputDataset = True

config.section_("Site")
# Where the output files will be transmitted to
#config.Site.storageSite = 'T2_KR_KNU'
#crab checkwrite --site=T3_KR_KISTI --lfn=/store/group/CAT/
config.Site.storageSite = 'T3_KR_KISTI'
config.Data.inputDataset = ''
config.Data.inputDBS = 'phys03'
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.splitting='FileBased'
config.Data.unitsPerJob=1
config.JobType.pyCfgParams = ['runOnMC=True','useMiniAOD=True','globalTag=','runGenTop=False']

