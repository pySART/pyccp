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
        cmd = cmo.data[0]
        self.COMMAND_HANDLERS[cmd](self)
        #print("Command-Handler: {}".format(self.COMMAND_HANDLERS[cmd]))

    def onConnect(self):
        self.logger.debug("onConnect")

    def onGetCCPVersion(self):
        self.logger.debug("onGetCCPVersion")

    def onTest(self):
        self.logger.debug("onTest")

    def onExchangeId(self):
        self.logger.debug("onExchangeId")

    def onSetMta(self):
        self.logger.debug("onSetMta")

    def onDnload(self):
        self.logger.debug("onDnload")

    def onDnload6(self):
        self.logger.debug("onDnload6")

    def onUpload(self):
        self.logger.debug("onUpload")

    def onShortUp(self):
        """
        0xff    0x00 0x23 0x10 0x11 0x12 0x13
        """
        self.logger.debug("onShortUp")

    def onGetDaqSize(self):
        self.logger.debug("onGetDaqSize")

    def onSetDaqPtr(self):
        self.logger.debug("onSetDaqPtr")

    def onWriteDaq(self):
        self.logger.debug("onWriteDaq")

    def onStartStopAll(self):
        self.logger.debug("onStartStopAll")

    def onStartStop(self):
        self.logger.debug("onStartStop")

    def onDisconnect(self):
        self.logger.debug("onDisconnect")

    def onSetSStatus(self):
        self.logger.debug("onSetSStatus")

    def onGetSStatus(self):
        self.logger.debug("onGetSStatus")

    def onBuildChksum(self):
        self.logger.debug("onBuildChksum")

    def onClearMemory(self):
        self.logger.debug("onClearMemory")

    def onProgram(self):
        self.logger.debug("onProgram")

    def onProgram6(self):
        self.logger.debug("onProgram6")

    def onMove(self):
        self.logger.debug("onMove")

    def onGetActiveCalPage(self):
        self.logger.debug("onGetActiveCalPage")

    def onSelectCalPage(self):
        self.logger.debug("onSelectCalPage")

    def onUnlock(self):
        self.logger.debug("onUnlock")

    def onGetSeed(self):
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
