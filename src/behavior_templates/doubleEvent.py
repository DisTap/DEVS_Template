from pyevsim import BehaviorModelExecutor, SystemSimulator, Infinite
from pyevsim.system_message import SysMessage

from doubleEventTemplate import doubleEventTemplate
import datetime

from abc import abstractmethod


class doubleEvent(doubleEventTemplate):
    def __init__(self, i_time, d_time, name, ename, freq):
        super().__init__(i_time, d_time, name, ename)

    def out_action(self):
        pass
    
    def int_action(self):
        pass

    @abstractmethod
    def ext_event1_action(self,msg):
        pass

    @abstractmethod
    def ext_event2_action(self,msg):
        pass