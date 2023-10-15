from pyevsim import BehaviorModelExecutor, SystemSimulator, Infinite
from pyevsim.system_message import SysMessage

from eventTemplate import eventTemplate
import datetime

from abc import abstractmethod

class event(eventTemplate):
    def __init__(self, i_time, d_time, name, ename):
        super().__init__(i_time, d_time, name, ename)

    def ext_action(self, port):
        pass

    def out_action(self):
        pass
    
    def int_action(self):
        pass