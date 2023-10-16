from pyevsim import BehaviorModelExecutor, SystemSimulator, Infinite
from pyevsim.system_message import SysMessage

from basicPeriodicTemplate import BasicPeriodicTemplate
import datetime

from abc import abstractmethod

class basicPeriodic(BasicPeriodicTemplate):
    def __init__(self, i_time, d_time, name, ename, freq):
        super().__init__(i_time, d_time, name, ename, freq)

    def ext_action(self, port):
        pass

    def out_action(self):
        pass
    
    def int_action(self):
        pass