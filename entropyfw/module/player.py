#!/usr/bin/python
# -*- coding: utf-8 -*-
from entropyfw.common.event import Event
from entropyfw.common.request import Request
import abc
__author__ = 'otger'


class Player(metaclass=abc.ABCMeta):
    def __init__(self, name):
        self.d = None
        self.name = name or self.name
        self._req_counter = 0

    def set_dealer(self, dealer):
        self.d = dealer
        self.d.add_player(self)

    def pub_event(self, event_id, value=None):
        event = Event(source=self.name, event_id=event_id, value=value)
        self.d.event(event)

    def request(self, target=None, command=None, arguments={}):
        self._req_counter += 1
        request = Request(command_id=self._req_counter,
                          source=self.name,
                          target=target,
                          command=command,
                          arguments=arguments)
        self.d.request(request)
        return request

    @abc.abstractmethod
    def check_event(self, event):
        """
        Module must check if it has a subscription to that event.
        If this is the case
        :param event:
        :return:
        """
        pass

    @abc.abstractmethod
    def check_request(self, request):
        """
        Module must implement a way to check if command of request is implemented
        :param request:
        :return:
        """
        pass