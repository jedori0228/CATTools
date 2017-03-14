import FWCore.ParameterSet.Config as cms
import os

process = cms.Process("Ana")

process.load("FWCore.MessageLogger.MessageLogger_cfi")
#process.load("Configuration.StandardSequences.Services_cff")
#process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")

process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.MessageLogger.cerr.FwkReport.reportEvery = 10000

process.source = cms.Source("PoolSource",
fileNames = cms.untracked.vstring(

"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_1.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_10.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_100.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_101.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_102.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_103.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_104.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_105.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_106.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_107.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_108.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_109.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_11.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_110.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_111.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_112.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_113.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_114.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_115.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_116.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_117.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_118.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_119.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_12.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_120.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_121.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_122.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_123.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_124.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_125.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_126.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_127.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_128.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_129.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_13.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_130.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_131.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_132.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_133.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_134.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_135.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_136.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_137.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_138.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_139.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_14.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_140.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_141.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_142.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_143.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_144.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_145.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_146.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_147.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_148.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_149.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_15.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_150.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_151.root",
"root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/DoubleMuon/v8-0-4_Run2016B-23Sep2016-v3/170113_133450/0000/catTuple_152.root",
      )
)


process.load("CATTools.CatAnalyzer.filters_cff")

process.nEventsTotal = cms.EDProducer("EventCountProducer")
process.ntuple = cms.EDAnalyzer("GenericNtupleMakerSNU",
    failureMode = cms.untracked.string("keep"), # choose one among keep/skip/error
    eventCounters = cms.vstring("nEventsTotal"), #"nEventsTotal", "nEventsClean", "nEventsPAT"),
    genjet = cms.InputTag("slimmedGenJets"),
    genLabel      = cms.InputTag("prunedGenParticles"),
    triggerBits = cms.InputTag("TriggerResults::HLT"),
    triggerBits2 = cms.InputTag("TriggerResults::HLT2"),
    triggerObjects = cms.InputTag("catTrigger"),
    muons = cms.InputTag("catMuons"),
    electrons = cms.InputTag("catElectrons"),
    jets = cms.InputTag("catJets"),     
    fatjets = cms.InputTag("catFatJets"),     
    vertices = cms.InputTag("catVertex"),
    met = cms.InputTag("catMETs"),
    runFullTrig = cms.bool(False),
    keepAllGen= cms.bool(False),                      
    makeSlim= cms.bool(True),
                                genWeightLabel = cms.InputTag("genWeight"),
    pdfweights = cms.InputTag("flatGenWeights","pdf"),
    scaleupweights = cms.InputTag("flatGenWeights","scaleup"),
    scaledownweights = cms.InputTag("flatGenWeights","scaledown"),

    metFilterBitsPAT = cms.InputTag("TriggerResults","","PAT"),                                                                                 
    metFilterBitsRECO = cms.InputTag("TriggerResults","","RECO"),                                                                                
    metFilterNames = cms.vstring(
        "HBHENoiseFilter",
         "HBHENoiseIsoFilter",
         "EcalDeadCellTriggerPrimitiveFilter",
         "CSCTightHaloFilter",
         "eeBadScFilter",
         "globalTightHalo2016Filter",
         "goodVertices",
         ),

    allweights= cms.bool(False),                                
                                # Fill direct from Cattuple                                
                                
    int = cms.PSet(
        nGoodPV           =  cms.InputTag("catVertex"   , "nGoodPV"),
        nPV               =  cms.InputTag("catVertex"   , "nPV"    ),
        nTrueInteraction  =  cms.InputTag("pileupWeight", "nTrueInteraction" ),
    ),
    bool  = cms.PSet(
        BadChargedCandidateFilter =  cms.InputTag("BadChargedCandidateFilter"),
        BadPFMuonFilter =  cms.InputTag("BadPFMuonFilter"),
),
    float = cms.PSet( ),

    floats = cms.PSet( ),


    cands_bool = cms.PSet(
        photons = cms.PSet(
            src = cms.InputTag("catPhotons"),
            exprs = cms.untracked.PSet(
                #photonID_loose   = cms.string("photonID('cutBasedPhotonID-Spring15-25ns-V1-standalone-loose')"),
                #photonID_medium  = cms.string("photonID('cutBasedPhotonID-Spring15-25ns-V1-standalone-medium')"),
                #photonID_tight   = cms.string("photonID('cutBasedPhotonID-Spring15-25ns-V1-standalone-tight')"),
                #photonID_mva     = cms.string("photonID('mvaPhoID-Spring15-25ns-nonTrig-V2-wp90')"),
                mcMatched = cms.string("mcMatched"),
                haspixseed = cms.string("HasPixelSeed"),
                passelectronveto = cms.string("PassElectronVeto"),
                ),
            selections = cms.untracked.PSet(),
            ),

        ),
                                
   cands_int = cms.PSet(
        ),
                    
    cands = cms.PSet(

     photons = cms.PSet(
            src = cms.InputTag("catPhotons"),
            exprs = cms.untracked.PSet(
                 pt  = cms.string("pt"),
                 eta = cms.string("eta"),
                 phi = cms.string("phi"),
                 energy   = cms.string("energy"),
                 chargedHadronIso = cms.string("chargedHadronIso"),
                 puChargedHadronIso  = cms.string("puChargedHadronIso"),
                 neutralHadronIso  = cms.string("neutralHadronIso"),
                 photonIso = cms.string("photonIso"),
                 rhoIso = cms.string("rhoIso"),
                 #chargedHadronIsoWithEA = cms.string("chargedHadronIsoWithEA"),
                 #neutralHadronIsoWithEA  = cms.string("neutralHadronIsoWithEA"),
                 #photonIsoWithEA = cms.string("photonIsoWithEA"),
                 sigmaietaieta = cms.string("SigmaiEtaiEta"),
                 r9 = cms.string("r9"),
                 hovere = cms.string("HoverE"),
                 sceta = cms.string("SCEta"),
                 scphi = cms.string("SCPhi"),
                 scrawenergy = cms.string("SCRawEnergy"),
                 scpreshowerenergy = cms.string("SCPreShowerEnergy"),
                 ),
            selections = cms.untracked.PSet(),
        ),

        met = cms.PSet(
            src = cms.InputTag("catMETs"),
            exprs = cms.untracked.PSet(
                pt  = cms.string("pt"),
                phi = cms.string("phi"),
                sumet = cms.string("sumEt"),
                xyshift_px  = cms.string("XYShiftedPx"),
                xyshift_py  = cms.string("XYShiftedPy"),
                xyshift_sumet =  cms.string("XYShiftedsumEt"),
                unclusteredEn_Px_up = cms.string("unclusteredEnPx(1)"),
                unclusteredEn_Py_up = cms.string("unclusteredEnPy(1)"),
                unclusteredEn_SumEt_up = cms.string("unclusteredEnSumEt(1)"),
                unclusteredEn_Phi_up = cms.string("unclusteredEnPhi(1)"),
                unclusteredEn_Px_down = cms.string("unclusteredEnPx(-1)"),
                unclusteredEn_Py_down = cms.string("unclusteredEnPy(-1)"),
                unclusteredEn_SumEt_down = cms.string("unclusteredEnSumEt(-1)"),
                unclusteredEn_Phi_down = cms.string("unclusteredEnPhi(-1)"),
 
                jetEn_Px_up  = cms.string("JetEnPx(1)"),
                jetEn_Py_up  = cms.string("JetEnPy(1)"),
                jetEn_SumEt_up  = cms.string("JetEnSumEt(1)"),
                jetEn_Px_down  = cms.string("JetEnPx(-1)"),
                jetEn_Py_down  = cms.string("JetEnPy(-1)"),
                jetEn_SumEt_down  = cms.string("JetEnSumEt(-1)"),
                jetRes_Px_up  = cms.string("JetResPx(1)"),
                jetRes_Py_up  = cms.string("JetResPy(1)"),
                jetRes_SumEt_up  = cms.string("JetResSumEt(1)"),
                jetRes_Px_down  = cms.string("JetResPx(-1)"),
                jetRes_Py_down  = cms.string("JetResPy(-1)"),
                jetRes_SumEt_down  = cms.string("JetResSumEt(-1)"),
                ),
            selections = cms.untracked.PSet(),
        ),
     ),
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string("ntuple.root"),
)

#process.load("CATTools.CatProducer.pseudoTop_cff")
process.p = cms.Path(
    process.nEventsTotal*
    process.ntuple
)

