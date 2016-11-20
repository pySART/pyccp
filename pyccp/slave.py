#!/usr/bin/env python
# -*- coding: utf-8 -*-

__copyright__="""
    pySART - Simplified AUTOSAR-Toolkit for Python.

   (C) 2009-2016 by Christoph Schueler <cpu12.gems@googlemail.com>

   All Rights Reserved

  This program is free software; you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation; either version 2 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License along
  with this program; if not, write to the Free Software Foundation, Inc.,
  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""

from collections import namedtuple
import enum
from pprint import pprint
import struct

from pyccp import ccp
from pyccp.logger import Logger


class Slave(object):

    def __init__(self, transport, memory):
        self.transport = transport
        self.transport.parent = self
        self._mta = 0x0000
        self.ctr = 0x00
        self.logger = Logger("pyccp.slave")

    def receive(self, cmo):
        """
        :param cmo: CAN Message Object
        :type cmo: `CANMessageObject`
        """
        print("Received: {}".format(cmo))
        self.logger.debug("Received: {}".format(cmo))
        self.commandHandler(cmo)

    def commandHandler(self, cmo):
        cmd = cmo.data[0]
        payload = cmo.data[ 1 : ]
        handler = self.COMMAND_HANDLERS.get(cmd, None)
        if handler:
            handler(self, payload)
        else:
            pass # TODO: CCP error handling.

    def onConnect(self, payload):
        self.logger.debug("onConnect")
        print("connecting", payload)

    def onGetCCPVersion(self, payload):
        self.logger.debug("onGetCCPVersion")

    def onTest(self, payload):
        self.logger.debug("onTest")

    def onExchangeId(self, payload):
        self.logger.debug("onExchangeId")

    def onSetMta(self, payload):
        self.logger.debug("onSetMta")

    def onDnload(self, payload):
        self.logger.debug("onDnload")

    def onDnload6(self, payload):
        self.logger.debug("onDnload6")

    def onUpload(self, payload):
        self.logger.debug("onUpload")

    def onShortUp(self, payload):
        """
        0xff    0x00 0x23 0x10 0x11 0x12 0x13
        """
        self.logger.debug("onShortUp")

    def onGetDaqSize(self, payload):
        self.logger.debug("onGetDaqSize")

    def onSetDaqPtr(self, payload):
        self.logger.debug("onSetDaqPtr")

    def onWriteDaq(self, payload):
        self.logger.debug("onWriteDaq")

    def onStartStopAll(self, payload):
        self.logger.debug("onStartStopAll")

    def onStartStop(self, payload):
        self.logger.debug("onStartStop")

    def onDisconnect(self, payload):
        self.logger.debug("onDisconnect")

    def onSetSStatus(self, payload):
        self.logger.debug("onSetSStatus")

    def onGetSStatus(self, payload):
        self.logger.debug("onGetSStatus")

    def onBuildChksum(self, payload):
        self.logger.debug("onBuildChksum")

    def onClearMemory(self, payload):
        self.logger.debug("onClearMemory")

    def onProgram(self, payload):
        self.logger.debug("onProgram")

    def onProgram6(self, payload):
        self.logger.debug("onProgram6")

    def onMove(self, payload):
        self.logger.debug("onMove")

    def onGetActiveCalPage(self, payload):
        self.logger.debug("onGetActiveCalPage")

    def onSelectCalPage(self, payload):
        self.logger.debug("onSelectCalPage")

    def onUnlock(self, payload):
        self.logger.debug("onUnlock")

    def onGetSeed(self, payload):
        self.logger.debug("onGetSeed")

    COMMAND_HANDLERS = {
        ccp.CommandCodes.CONNECT: onConnect,
        ccp.CommandCodes.GET_CCP_VERSION: onGetCCPVersion,
        ccp.CommandCodes.TEST: onTest,
        ccp.CommandCodes.EXCHANGE_ID:  onExchangeId,
        ccp.CommandCodes.SET_MTA: onSetMta,
        ccp.CommandCodes.DNLOAD: onDnload,
        ccp.CommandCodes.DNLOAD_6: onDnload6,
        ccp.CommandCodes.UPLOAD: onUpload,
        ccp.CommandCodes.SHORT_UP: onShortUp,
        ccp.CommandCodes.GET_DAQ_SIZE: onGetDaqSize,
        ccp.CommandCodes.SET_DAQ_PTR: onSetDaqPtr,
        ccp.CommandCodes.WRITE_DAQ: onWriteDaq,
        ccp.CommandCodes.START_STOP_ALL: onStartStopAll,
        ccp.CommandCodes.START_STOP: onStartStop,
        ccp.CommandCodes.DISCONNECT: onDisconnect,
        ccp.CommandCodes.SET_S_STATUS: onSetSStatus,
        ccp.CommandCodes.GET_S_STATUS: onGetSStatus,
        ccp.CommandCodes.BUILD_CHKSUM: onBuildChksum,
        ccp.CommandCodes.CLEAR_MEMORY: onClearMemory,
        ccp.CommandCodes.PROGRAM: onProgram,
        ccp.CommandCodes.PROGRAM_6: onProgram6,
        ccp.CommandCodes.MOVE: onMove,
        ccp.CommandCodes.GET_ACTIVE_CAL_PAGE: onGetActiveCalPage,
        ccp.CommandCodes.SELECT_CAL_PAGE: onSelectCalPage,
        ccp.CommandCodes.UNLOCK: onUnlock,
        ccp.CommandCodes.GET_SEED: onGetSeed,
    }

transport = ccp.Transport()
memory = ccp.Memory()
slave = Slave(transport, memory)
