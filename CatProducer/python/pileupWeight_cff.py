import FWCore.ParameterSet.Config as cms
#from   FWCore.PythonUtilities.LumiList import LumiList
from   CATTools.CatProducer.pileupWeight.pileupWeightRunI_cff import pileupWeightMap as pileupWeightRunI
from   CATTools.CatProducer.pileupWeight.pileupWeight2015_cff import pileupWeightMap as pileupWeight2015
from   CATTools.CatProducer.pileupWeight.pileupWeight2016_cff import pileupWeightMap as pileupWeight2016
pileupWeightMap = {}
pileupWeightMap.update(pileupWeightRunI)
pileupWeightMap.update(pileupWeight2015)
pileupWeightMap.update(pileupWeight2016)

pileupWeight = cms.EDProducer("CATPileupWeightProducer",
    #weightingMethod = cms.string("NVertex"), # Simple bin-by-bin correction of nVertex distribution. Non standard
    weightingMethod = cms.string("Standard"), # The Standard method in the CMSSW
    #weightingMethod = cms.string("RedoWeight"), # this is to be used re-reweight on CATTuple
    pileupMC = cms.vdouble(),
    pileupRD = cms.vdouble(),
    pileupUp = cms.vdouble(),
    pileupDn = cms.vdouble(),
    simpleWeights = cms.vdouble(),
    #pileupInfo = cms.InputTag("addPileupInfo"), # For the AOD and MiniAODv1
    pileupInfo = cms.InputTag("slimmedAddPileupInfo"),
    vertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    nTrueIntr = cms.InputTag("pileupWeight", "nTrueInteraction", "CAT"),
    doPeriodWeights  = cms.bool(False),
    pileupRD_B = cms.vdouble(),
    pileupRD_C = cms.vdouble(),
    pileupRD_D = cms.vdouble(),
    pileupRD_E = cms.vdouble(),
    pileupRD_F = cms.vdouble(),
    pileupRD_G = cms.vdouble(),
    pileupRD_H = cms.vdouble(),
    #LuminositySectionsBlockRange = LumiList('LumiMask/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON.txt').getVLuminosityBlockRange()
)


