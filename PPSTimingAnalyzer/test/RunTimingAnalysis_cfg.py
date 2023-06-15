
import FWCore.ParameterSet.Config as cms
import copy

process = cms.Process('PPSTiming2')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = ''
process.MessageLogger.cerr.FwkReport.reportEvery = 1000


process.source = cms.Source ("PoolSource",
                             fileNames = cms.untracked.vstring(
                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_11.root',
                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_12.root',
                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_13.root',
                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_14.root',
                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_16.root',
                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_17.root',
                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_18.root',
                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_19.root',
                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_1.root',        
                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_2.root',
                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_21.root',
                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_22.root',
                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_23.root',
                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_25.root',
                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_26.root',
                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_27.root',
                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_28.root',
                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_29.root',
                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_3.root',
                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_30.root',
                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_32.root',
                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_33.root',
                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_34.root',
                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_35.root',
                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_36.root'
                        )
)


#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
#from Configuration.AlCa.GlobalTag import GlobalTag
#from Configuration.StandardSequences.FrontierConditions_GlobalTag_cff import GlobalTag
#process.GlobalTag.globaltag = '124X_dataRun3_Prompt_frozen_v4'
#process.GlobalTag.toGet = cms.VPSet()

# JH: recipe from C. Misan to pick up new timing calibrations                                                                                  
#process.GlobalTag.toGet=cms.VPSet(
#  cms.PSet(record = cms.string("PPSTimingCalibrationRcd"),
#           tag = cms.string("PPSDiamondTimingCalibration_Run3_recovered_v1"),
#           label = cms.untracked.string('PPSTestCalibration'),
#           connect = cms.string("frontier://FrontierPrep/CMS_CONDITIONS")
#          )
#)

# Copied from https://github.com/cms-sw/cmssw/blob/master/CalibPPS/TimingCalibration/test/DiamondCalibrationWorker_cfg.py#L23-34
# Attempting to pickup new time-walk calibrations from sqlite file. Not sure if this really works...

process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
from Configuration.AlCa.autoCond import autoCond
process.GlobalTag = GlobalTag(process.GlobalTag, autoCond['run3_data_prompt'], '')
#process.GlobalTag.globaltag = '126X_dataRun3_v2'
process.load("EventFilter.CTPPSRawToDigi.ctppsRawToDigi_cff")
process.load("RecoPPS.Configuration.recoCTPPS_cff")

process.load('CondCore.CondDB.CondDB_cfi')
process.CondDB.connect = 'sqlite_file:../../../CTPPSTimeCalibration/ppsALL.sqlite' # SQLite input
process.PoolDBESSource = cms.ESSource('PoolDBESSource',
        process.CondDB,
        DumpStats = cms.untracked.bool(True),
        toGet = cms.VPSet(
            cms.PSet(
                record = cms.string('PPSTimingCalibrationRcd'),
                tag = cms.string('DiamondTimingCalibration')
        )
    )
)


# JH - rerun reco sequence with new timing conditions                                                                                          
process.load("RecoPPS.Configuration.recoCTPPS_cff")
#process.ctppsDiamondRecHits.timingCalibrationTag=cms.string("GlobalTag:PPSTestCalibration")

process.ctppsDiamondRecHits.timingCalibrationTag = ("")

process.ctppsDiamondLocalTracks.recHitsTag = cms.InputTag("ctppsDiamondRecHits","","PPSTiming2")
process.ctppsLocalTrackLiteProducer.tagDiamondTrack = cms.InputTag("ctppsDiamondLocalTracks","","PPSTiming2")
process.ctppsProtons.tagLocalTrackLite = cms.InputTag("ctppsLocalTrackLiteProducer","","PPSTiming2")
process.ctppsLocalTrackLiteProducer.includeDiamonds = cms.bool(True)
process.ctppsLocalTrackLiteProducer.includePixels = cms.bool(True)


process.mydiamonds = cms.EDAnalyzer(
    'PPSTimingAnalyzer',
    #    lhcInfoLabel = cms.string(''),
    verticesTag = cms.InputTag('offlinePrimaryVertices'),
    tracksTag = cms.InputTag('generalTracks'),
    #
    # Take PPS information from the existing Prompt RECO AOD
    #
    #    tagDiamondRecHits = cms.InputTag("ctppsDiamondRecHits"),
    #    tagTrackLites = cms.InputTag( "ctppsLocalTrackLiteProducer"),
    #    ppsRecoProtonSingleRPTag = cms.InputTag("ctppsProtons", "singleRP"),
    #    ppsRecoProtonMultiRPTag = cms.InputTag("ctppsProtons", "multiRP"),
    #    #
    # Alternatively, uncomment these lines to take PPS information from on-the-fly re-RECO
    #
    tagDiamondRecHits = cms.InputTag("ctppsDiamondRecHits","","PPSTiming2"),                                               
    tagTrackLites = cms.InputTag( "ctppsLocalTrackLiteProducer", "", "PPSTiming2"), 
    ppsRecoProtonSingleRPTag = cms.InputTag("ctppsProtons", "singleRP", "PPSTiming2"),
    ppsRecoProtonMultiRPTag = cms.InputTag("ctppsProtons", "multiRP", "PPSTiming2"),
    maxVertices = cms.uint32(1),
    outfilename = cms.untracked.string( "output_ZeroBias.root" )
)

#process.ctppsDiamondRecHits.timingCalibrationTag = cms.string("")

# Trigger                                                                                                                  
from HLTrigger.HLTfilters.hltHighLevel_cfi import *
process.hltFilter = copy.deepcopy(hltHighLevel)
process.hltFilter.TriggerResultsTag = cms.InputTag("TriggerResults","","HLT")
process.hltFilter.HLTPaths = ['HLT_EphemeralZeroBias_*']

process.ALL = cms.Path(
    process.hltFilter * 
    # Uncomment these lines, to re-run the PPS local+proton timing reconstruction starting from AOD
    process.ctppsDiamondRecHits *
    process.ctppsDiamondLocalTracks *
    process.ctppsPixelLocalTracks * 
    process.ctppsLocalTrackLiteProducer *
    process.ctppsProtons *
    process.mydiamonds 
                       )

process.schedule = cms.Schedule(process.ALL)

#print(process.dumpPython())
