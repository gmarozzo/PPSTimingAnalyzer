
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
     "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/0bf04b74-d4bc-4f32-838d-57fd4798fb4f.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/10b74f7d-91d2-4c51-849c-6f10ec190b3f.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/113d9abe-bc1b-4720-a887-0956d60998da.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/12298117-f283-4e9e-906a-f625dce0070e.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/14aebcc5-15a1-42de-b658-7cb49ae0c6d7.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/186e74e7-fe8b-4c3f-8f2b-d3b95b7b13f4.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/197c4539-a6d4-452a-97f5-0c4ca8e96324.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/1d7027d1-9633-4df9-8938-b536a896b823.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/398b5481-3bc6-4187-96b6-d9267b426ebd.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/3bec21f4-5e44-4db5-887d-abd0ad639021.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/3c441ad3-f3f8-4dd9-9d83-3dc534dff3aa.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/435234e1-94bf-4fe7-a1ed-d32e7fbb837f.root",
      #"/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/4e926e7b-75ac-4358-bc08-2c3d38902042.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/4ecbf2bf-7ffe-43d8-bc11-cdf37e8c2e23.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/54eb1f0e-f532-4130-88f2-14d1b152d623.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/55ca6a46-7b3a-4e16-a246-ef2c075d845a.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/5a6a762c-2a91-4f1c-874a-eb04e5f27ce8.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/5e344577-ff42-464a-b066-8ffd0425e728.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/65712915-56aa-41c3-8a02-b43272643faa.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/66002e39-d103-4b1e-9b8d-f7b0d016817a.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/688fdb9f-7234-4ef5-9c16-99654a521c23.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/6a8aad05-5d42-406e-b70f-d94d7cf1a901.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/6d66e32b-9484-4932-a466-e17b2c613db9.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/6df3f139-0751-4adc-9ebd-f7d0bcf7085f.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/7101dfe2-c92f-493d-bb11-08ac3573c7ed.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/74dbfe4a-e24f-4f50-9434-89935404085a.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/75513c39-6990-4da6-8356-83eb681e2fa9.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/75f0a9b1-f1b7-4902-9045-dda638788af8.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/7addeb7e-efa2-4f01-8c92-b5b4ea73d901.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/80cad7df-8ff1-4aca-9f5e-174f327f8627.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/8a014983-2b8b-47eb-afc6-99b3940b2d13.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/8bf13561-6a1b-4dda-b000-b7afe66dc976.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/8ce8d46b-ba0c-4dfe-ae7e-58a0bd25b6c9.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/8e3d36a7-230a-4e68-a21f-4c497d0b40d1.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/9ffe490d-530e-4870-89d7-cc14168ed39c.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/a44ccf8e-da1f-4dee-b56a-4cb60bfb6586.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/a574242c-049e-4f91-bcc6-a92ecb256671.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/a8378340-7019-4aa9-9b02-c69aba94add7.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/a8a1ab70-9ab1-4695-9bdb-6c83676af97e.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/aac43424-8c4b-472f-80a8-2c301cb9a081.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/ab3f9b9d-1c22-4de4-9621-29fb6145ffe0.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/b6a1a9f1-5e14-40d7-8ce8-ad6c73dc256e.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/b6ae1e42-0b3e-4a15-822b-397cc41a73bb.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/b81a5d94-d6bd-4205-9c8b-839d6db4e914.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/b959c06a-4c43-4bd3-853d-931da0ddc48a.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/c2ae26a1-bf8a-4885-9ebc-6630aae6510c.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/c368672c-9989-41fc-a29d-71c792e1dd6e.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/ca4f0333-f997-4acd-b586-2c8947991d3c.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/cc6bab20-5cad-4de4-85d7-52a320898004.root",
      "/store/data/Run2023D/SpecialZeroBias0/AOD/19Jul2023-v1/2520000/ccaf3da8-5a37-4207-81ff-6e8305293660.root"                            
                        )
)

process.source.bypassVersionCheck = cms.untracked.bool(True)


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
#process.CondDB.connect = 'sqlite_file:../../../CTPPSTimeCalibration/ppsDiamondTiming_calibration369956.sqlite' # SQLite input
#process.PoolDBESSource = cms.ESSource('PoolDBESSource',
#        process.CondDB,
#        DumpStats = cms.untracked.bool(True),
#        toGet = cms.VPSet(
#            cms.PSet(
#                record = cms.string('PPSTimingCalibrationRcd'),
#                tag = cms.string('DiamondTimingCalibration')
#        )
#    )
#)


# JH - rerun reco sequence with new timing conditions                                                                                          
process.load("RecoPPS.Configuration.recoCTPPS_cff")
#process.ctppsDiamondRecHits.timingCalibrationTag=cms.string("GlobalTag:PPSTestCalibration")

#process.ctppsDiamondRecHits.timingCalibrationTag = ("")

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
    outfilename = cms.untracked.string( "output_ZeroBias2.root" )
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
