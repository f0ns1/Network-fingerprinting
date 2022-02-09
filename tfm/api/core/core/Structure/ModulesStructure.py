#!/usr/bin/python3

from abc import ABC, abstractmethod

class Module(ABC):

    def __init__(self, target, ports):
        self.target=target
        self.ports= ports
        super().__init__()

    @abstractmethod
    def do_scan(self):
        pass

    @abstractmethod
    def do_response(self):
        pass

    @abstractmethod
    def do_not_response(self):
        pass