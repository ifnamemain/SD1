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

class SD_DIO(SD_Module) :
	##Config
	def IOstandardConfig(self, portSector, logicStandard) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_IOstandardConfig(self._SD_Object__handle, portSector, logicStandard);
		else :
			return const.error.MODULE_NOT_OPENED;

	def IOdirectionConfig(self, lineMask, direction) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_IOdirectionConfig(self._SD_Object__handle, c_longlong(lineMask), direction);
		else :
			return const.error.MODULE_NOT_OPENED;

	##Ports
	def portWrite(self, nPort, portValue) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_portWrite(self._SD_Object__handle, nPort, c_longlong(portValue));
		else :
			return const.error.MODULE_NOT_OPENED;

	def portWriteWithMask(self, nPort, portValue, lineMask) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_portWriteWithMask(self._SD_Object__handle, nPort, c_longlong(portValue), c_longlong(lineMask));
		else :
			return const.error.MODULE_NOT_OPENED;

	def portRead(self, nPort) :
		value = c_longlong(0);
		error = c_int(const.error.MODULE_NOT_OPENED);

		if self._SD_Object__handle > 0 :
			self._SD_Object__core_dll.SD_DIO_portRead.restype = c_longlong;
			value = self._SD_Object__core_dll.SD_DIO_portRead(self._SD_Object__handle, nPort, byref(error));

		return (value.value, error.value);

	##Buses
	def busConfig(self, nBus, nPort, StartBit, EndBit):
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_busConfig(self._SD_Object__handle, nBus, nPort, StartBit, EndBit);
		else :
			return const.error.MODULE_NOT_OPENED;

	def busWrite(self, nBus, busValue) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_busWrite(self._SD_Object__handle, nBus, busValue);
		else :
			return const.error.MODULE_NOT_OPENED;

	def busRead(self, nBus) :
		error = c_int(const.error.MODULE_NOT_OPENED);
		value = 0;

		if self._SD_Object__handle > 0 :
			value = self._SD_Object__core_dll.SD_DIO_busRead(self._SD_Object__handle, nBus, byref(error));

		return (value, error.value);

	def busSamplingConfig(self, nBus, switchStrobe, strobeOn, strobeType, strobeDelay, prescaler = 0, debouncing = 0) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_busSamplingConfig(self._SD_Object__handle, nBus, switchStrobe, strobeOn, strobeType, c_float(strobeDelay), prescaler, debouncing);
		else :
			return const.error.MODULE_NOT_OPENED;

	##Digital Lines
	def lineWrite(self, nPort, nLine, lineValue) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_lineWrite(self._SD_Object__handle, nPort, nLine, lineValue);
		else :
			return const.error.MODULE_NOT_OPENED;

	def lineRead(self, nPort, nLine) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_lineRead(self._SD_Object__handle, nPort, nLine);
		else :
			return const.error.MODULE_NOT_OPENED;

	##DWG
	def waveformGetAddress(self, waveformNumber) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_waveformGetAddress(self._SD_Object__handle, waveformNumber);
		else :
			return const.error.MODULE_NOT_OPENED;

	def waveformGetMemorySize(self, waveformNumber) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_waveformGetMemorySize(self._SD_Object__handle, waveformNumber);
		else :
			return const.error.MODULE_NOT_OPENED;

	def waveformMemoryGetWriteAddress(self) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_waveformMemoryGetWriteAddress(self._SD_Object__handle);
		else :
			return const.error.MODULE_NOT_OPENED;

	def waveformMemorySetWriteAddress(self, writeAddress) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_waveformMemorySetWriteAddress(self._SD_Object__handle, writeAddress);
		else :
			return const.error.MODULE_NOT_OPENED;

	def waveformReLoad(self, waveformObject, waveformNumber, paddingMode = 0) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_waveformReLoad(self._SD_Object__handle, waveformObject._SD_Object__handle, waveformNumber, paddingMode);
		else :
			return const.error.MODULE_NOT_OPENED;

	def waveformReLoadArrayInt16(self, waveformType, dataRaw, waveformNumber, paddingMode = 0) :
		if self._SD_Object__handle > 0 :
			if len(dataRaw) > 0 :
				dataC = (c_short * len(dataRaw))(*dataRaw);
				return self._SD_Object__core_dll.SD_DIO_waveformReLoadArrayInt16(self._SD_Object__handle, waveformType, dataC._length_, dataC, waveformNumber, paddingMode);
			else :
				return const.error.INVALID_VALUE;
		else :
			return const.error.MODULE_NOT_OPENED;

	def waveformLoad(self, waveformObject, waveformNumber, paddingMode = 0) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_waveformLoad(self._SD_Object__handle, waveformObject._SD_Object__handle, waveformNumber, paddingMode);
		else :
			return const.error.MODULE_NOT_OPENED;

	def waveformLoadArrayInt16(self, waveformType, dataRaw, waveformNumber, paddingMode = 0) :
		if self._SD_Object__handle > 0 :
			if len(dataRaw) > 0 :
				dataC = (c_short * len(dataRaw))(*dataRaw);
				return self._SD_Object__core_dll.SD_DIO_waveformLoadArrayInt16(self._SD_Object__handle, waveformType, dataC._length_, dataC, waveformNumber, paddingMode);
			else :
				return const.error.INVALID_VALUE;
		else :
			return const.error.MODULE_NOT_OPENED;

	def waveformFlush(self) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_waveformFlush(self._SD_Object__handle);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DWGqueueWaveform(self, nDWG, waveformNumber, triggerMode, startDelay, cycles, prescaler) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_DWGqueueWaveform(self._SD_Object__handle, nDWG, waveformNumber, triggerMode, startDelay, cycles, prescaler);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DWGstart(self, nDWG) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_DWGstart(self._SD_Object__handle, nDWG);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DWGstop(self, nDWG) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_DWGstop(self._SD_Object__handle, nDWG);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DWGresume(self, nDWG) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_DWGresume(self._SD_Object__handle, nDWG);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DWGpause(self, nDWG) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_DWGpause(self._SD_Object__handle, nDWG);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DWGtrigger(self, nDWG) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_DWGtrigger(self._SD_Object__handle, nDWG);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DWGstartMultiple(self, DWGmask) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_DWGstartMultiple(self._SD_Object__handle, DWGmask);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DWGstopMultiple(self, DWGmask) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_DWGstopMultiple(self._SD_Object__handle, DWGmask);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DWGresumeMultiple(self, DWGmask) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_DWGresumeMultiple(self._SD_Object__handle, DWGmask);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DWGpauseMultiple(self, DWGmask) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_DWGpauseMultiple(self._SD_Object__handle, DWGmask);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DWGtriggerMultiple(self, DWGmask) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_DWGtriggerMultiple(self._SD_Object__handle, DWGmask);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DWGflush(self, nDWG) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_DWGflush(self._SD_Object__handle, nDWG);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DWGisRunning(self, nDWG) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_DWGisRunning(self._SD_Object__handle, nDWG);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DWGnWFplaying(self, nDWG) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_DWGnWFplaying(self._SD_Object__handle, nDWG);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DWGfromFile(self, nDWG, waveformFile, triggerMode, startDelay, cycles, prescaler, paddingMode = 0) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_DWGfromFile(self._SD_Object__handle, nDWG, waveformFile.encode(), triggerMode, startDelay, cycles, prescaler, paddingMode);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DWG(self, nDWG, triggerMode, startDelay, cycles, prescaler, waveformType, waveformDataA, waveformDataB = None, paddingMode = 0) :
		if self._SD_Object__handle > 0 :
			if len(waveformDataA) > 0 and (waveformDataB is None or len(waveformDataA) == len(waveformDataB)) :
				waveform_dataA_C = (c_int * len(waveformDataA))(*waveformDataA);

				if waveformDataB is None:
					waveform_dataB_C = c_void_p(0);
				else :
					waveform_dataB_C = (c_int * len(waveformDataB))(*waveformDataB);

				return self._SD_Object__core_dll.SD_DIO_DWGfromArray(self._SD_Object__handle, nDWG, triggerMode, startDelay, cycles, prescaler, waveformType, waveform_dataA_C._length_, waveform_dataA_C, waveform_dataB_C, paddingMode)
			else :
				return const.error.INVALID_VALUE
		else :
			return const.error.MODULE_NOT_OPENED

	def DWGtriggerExternalConfig(self, nDWG, externalSource, triggerBehavior) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_DWGtriggerExternalConfig(self._SD_Object__handle, nDWG, externalSource, triggerBehavior);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DAQread(self, nDAQ, nPoints, timeOut = 0) :
		if self._SD_Object__handle > 0 :
			if nPoints > 0 :
				data = (c_short * nPoints)()

				nPoints = self._SD_Object__core_dll.SD_DIO_DAQread(self._SD_Object__handle, nDAQ, data, nPoints, timeOut)

				if nPoints > 0 :
					return np.array(data)
				else :
					return np.empty(0, dtype=np.short)
			else :
				return const.error.INVALID_VALUE
		else :
			return const.error.MODULE_NOT_OPENED

	def DAQconfig(self, nDAQ, nDAQpointsPerCycle, nCycles, prescaler, triggerMode) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_DAQconfig(self._SD_Object__handle, nDAQ, nDAQpointsPerCycle, nCycles, prescaler, triggerMode);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DAQtriggerExternalConfig(self, nDAQ, externalSource, triggerBehavior) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_DAQtriggerExternalConfig(self._SD_Object__handle, nDAQ, externalSource, triggerBehavior);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DAQcounterRead(self, nDAQ) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_DAQcounterRead(self._SD_Object__handle, nDAQ);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DAQstart(self, nDAQ) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_DAQstart(self._SD_Object__handle, nDAQ);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DAQpause(self, nDAQ) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_DAQpause(self._SD_Object__handle, nDAQ);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DAQresume(self, nDAQ) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_DAQresume(self._SD_Object__handle, nDAQ);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DAQflush(self, nDAQ) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_DAQflush(self._SD_Object__handle, nDAQ);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DAQstop(self, nDAQ) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_DAQstop(self._SD_Object__handle, nDAQ);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DAQtrigger(self, nDAQ) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_DAQtrigger(self._SD_Object__handle, nDAQ);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DAQstartMultiple(self, DAQmask) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_DAQstartMultiple(self._SD_Object__handle, DAQmask);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DAQpauseMultiple(self, DAQmask) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_DAQpauseMultiple(self._SD_Object__handle, DAQmask);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DAQresumeMultiple(self, DAQmask) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_DAQresumeMultiple(self._SD_Object__handle, DAQmask);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DAQflushMultiple(self, DAQmask) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_DAQflushMultiple(self._SD_Object__handle, DAQmask);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DAQstopMultiple(self, DAQmask) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_DAQstopMultiple(self._SD_Object__handle, DAQmask);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DAQtriggerMultiple(self, DAQmask) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_DIO_DAQtriggerMultiple(self._SD_Object__handle, DAQmask);
		else :
			return const.error.MODULE_NOT_OPENED;

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

class SD_AIN(SD_Module) :
	def channelInputConfig(self, channel, fullScale, impedance, coupling) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_AIN_channelInputConfig(self._SD_Object__handle, channel, c_double(fullScale), impedance, coupling);
		else :
			return const.error.MODULE_NOT_OPENED;

	def channelPrescalerConfig(self, channel, prescaler) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_AIN_channelPrescalerConfig(self._SD_Object__handle, channel, prescaler);
		else :
			return const.error.MODULE_NOT_OPENED;

	def channelPrescalerConfigMultiple(self, mask, prescaler) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_AIN_channelPrescalerConfigMultiple(self._SD_Object__handle, mask, prescaler);
		else :
			return const.error.MODULE_NOT_OPENED;

	def channelPrescaler(self, channel) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_AIN_channelPrescaler(self._SD_Object__handle, channel);
		else :
			return const.error.MODULE_NOT_OPENED;

	def channelFullScale(self, channel) :
		if self._SD_Object__handle > 0 :
			self._SD_Object__core_dll.SD_AIN_channelFullScale.restype = c_double;
			result = self._SD_Object__core_dll.SD_AIN_channelFullScale(self._SD_Object__handle, channel);

			if result < 0 :
				return int(result);
			else :
				return result;
		else :
			return const.error.MODULE_NOT_OPENED;

	def channelMinFullScale(self, impedance, coupling) :
		if self._SD_Object__handle > 0 :
			self._SD_Object__core_dll.SD_AIN_channelMinFullScale.restype = c_double;
			result = self._SD_Object__core_dll.SD_AIN_channelMinFullScale(self._SD_Object__handle, impedance, coupling);

			if result < 0 :
				return int(result);
			else :
				return result;
		else :
			return const.error.MODULE_NOT_OPENED;

	def channelMaxFullScale(self, impedance, coupling) :
		if self._SD_Object__handle > 0 :
			self._SD_Object__core_dll.SD_AIN_channelMaxFullScale.restype = c_double;
			result = self._SD_Object__core_dll.SD_AIN_channelMaxFullScale(self._SD_Object__handle, impedance, coupling);

			if result < 0 :
				return int(result);
			else :
				return result;
		else :
			return const.error.MODULE_NOT_OPENED;

	def channelImpedance(self, channel) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_AIN_channelImpedance(self._SD_Object__handle, channel);
		else :
			return const.error.MODULE_NOT_OPENED;

	def channelCoupling(self, channel) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_AIN_channelCoupling(self._SD_Object__handle, channel);
		else :
			return const.error.MODULE_NOT_OPENED;

	def channelTriggerConfig(self, channel, analogTriggerMode, threshold) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_AIN_channelTriggerConfig(self._SD_Object__handle, channel, analogTriggerMode, c_double(threshold));
		else :
			return const.error.MODULE_NOT_OPENED;

	def clockIOconfig(self, clockConfig) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_AIN_clockIOconfig(self._SD_Object__handle, clockConfig);
		else :
			return const.error.MODULE_NOT_OPENED;

	def clockGetFrequency(self) :
		if self._SD_Object__handle > 0 :
			self._SD_Object__core_dll.SD_AIN_clockGetFrequency.restype = c_double;
			result = self._SD_Object__core_dll.SD_AIN_clockGetFrequency(self._SD_Object__handle);

			if result < 0 :
				return int(result);
			else :
				return result;
		else :
			return const.error.MODULE_NOT_OPENED;

	def clockGetSyncFrequency(self) :
		if self._SD_Object__handle > 0 :
			self._SD_Object__core_dll.SD_AIN_clockGetSyncFrequency.restype = c_double;
			result = self._SD_Object__core_dll.SD_AIN_clockGetSyncFrequency(self._SD_Object__handle);

			if result < 0 :
				return int(result);
			else :
				return result;
		else :
			return const.error.MODULE_NOT_OPENED;

	def clockSetFrequency(self, frequency, mode = 1) :
		if self._SD_Object__handle > 0 :
			self._SD_Object__core_dll.SD_AIN_clockSetFrequency.restype = c_double;
			result = self._SD_Object__core_dll.SD_AIN_clockSetFrequency(self._SD_Object__handle, c_double(frequency), mode);

			if result < 0 :
				return int(result);
			else :
				return result;
		else :
			return const.error.MODULE_NOT_OPENED;

	def clockResetPhase(self, triggerBehavior, PXItrigger, skew = 0.0) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_AIN_clockResetPhase(self._SD_Object__handle, triggerBehavior, PXItrigger, c_double(skew));
		else :
			return const.error.MODULE_NOT_OPENED;

	def triggerIOconfig(self, direction) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_AIN_triggerIOconfig(self._SD_Object__handle, direction);
		else :
			return const.error.MODULE_NOT_OPENED;

	def triggerIOwrite(self, value, syncMode = 1) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_AIN_triggerIOwrite(self._SD_Object__handle, value, syncMode);
		else :
			return const.error.MODULE_NOT_OPENED;

	def triggerIOread(self) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_AIN_triggerIOread(self._SD_Object__handle);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DAQconfig(self, channel, pointsPerCycle, nCycles, triggerDelay, triggerMode) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_AIN_DAQconfig(self._SD_Object__handle, channel, pointsPerCycle, nCycles, triggerDelay, triggerMode);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DAQtriggerConfig(self, channel, digitalTriggerMode, digitalTriggerSource, analogTriggerMask) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_AIN_DAQtriggerConfig(self._SD_Object__handle, channel, digitalTriggerMode, digitalTriggerSource, analogTriggerMask);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DAQanalogTriggerConfig(self, channel, analogTriggerMask) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_AIN_DAQanalogTriggerConfig(self._SD_Object__handle, channel, analogTriggerMask);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DAQdigitalTriggerConfig(self, channel, triggerSource, triggerBehavior) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_AIN_DAQdigitalTriggerConfig(self._SD_Object__handle, channel, triggerSource, triggerBehavior);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DAQtriggerExternalConfig(self, nDAQ, externalSource, triggerBehavior, sync = SD_SyncModes.SYNC_NONE) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_AIN_DAQtriggerExternalConfig(self._SD_Object__handle, nDAQ, externalSource, triggerBehavior, sync);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DAQstart(self, channel) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_AIN_DAQstart(self._SD_Object__handle, channel);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DAQstop(self, channel) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_AIN_DAQstop(self._SD_Object__handle, channel);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DAQflush(self, channel) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_AIN_DAQflush(self._SD_Object__handle, channel);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DAQtrigger(self, channel) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_AIN_DAQtrigger(self._SD_Object__handle, channel);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DAQstartMultiple(self, channel) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_AIN_DAQstartMultiple(self._SD_Object__handle, channel);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DAQstopMultiple(self, channel) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_AIN_DAQstopMultiple(self._SD_Object__handle, channel);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DAQflushMultiple(self, channel) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_AIN_DAQflushMultiple(self._SD_Object__handle, channel);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DAQtriggerMultiple(self, channel) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_AIN_DAQtriggerMultiple(self._SD_Object__handle, channel);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DAQread(self, nDAQ, nPoints, timeOut = 0) :
		if self._SD_Object__handle > 0 :
			if nPoints > 0 :
				data = (c_short * nPoints)()

				nPoints = self._SD_Object__core_dll.SD_AIN_DAQread(self._SD_Object__handle, nDAQ, data, nPoints, timeOut)

				if nPoints > 0 :
					return np.array(data)
				else :
					return np.empty(0, dtype=np.short)
			else :
				return const.error.INVALID_VALUE
		else :
			return const.error.MODULE_NOT_OPENED

	def DAQcounterRead(self, nDAQ) :
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_AIN_DAQcounterRead(self._SD_Object__handle, nDAQ);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DAQbufferPoolConfig(self, nDAQ, nPoints, timeOut = 0):
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_AIN_DAQbufferPoolConfig(self._SD_Object__handle, nDAQ, c_void_p(0), nPoints, timeOut, c_void_p(0), c_void_p(0));
		else :
			return const.error.MODULE_NOT_OPENED;

	def DAQbufferPoolRelease(self, nDAQ):
		if self._SD_Object__handle > 0 :
			return self._SD_Object__core_dll.SD_AIN_DAQbufferPoolRelease(self._SD_Object__handle, nDAQ);
		else :
			return const.error.MODULE_NOT_OPENED;

	def DAQbufferGet(self, nDAQ):
		if self._SD_Object__handle > 0 :
			self._SD_Object__core_dll.SD_AIN_DAQbufferGet.restype = POINTER(c_short)
			error = c_int32()
			readPoints = c_int32()
			data = self._SD_Object__core_dll.SD_AIN_DAQbufferGet(self._SD_Object__handle, nDAQ, byref(readPoints), byref(error))
			error = error.value

			if error < 0 :
				return error
			else :
				nPoints = readPoints.value

				if nPoints > 0 :
					return  np.array(data)
				else :
					return np.empty(0, dtype=np.short)
		else :
			return const.error.MODULE_NOT_OPENED

	def FFT(self, channel, data, dB = False, windowType = 0) :
		error = const.error.INVALID_PARAMETERS

		if self._SD_Object__handle > 0 :
			if data is not None :
				size = len(data)

				if size > 0 :
					resultSize = int(ceil(pow(2, ceil(log(size, 2)))/2))
					dataC = (c_short * size)(*data)
					moduleC = (c_double * resultSize)()
					phaseC = (c_double * resultSize)()

					resultSize = self._SD_Object__core_dll.SD_AIN_FFT(self._SD_Object__handle, channel, dataC, size, moduleC, resultSize, phaseC, dB, windowType)

					if resultSize > 0 :
						moduleData = np.array(moduleC)
						phaseData = np.array(phaseC)
					else :
						moduleData = np.empty(0, dtype=np.double)
						phaseData = np.empty(0, dtype=np.double)

					return (moduleData, phaseData)
		else :
			error = const.error.MODULE_NOT_OPENED

		return error

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
