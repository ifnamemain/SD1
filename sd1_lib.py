import os;
from ctypes import *
from math import pow, log, ceil

import numpy as np
from sd_constants import constants as const
from keysightSD1 import *

class sd1_lib(object):
    
    def __init__(self):
        self._sd_wave = SD_Wave()
        self._sd_module = SD_Module()
        self._sd_aou = SD_AOU()
        self._sd_dio = SD_DIO()
    
    def newFromFile(self, waveform_file):
        return self._sd_wave.newFromFile(waveform_file)
    
    def newFromArrayDouble(self, waveformType, waveformDataA, waveformDataB = None):
        return self._sd_wave.newFromArrayDouble(waveformType, waveformDataA, waveformDataB)
    
    def newFromArrayInteger(self, waveformType, waveformDataA, waveformDataB = None):
        return self._sd_wave.newFromArrayInteger(waveformType, waveformDataA, waveformDataB)
    
    def getWaveStatus(self):
        return self._sd_wave.getStatus()
    
    def getWaveType(self):
        return self._sd_wave.getType()
    
    def openWithSerialNumber(self, partNumber, serialNumber):
        return self._sd_module.openWithSerialNumber(partNumber, serialNumber)
    
    def openWithSerialNumberCompatibility(self, partNumber, serialNumber, compatibility):
        return self._sd_module.openWithSerialNumberCompatibility(partNumber, serialNumber, compatibility)
    
    def openWithSlot(self, partNumber, nChassis, nSlot):
        return self._sd_module.openWithSlot(partNumber, nChassis, nSlot)
    
    def openWithSlotCompatibility(self, partNumber, nChassis, nSlot, compatibility):
        return self._sd_module.openWithSlotCompatibility(partNumber, nChassis, nSlot, compatibility)
    
    def close(self):
        return self._sd_module.close()
    
    def isOpen(self):
        return self._sd_module.isOpen()
    
    def getType(self):
        return self._sd_module.getType()
    
    def moduleCount(self):
        return self._sd_module.moduleCount()
    
    def getProductNameBySlot(self, chassis, slot):
        return self._sd_module.getProductName(chassis, slot)
    
    def getProductNameByIndex(cls, index):
        return self._sd_module.getProductNameByIndex(index)
    
    def getSerialNumberBySlot(cls, chassis, slot) :
        return self._sd_module.getSerialNumberBySlot(chassis, slot)
    
    def getSerialNumberByIndex(cls, index) :
        return self._sd_module.getSerialNumberByIndex(index)
    
    def getTypeBySlot(cls, chassis, slot) :
        return self._sd_module.getTypeBySlot(chassis, slot)
    
    def getTypeByIndex(cls, index) :
        return self._sd_module.getTypeByIndex(index)
    
    def getChassisByIndex(cls, index) :
        return self._sd_module.getChassisByIndex(index)
    
    def getSlotByIndex(cls, index) :
        return self._sd_module.getSlotByIndex(index)
    
    def getStatus(self) :
        return self._sd_module.getStatus()
    
    def runSelfTest(self) :
        return self._sd_module.runSelfTest()
    
    def getSerialNumber(self) :
        return self._sd_module.getSerialNumber()
    
    def getProductName(self) :
        return self._sd_module.getProductName()
    
    def getFirmwareVersion(self) :
        return self._sd_module.getFirmwareVersion()
    
    def getHardwareVersion(self) :
        return self._sd_module.getHardwareVersion()
    
    def getChassis(self) :
        return self._sd_module.getChassis()
    
    def getSlot(self) :
        return self._sd_module.getSlot()
    
    ##HVI Registers
    def readRegisterByNumber(self, varNumber) :
        return self._sd_module.readRegisterByNumber(varNumber)
    
    def readRegisterByName(self, varName) :
        return self._sd_module.readRegisterByName(varName)
    
    def readRegisterDoubleByNumber(self, varNumber, unit) :
        return self._sd_module.readRegisterDoubleByNumber(varNumber, unit)
    
    def readRegisterDoubleByName(self, varName, unit) :
        return self._sd_module.readRegisterDoubleByName(varName, unit)
    
    def writeRegisterByNumber(self, varNumber, varValue) :
        return self._sd_module.writeRegisterByNumber(varNumber, varValue)
    
    def writeRegisterByName(self, varName, varValue) :
        return self._sd_module.writeRegisterByName(varName, varValue)
    
    def writeRegisterDoubleByNumber(self, varNumber, value, unit) :
        return self._sd_module.writeRegisterDoubleByNumber(varNumber, value, unit)
    
    def writeRegisterDoubleByName(self, varName, value, unit) :
        return self._sd_module.writeRegisterDoubleByName(varName, value, unit)
    
    ## PXItrigger
    def PXItriggerWrite(self, trigger, value) :
        return self._sd_module.PXItriggerWrite(trigger, value)
    
    def PXItriggerRead(self, trigger) :
        return self._sd_module.PXItriggerRead(trigger)
    
    ## External Trigger Lines
    def translateTriggerPXItoExternalTriggerLine(self, trigger) :
        return self._sd_module.translateTriggerPXItoExternalTriggerLine(trigger)
    
    def translateTriggerIOtoExternalTriggerLine(self, trigger) :
        return self._sd_module.translateTriggerIOtoExternalTriggerLine(trigger)
    
    ## FPGA
    def FPGAreadPCport(self, port, nDW, address, addressMode, accessMode) :
        return self._sd_module.FPGAreadPCport(port, nDW, address, addressMode, accessMode)
    
    def FPGAwritePCport(self, port, buffer, address, addressMode, accessMode) :
        return self._sd_module.FPGAwritePCport(port, buffer, address, addressMode, accessMode)
    
    def FPGAload(self, fileName) :
        return self._sd_module.FPGAload(fileName)
    
    def FPGAreset(self, mode) :
        return self._sd_module.FPGAreset(mode)
    
    def openHVI(self, fileHVI) :
        return self._sd_module.openHVI(fileHVI)
    
    def compileHVI(self) :
        return self._sd_module.compileHVI()
    
    def compilationErrorMessageHVI(self, errorIndex) :
        return self._sd_module.compilationErrorMessageHVI(errorIndex)
    
    def loadHVI(self) :
        return self._sd_module.loadHVI()
    
    ##HVI Control
    def startHVI(self) :
        return self._sd_module.startHVI()
    
    def pauseHVI(self) :
        return self._sd_module.pauseHVI()
    
    def resumeHVI(self) :
        return self._sd_module.resumeHVI()
    
    def stopHVI(self) :
        return self._sd_module.stopHVI()
    
    def resetHVI(self) :
        return self._sd_module.resetHVI()
    
    #AUO Functions
    def clockGetFrequency(self) :
        return self._sd_aou.clockGetFrequency()
    
    def clockGetSyncFrequency(self) :
        return self._sd_aou.clockGetSyncFrequency()
    
    def clockSetFrequency(self, frequency, mode = 1) :
        return self._sd_aou.clockSetFrequency(frequency, mode = 1)
    
    def clockResetPhase(self, triggerBehavior, triggerSource, skew = 0.0):
        return self._sd_aou.clockResetPhase(triggerBehavior, triggerSource, skew = 0.0)
    
    def channelAmplitude(self, nChannel, amplitude):
        return self._sd_aou.channelAmplitude(nChannel, amplitude)
    
    def channelOffset(self, nChannel, offset) :
        return self._sd_aou.channelOffset(nChannel, offset)
    
    def channelWaveShape(self, nChannel, waveShape) :
        return self._sd_aou.channelWaveShape(nChannel, waveShape)
    
    def channelFrequency(self, nChannel, frequency) :
        return self._sd_aou.channelFrequency(nChannel, frequency)
    
    def channelPhase(self, nChannel, phase) :
        return self._sd_aou.channelPhase(nChannel, phase)
    
    def channelPhaseReset(self, nChannel) :
        return self._sd_aou.channelPhaseReset(nChannel)
    
    def channelPhaseResetMultiple(self, channelMask) :
        return self._sd_aou.channelPhaseResetMultiple(channelMask) 
    
    def modulationAngleConfig(self, nChannel, modulationType, deviationGain) :
        return self._sd_aou.modulationAngleConfig(nChannel, modulationType, deviationGain)
    
    def modulationAmplitudeConfig(self, nChannel, modulationType, deviationGain) :
        return self._sd_aou.modulationAmplitudeConfig(nChannel, modulationType, deviationGain)
    
    def modulationIQconfig(self, nChannel, enable) :
        return self._sd_aou.modulationIQconfig(nChannel, enable)
    
    def clockIOconfig(self, clockConfig) :
        return self._sd_aou.clockIOconfig(clockConfig)
    
    def triggerIOconfigV5(self, direction, syncMode = 1) :
        return self._sd_aou.triggerIOconfigV5(direction, syncMode) 
    
    def triggerIOconfig(self, direction) :
        return self._sd_aou.triggerIOconfig(direction)
    
    def triggerIOwrite(self, value, syncMode = 1) :
        return self._sd_aou.triggerIOwrite(value, syncMode)
    
    def triggerIOread(self) :
        return self._sd_aou.triggerIOread()
    
    def waveformReLoad(self, waveformObject, waveformNumber, paddingMode = 0) :
        return self._sd_aou.waveformReLoad(waveformObject, waveformNumber, paddingMode)
    
    def waveformReLoadArrayInt16(self, waveformType, dataRaw, waveformNumber, paddingMode = 0) :
        return self._sd_aou.waveformReLoadArrayInt16(waveformType, dataRaw, waveformNumber, paddingMode)
    
    def waveformLoad(self, waveformObject, waveformNumber, paddingMode = 0) :
        return self._sd_aou.waveformLoad(waveformObject, waveformNumber, paddingMode)
    
    def waveformLoadInt16(self, waveformType, dataRaw, waveformNumber, paddingMode = 0) :
        return self._sd_aou.waveformLoadInt16(waveformType, dataRaw, waveformNumber, paddingMode) 
    
    def waveformFlush(self) :
        return self._sd_aou.waveformFlush()
    
    def AWGqueueWaveform(self, nAWG, waveformNumber, triggerMode, startDelay, cycles, prescaler) :
        return self._sd_aou.AWGqueueWaveform(nAWG, waveformNumber, triggerMode, startDelay, cycles, prescaler)
    
    def AWGstartMultiple(self, AWGmask) :
        return self._sd_aou.AWGstartMultiple(AWGmask)
    
    def AWGstopMultiple(self, AWGmask) :
        return self._sd_aou.AWGstopMultiple(AWGmask)
    
    def AWGresumeMultiple(self, AWGmask) :
        return self._sd_aou.AWGresumeMultiple(AWGmask)
    
    def AWGpauseMultiple(self, AWGmask) :
        return self._sd_aou.AWGpauseMultiple(AWGmask)
    
    def AWGtriggerMultiple(self, AWGmask) :
        return self._sd_aou.AWGtriggerMultiple(AWGmask)
    
    def AWGstart(self, nAWG) :
        return self._sd_aou.AWGstart(nAWG)
    
    def AWGstop(self, nAWG) :
        return self._sd_aou.AWGstop(nAWG)
    
    def AWGresume(self, nAWG) :
        return self._sd_aou.AWGresume(nAWG)
    
    def AWGpause(self, nAWG) :
        return self._sd_aou.AWGpause(nAWG)
    
    def AWGtrigger(self, nAWG) :
        return self._sd_aou.AWGtrigger(nAWG)
    
    def AWGjumpNextWaveform(self, nAWG) :
        return self._sd_aou.AWGjumpNextWaveform(nAWG)
    
    def AWGflush(self, nAWG) :
        return self._sd_aou.AWGflush(nAWG)
    
    def AWGisRunning(self, nAWG) :
        return self._sd_aou.AWGisRunning(nAWG)
    
    def AWGnWFplaying(self, nAWG) :
        return self._sd_aou.AWGnWFplaying(nAWG)
    
    def AWGfromArray(self, nAWG, triggerMode, startDelay, cycles, prescaler, waveformType, waveformDataA, waveformDataB = None, paddingMode = 0) :
        return self._sd_aou.AWGfromArray(nAWG, triggerMode, startDelay, cycles, prescaler, waveformType, waveformDataA, waveformDataB, paddingMode)
    
    def AWGFromFile(self, nAWG, waveformFile, triggerMode, startDelay, cycles, prescaler, paddingMode = 0) :
        return self._sd_aou.AWGFromFile(nAWG, waveformFile, triggerMode, startDelay, cycles, prescaler, paddingMode)
    
    def AWGtriggerExternalConfig(self, nAWG, externalSource, triggerBehavior, sync = SD_SyncModes.SYNC_CLK10) :
        return self._sd_aou.AWGtriggerExternalConfig(nAWG, externalSource, triggerBehavior, sync)
    
    def AWGidleValue(self, nAWG, value) :
        return self._sd_aou.AWGidleValue(nAWG, value)
    
    def AWGidleValueRead(self, nAWG) :
        return self._sd_aou.AWGidleValueRead(nAWG)
    
    def AWGqueueConfig(self, nAWG, mode) :
        return self._sd_aou.AWGqueueConfig(nAWG, mode)
    
    def AWGqueueConfigRead(self, nAWG) :
        return self._sd_aou.AWGqueueConfigRead(nAWG)
    
    def AWGqueueMarkerConfig(self, nAWG, markerMode, trgPXImask, trgIOmask, value, syncMode, length, delay) :
        return self._sd_aou.AWGqueueMarkerConfig(nAWG, markerMode, trgPXImask, trgIOmask, value, syncMode, length, delay)
    
    def AWGqueueSyncMode(self, nAWG, syncMode) :
        return self._sd_aou.AWGqueueSyncMode(nAWG, syncMode)
    
    #DIO Functions
    ##Config
    def IOstandardConfig(self, portSector, logicStandard) :
        return self._sd_dio.IOstandardConfig(portSector, logicStandard)
    
    def IOdirectionConfig(self, lineMask, direction) :
        return self._sd_dio.IOdirectionConfig(lineMask, direction)
    
    ##Ports
    def portWrite(self, nPort, portValue) :
        return self._sd_dio.portWrite(nPort, portValue)
    
    def portWriteWithMask(self, nPort, portValue, lineMask) :
        return self._sd_dio.portWriteWithMask(nPort, portValue, lineMask)
    
    def portRead(self, nPort) :
        return self._sd_dio.portRead(nPort)
    
    ##Buses
    def busConfig(self, nBus, nPort, StartBit, EndBit):
        return self._sd_dio.busConfig(nBus, nPort, StartBit, EndBit)
    
    def busWrite(self, nBus, busValue) :
        return self._sd_dio.busWrite(nBus, busValue)
    
    def busRead(self, nBus) :
        return self._sd_dio.busRead(nBus)
    
    def busSamplingConfig(self, nBus, switchStrobe, strobeOn, strobeType, strobeDelay, prescaler = 0, debouncing = 0) :
        return self._sd_dio.busSamplingConfig(nBus, switchStrobe, strobeOn, strobeType, strobeDelay, prescaler = 0, debouncing = 0)
    
    ##Digital Lines
    def lineWrite(self, nPort, nLine, lineValue) :
        return self._sd_dio.lineWrite(nPort, nLine, lineValue)
    
    def lineRead(self, nPort, nLine) :
        return self._sd_dio.lineRead(nPort, nLine)
    
    ##DWG
    def waveformGetAddress(self, waveformNumber) :
        return self._sd_dio.waveformGetAddress(waveformNumber)
    
    def waveformGetMemorySize(self, waveformNumber) :
        return self._sd_dio.waveformGetMemorySize(waveformNumber)
    
    def waveformMemoryGetWriteAddress(self) :
        return self._sd_dio.waveformMemoryGetWriteAddress()
    
    def waveformMemorySetWriteAddress(self, writeAddress) :
        return self._sd_dio.waveformMemorySetWriteAddress(writeAddress)
    
    def waveformReLoad(self, waveformObject, waveformNumber, paddingMode = 0) :
        return self._sd_dio.waveformReLoad(waveformObject, waveformNumber, paddingMode) 
    
    def waveformReLoadArrayInt16(self, waveformType, dataRaw, waveformNumber, paddingMode = 0) :
        return self._sd_dio.waveformReLoadArrayInt16(waveformType, dataRaw, waveformNumber, paddingMode) 
    
    def waveformLoad(self, waveformObject, waveformNumber, paddingMode = 0) :
        return self._sd_dio.waveformLoad(waveformObject, waveformNumber, paddingMode) 
    
    def waveformLoadArrayInt16(self, waveformType, dataRaw, waveformNumber, paddingMode = 0) :
        return self._sd_dio.waveformLoadArrayInt16(waveformType, dataRaw, waveformNumber, paddingMode) 
    
    def waveformFlush(self) :
        return self._sd_dio.waveformFlush() 
    
    def DWGqueueWaveform(self, nDWG, waveformNumber, triggerMode, startDelay, cycles, prescaler) :
        return self._sd_dio.DWGqueueWaveform(nDWG, waveformNumber, triggerMode, startDelay, cycles, prescaler) 
    
    def DWGstart(self, nDWG) :
        return self._sd_dio.DWGstart(nDWG)
    
    def DWGstop(self, nDWG) :
        return self._sd_dio.DWGstop(nDWG) 
    
    def DWGresume(self, nDWG) :
        return self._sd_dio.DWGresume(nDWG) 
    
    def DWGpause(self, nDWG) :
        return self._sd_dio.DWGpause(nDWG) 
    
    def DWGtrigger(self, nDWG) :
        return self._sd_dio.DWGtrigger(nDWG)
    
    def DWGstartMultiple(self, DWGmask) :
        return self._sd_dio.DWGstartMultiple(DWGmask)
    
    def DWGstopMultiple(self, DWGmask) :
        return self._sd_dio.DWGstopMultiple(DWGmask)
    
    def DWGresumeMultiple(self, DWGmask) :
        return self._sd_dio.DWGresumeMultiple(DWGmask)
    
    def DWGpauseMultiple(self, DWGmask) :
        return self._sd_dio.DWGpauseMultiple(DWGmask) 
    
    def DWGtriggerMultiple(self, DWGmask) :
        return self._sd_dio.DWGtriggerMultiple(DWGmask)
    
    def DWGflush(self, nDWG) :
        return self._sd_dio.DWGflush(nDWG)
    
    def DWGisRunning(self, nDWG) :
        return self._sd_dio.DWGisRunning(nDWG)
    
    def DWGnWFplaying(self, nDWG) :
        return self._sd_dio.DWGnWFplaying(nDWG)
    
    def DWGfromFile(self, nDWG, waveformFile, triggerMode, startDelay, cycles, prescaler, paddingMode = 0) :
        return self._sd_dio.DWGfromFile(nDWG, waveformFile, triggerMode, startDelay, cycles, prescaler, paddingMode)
    
    def DWG(self, nDWG, triggerMode, startDelay, cycles, prescaler, waveformType, waveformDataA, waveformDataB = None, paddingMode = 0) :
        return self._sd_dio.DWG(nDWG, triggerMode, startDelay, cycles, prescaler, waveformType, waveformDataA, waveformDataB = None, paddingMode)
    
    def DWGtriggerExternalConfig(self, nDWG, externalSource, triggerBehavior) :
        return self._sd_dio.DWGtriggerExternalConfig(nDWG, externalSource, triggerBehavior)
    
    def DAQread(self, nDAQ, nPoints, timeOut = 0) :
        return self._sd_dio.DAQread(nDAQ, nPoints, timeOut)
    
    def DAQconfig(self, nDAQ, nDAQpointsPerCycle, nCycles, prescaler, triggerMode) :
        return self._sd_dio.DAQconfig(nDAQ, nDAQpointsPerCycle, nCycles, prescaler, triggerMode)
    
    def DAQtriggerExternalConfig(self, nDAQ, externalSource, triggerBehavior) :
        return self._sd_dio.DAQtriggerExternalConfig(nDAQ, externalSource, triggerBehavior)
    
    def DAQcounterRead(self, nDAQ) :
        return self._sd_dio.DAQcounterRead(nDAQ)
    
    def DAQstart(self, nDAQ) :
        return self._sd_dio.DAQstart(nDAQ)
    
    def DAQpause(self, nDAQ) :
        return self._sd_dio.DAQpause(nDAQ)
    
    def DAQresume(self, nDAQ) :
        return self._sd_dio.DAQresume(nDAQ)
    
    def DAQflush(self, nDAQ) :
        return self._sd_dio.DAQflush(nDAQ)
    
    def DAQstop(self, nDAQ) :
        return self._sd_dio.DAQstop(nDAQ)
    
    def DAQtrigger(self, nDAQ) :
        return self._sd_dio.DAQtrigger(nDAQ)
    
    def DAQstartMultiple(self, DAQmask) :
        return self._sd_dio.DAQstartMultiple(DAQmask)
    
    def DAQpauseMultiple(self, DAQmask) :
        return self._sd_dio.DAQpauseMultiple(DAQmask)
    
    def DAQresumeMultiple(self, DAQmask) :
        return self._sd_dio.DAQresumeMultiple(DAQmask)
    
    def DAQflushMultiple(self, DAQmask) :
        return self._sd_dio.DAQflushMultiple(DAQmask)
    
    def DAQstopMultiple(self, DAQmask) :
        return self._sd_dio.DAQstopMultiple(DAQmask)
    
    def DAQtriggerMultiple(self, DAQmask) :
        return self._sd_dio.DAQtriggerMultiple(DAQmask)

    #SD_AIN Functions
	def channelInputConfig(self, channel, fullScale, impedance, coupling) :
	def channelPrescalerConfig(self, channel, prescaler) :
	def channelPrescalerConfigMultiple(self, mask, prescaler) :
	def channelPrescaler(self, channel) :
	def channelFullScale(self, channel) :
	def channelMinFullScale(self, impedance, coupling) :
	def channelMaxFullScale(self, impedance, coupling) :
	def channelImpedance(self, channel) :
	def channelCoupling(self, channel) :
	def channelTriggerConfig(self, channel, analogTriggerMode, threshold) :
	def clockIOconfig(self, clockConfig) :
	def clockGetFrequency(self) :
	def clockGetSyncFrequency(self) :
	def clockSetFrequency(self, frequency, mode = 1) :
	def clockResetPhase(self, triggerBehavior, PXItrigger, skew = 0.0) :
	def triggerIOconfig(self, direction) :
	def triggerIOwrite(self, value, syncMode = 1) :
	def triggerIOread(self) :
	def DAQconfig(self, channel, pointsPerCycle, nCycles, triggerDelay, triggerMode) :
	def DAQtriggerConfig(self, channel, digitalTriggerMode, digitalTriggerSource, analogTriggerMask) :
	def DAQanalogTriggerConfig(self, channel, analogTriggerMask) :
	def DAQdigitalTriggerConfig(self, channel, triggerSource, triggerBehavior) :
	def DAQtriggerExternalConfig(self, nDAQ, externalSource, triggerBehavior, sync = SD_SyncModes.SYNC_NONE) :
	def DAQstart(self, channel) :
	def DAQstop(self, channel) :
	def DAQflush(self, channel) :
	def DAQtrigger(self, channel) :
	def DAQstartMultiple(self, channel) :
	def DAQstopMultiple(self, channel) :
	def DAQflushMultiple(self, channel) :
	def DAQtriggerMultiple(self, channel) :
	def DAQread(self, nDAQ, nPoints, timeOut = 0) :
	def DAQcounterRead(self, nDAQ) :
	def DAQbufferPoolConfig(self, nDAQ, nPoints, timeOut = 0):
	def DAQbufferPoolRelease(self, nDAQ):
	def DAQbufferGet(self, nDAQ):
	def FFT(self, channel, data, dB = False, windowType = 0) :
	
class SD_HVI(SD_Object) :
	def isOpen(self) :
		return (self._SD_Object__handle > 0);

	def open(self, fileHVI) :
		status = self._SD_Object__handle;

		if status <= 0 :
			status = self._SD_Object__handle = self._SD_Object__core_dll.SD_HVI_open(fileHVI.encode());

			if status > 0 :
				status = self._SD_Object__core_dll.SD_HVI_load(self._SD_Object__handle);

		return status;

	def close(self) :
		if self._SD_Object__handle > 0 :
			self._SD_Object__handle = self._SD_Object__core_dll.SD_HVI_close(self._SD_Object__handle);

		return self._SD_Object__core_dll;

	def getType(self) :
		return const.object_type.HVI;

	##HVI Control
	def compile(self) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_HVI_compile(self._SD_Object__handle);
		else :
			return const.error.HVI_NOT_OPENED;

	def compilationErrorMessage(self, errorIndex) :
		error = 0;
		message = ''.rjust(200, '\0').encode();

		if self._SD_Object__handle > 0 :
			error = self._SD_Object__core_dll.SD_HVI_compilationErrorMessage(self._SD_Object__handle, errorIndex, message, len(message));

			if error >= 0 :
				return self._SD_Object__formatString(message);
		else :
			error = const.error.HVI_NOT_OPENED;

		return error;

	def load(self) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_HVI_load(self._SD_Object__handle);
		else :
			return const.error.HVI_NOT_OPENED;

	def assignHardwareWithIndexAndSerialNumber(self, index, partNumber, serialNumber) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_HVI_assignHardwareWithIndexAndSerialNumber(self._SD_Object__handle, index, partNumber.encode(), serialNumber.encode());
		else :
			return const.error.HVI_NOT_OPENED;

	def assignHardwareWithIndexAndSlot(self, index, nChassis, nSlot) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_HVI_assignHardwareWithIndexAndSlot(self._SD_Object__handle, index, nChassis, nSlot);
		else :
			return const.error.HVI_NOT_OPENED;

	def assignHardwareWithUserNameAndSerialNumber(self, moduleUserName, partNumber, serialNumber) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_HVI_assignHardwareWithUserNameAndSerialNumber(self._SD_Object__handle, moduleUserName.encode(), partNumber.encode(), serialNumber.encode());
		else :
			return const.error.HVI_NOT_OPENED;

	def assignHardwareWithUserNameAndSlot(self, moduleUserName, nChassis, nSlot) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_HVI_assignHardwareWithUserNameAndSlot(self._SD_Object__handle, moduleUserName.encode(), nChassis, nSlot);
		else :
			return const.error.HVI_NOT_OPENED;

	def assignHardwareWithUserNameAndModuleID(self, moduleUserName, module) :
		if self._SD_Object__handle > 0 :
			if module is not None and module.isOpen() :
				return self._SD_Object__core_dll.SD_HVI_assignHardwareWithUserNameAndModuleID(self._SD_Object__handle, moduleUserName.encode(), module._SD_Object__handle);
			else :
				return const.error.MODULE_NOT_OPENED;
		else :
			return const.error.HVI_NOT_OPENED;

	def start(self) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_HVI_start(self._SD_Object__handle);
		else :
			return const.error.HVI_NOT_OPENED;

	def pause(self) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_HVI_pause(self._SD_Object__handle);
		else :
			return const.error.HVI_NOT_OPENED;

	def resume(self) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_HVI_resume(self._SD_Object__handle);
		else :
			return const.error.HVI_NOT_OPENED;

	def stop(self) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_HVI_stop(self._SD_Object__handle);
		else :
			return const.error.HVI_NOT_OPENED;

	def reset(self) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_HVI_reset(self._SD_Object__handle);
		else :
			return const.error.HVI_NOT_OPENED;

	##HVI Modules
	def getNumberOfModules(self) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_HVI_getNumberOfModules(self._SD_Object__handle);
		else :
			return const.error.HVI_NOT_OPENED;

	def getModuleName(self, index) :
		if self._SD_Object__handle > 0 :
			self._SD_Object__core_dll.SD_HVI_getModuleNameHidden.restype = c_char_p;
			return self._SD_Object__core_dll.SD_HVI_getModuleNameHidden(self._SD_Object__handle, index).decode();
		else :
			return const.error.MODULE_NOT_FOUND;

	def getModuleIndex(self, moduleUserName) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_HVI_getModuleIndex(self._SD_Object__handle, moduleUserName.encode());
		else :
			return const.error.HVI_NOT_OPENED;

	def getModuleByIndex(self, index) :
		if self._SD_Object__handle > 0 :
			return self.getModuleByName(self.getModuleName(index));
		else :
			return const.error.HVI_NOT_OPENED;

	def getModuleByName(self, moduleUserName) :
		if self._SD_Object__handle > 0 :
			moduleHandle = self._SD_Object__core_dll.SD_HVI_getModuleIDwithUserName(self._SD_Object__handle, moduleUserName.encode());

			if moduleHandle > 0 :
				switcher = {
					const.object_type.AOU: SD_AOU(),
					const.object_type.DIO: SD_DIO(),
##					const.object_type.TDC: SD_TDC(),
					const.object_type.AIN: SD_AIN(),
##					const.object_type.AIO: SD_AIO(),
				}

				requestModule = switcher.get(SD_Module.getType(moduleHandle), "nothing");

				if requestModule == "nothing" :
					return const.error.MODULE_NOT_FOUND;
				else :
					requestModule._SD_Object__handle = moduleHandle;
			else :
				return moduleHandle;
		else :
			return const.error.HVI_NOT_OPENED;

	##HVI Module's Constants
	def readIntegerConstantWithIndex(self, moduleIndex, constantName) :
		value = c_int32();
		error = const.error.HVI_NOT_OPENED;

		if self._SD_Object__handle > 0 :
			error = self._SD_Object__core_dll.SD_HVI_readIntegerConstantWithIndex(self._SD_Object__handle, moduleIndex, constantName.encode(), byref(value));

		return (error, value.value);

	def readIntegerConstantWithUserName(self, moduleUserName, constantName) :
		value = c_int32();
		error = const.error.HVI_NOT_OPENED;

		if self._SD_Object__handle > 0 :
			error = self._SD_Object__core_dll.SD_HVI_readIntegerConstantWithUserName(self._SD_Object__handle, moduleUserName.encode(), constantName.encode(), byref(value));

		return (error, value.value);

	def writeIntegerConstantWithIndex(self, moduleIndex, constantName, value) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_HVI_writeIntegerConstantWithIndex(self._SD_Object__handle, moduleIndex, constantName.encode(), value);
		else: 
			return const.error.HVI_NOT_OPENED;

	def writeIntegerConstantWithUserName(self, moduleUserName, constantName, value) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_HVI_writeIntegerConstantWithUserName(self._SD_Object__handle, moduleUserName.encode(), constantName.encode(), value);
		else :
			return const.error.HVI_NOT_OPENED;

	def readDoubleConstantWithIndex(self, moduleIndex, constantName) :
		value = c_double();
		unit = c_char_p();
		error = const.error.HVI_NOT_OPENED;

		if self._SD_Object__handle > 0 :
			error = self._SD_Object__core_dll.SD_HVI_readDoubleConstantWithIndex(self._SD_Object__handle, moduleIndex, constantName.encode(), byref(value), byref(unit));

		return (error, value.value, unit.value.decode());

	def readDoubleConstantWithUserName(self, moduleUserName, constantName) :
		value = c_double();
		unit = c_char_p();
		error = const.error.HVI_NOT_OPENED;

		if self._SD_Object__handle > 0 :
			error = self._SD_Object__core_dll.SD_HVI_readDoubleConstantWithUserName(self._SD_Object__handle, moduleUserName.encode(), constantName.encode(), byref(value), byref(unit));

		return (error, value.value, unit.value.decode());

	def writeDoubleConstantWithIndex(self, moduleIndex, constantName, value, unit) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_HVI_writeDoubleConstantWithIndex(self._SD_Object__handle, moduleIndex, constantName.encode(), c_double(value), unit.encode());
		else :
			return const.error.HVI_NOT_OPENED;

	def writeDoubleConstantWithUserName(self, moduleUserName, constantName, value, unit) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_HVI_writeDoubleConstantWithUserName(self._SD_Object__handle, moduleUserName.encode(), constantName.encode(), c_double(value), unit.encode());
		else :
			return const.error.HVI_NOT_OPENED;

class SD_AIN_TriggerMode :
	RISING_EDGE = 1;
	FALLING_EDGE = 2;
	BOTH_EDGES = 3;

class SD_AIN_SyncTriggerBehaviours :
	TRIGGER_HIGH_SYNC = SD_TriggerBehaviors.TRIGGER_HIGH + 8;
	TRIGGER_LOW_SYNC = SD_TriggerBehaviors.TRIGGER_LOW + 8;
	TRIGGER_RISE_SYNC = SD_TriggerBehaviors.TRIGGER_RISE + 8;
	TRIGGER_FALL_SYNC = SD_TriggerBehaviors.TRIGGER_FALL + 8;

class AIN_Coupling :
	AIN_COUPLING_DC = 0;
	AIN_COUPLING_AC = 1;

class AIN_Impedance :
	AIN_IMPEDANCE_HZ = 0;
	AIN_IMPEDANCE_50 = 1;

