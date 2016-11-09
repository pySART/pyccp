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


class Slave(object):

    def __init__(self, transport, memory):
        self.transport = transport
        self._mta = 0x0000
        self.ctr = 0x00

    def receive(self, cmo):
        """
        :param cmo: CAN Message Object
        :type cmo: `CANMessageObject`
        """
        pass

    def onConnect(self):
        pass

    def onTest(self):
        pass

    def onExchangeId(self):
        pass

    def onSetMta(self):
        pass

    def onDnload(self):
        pass

    def onDnload6(self):
        pass

    def onUpload(self):
        pass

    def onShortUp(self):
        """
        0xff    0x00 0x23 0x10 0x11 0x12 0x13
        """
        pass

    def onGetDaqSize(self):
        pass

    def onSetDaqPtr(self):
        pass

    def onWriteDaq(self):
        pass

    def onStartStopAll(self):
        pass

    def onStartStop(self):
        pass

    def onDisconnect(self):
        pass

    def onSetSStatus(self):
        pass

    def onGetSStatus(self):
        pass

    def onBuildChksum(self):
        pass

    def onClearMemory(self):
        pass

    def onProgram(self):
        pass

    def onProgram6(self):
        pass

    def onMove(self):
        pass

    def onGetActiveCalPage(self):
        pass

    def onSelectCalPage(self):
        pass

    def onUnlock(self):
        pass

    def onGetSeed(self):
        pass

    CALLBACKS = {
        ccp.CommandCodes.CONNECT: onConnect,
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
slave = Slave(transport)
