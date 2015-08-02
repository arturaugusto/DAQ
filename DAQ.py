__author__ = 'lighting'

from PyDAQmx import *
import numpy
import ctypes


class currentInput(Task):

    def __init__(self):
        Task.__init__(self)
        self.data = numpy.zeros(10)
        self.CreateAICurrentChan( b'cDAQ1Mod4/ai0',
                                  b'',
                                  DAQmx_Val_Cfg_Default,
                                  -0.02, 0.02,
                                  DAQmx_Val_Amps,
                                  DAQmx_Val_Default,
                                  249.0,
                                  None
                                  )
        self.CfgSampClkTiming(b'',10000.0,DAQmx_Val_Rising, DAQmx_Val_ContSamps,20)
        self.AutoRegisterEveryNSamplesEvent(DAQmx_Val_Acquired_Into_Buffer,10,0)
        self.AutoRegisterDoneEvent(0)

    def EveryNCallback(self):
        read = int32()
        self.ReadAnalogF64(10,10.0,DAQmx_Val_GroupByChannel,self.data,10,byref(read),None)
        return 0 # The function should return an integer

    def DoneCallback(self, status):

        return 0 # The function should return an integer

    def getResult(self):
        return numpy.average(self.data)


class voltageOutput(Task):

    def __init__(self):
        Task.__init__(self)
        self.CreateAOVoltageChan(b'cDAQ1Mod1/ao2',b'',0.0,10.0,DAQmx_Val_Volts,None)

    def voltOut(self,voltage):
        data = numpy.array([voltage,voltage],dtype = numpy.float64)
        self.WriteAnalogF64(2,1,10.0,DAQmx_Val_GroupByChannel,data,None,None)


if __name__ == '__main__':
    current_input = currentInput()
    current_input.StartTask()

    voltage_output = voltageOutput()
    voltage_output.voltOut(4.0)
    voltage_output.StopTask()

    print(current_input.getResult())
    current_input.StopTask()


