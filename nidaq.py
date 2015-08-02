__author__ = 'lighting'

import ctypes
import numpy

# the typedefs
int32 = ctypes.c_long
uInt32 = ctypes.c_ulong
uInt64 = ctypes.c_ulonglong
float64 = ctypes.c_double
TaskHandle = uInt32
# the constants
DAQmx_Val_Cfg_Default = int32(-1)
DAQmx_Val_Amps = 10342
DAQmx_Val_Volts = 10348
DAQmx_Val_Rising = 10280
DAQmx_Val_Default = int32(-1)
DAQmx_Val_ContSamps = 10123
DAQmx_Val_FiniteSamps = 10178
DAQmx_Val_GroupByChannel = 0
DAQmx_Val_Acquired_Into_Buffer = 1

class current_input:

    def __init__(self, handle):
        self.nidaq = ctypes.windll.nicaiu
        self.taskHandle = TaskHandle(handle)
        self.nidaq.DAQmxCreateAICurrentChan(self.taskHandle,
                                            "cDAQ1Mod4/ai0",
                                            "",
                                            DAQmx_Val_Cfg_Default,
                                            float64(-0.02), float64(0.02),
                                            DAQmx_Val_Amps,
                                            DAQmx_Val_Default,
                                            float64(249.0),
                                            None
                                            )

