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


MTA0 = 0
MTA1 = 1

class Master(ccp.CRO):

    def __init__(self, transport):
        self.slaveConnections = {}
        self.transport = transport
        self.transport.parent = self
        self.ctr = 0x00
        self.logger = Logger("pyccp.master")

    def sendCRO(self, canID, cmd, ctr, b0 = 0, b1 = 0, b2 = 0, b3 = 0, b4 = 0, b5 = 0):
        """Transfer up to 6 data bytes from master to slave (ECU).
        """
        self.transport.send(canID, cmd, ctr, b0, b1, b2, b3, b4, b5)

    ##
    ## Mandatory Commands.
    ##
    def connect(self, canID, address):
        h = (address & 0xff00) >> 8
        l = address & 0x00ff
        self.sendCRO(canID, ccp.CommandCodes.CONNECT, self.ctr, l, h)

    def getCCPVersion(self, canID, major = 2, minor = 1):
        self.sendCRO(canID, ccp.CommandCodes.GET_CCP_VERSION, self.ctr, major, minor)

    def exchangeId(self, canID, b0 = 0, b1 = 0, b2 = 0, b3 = 0, b4 = 0, b5 = 0):
        self.sendCRO(canID, ccp.CommandCodes.EXCHANGE_ID, self.ctr, b0, b1, b2, b3, b4, b5)

    def setMta(self, canID, address, addressExtension = 0x00, mta = MTA0):
        address = struct.pack(">L", address)
        self.sendCRO(canID, ccp.CommandCodes.SET_MTA, self.ctr, mta, addressExtension, *address)

    def dnload(self, canID, size, data):
        self.sendCRO(canID, ccp.CommandCodes.DNLOAD, self.ctr, size, *data)

    def upload(self, canID, size):
        self.sendCRO(canID, ccp.CommandCodes.UPLOAD, self.ctr, size)

    def getDaqSize(self, canID, daqListNumber, address):
        address = struct.pack(">L", address)
        self.sendCRO(canID, ccp.CommandCodes.GET_DAQ_SIZE, self.ctr, daqListNumber, 0x00, *address)

    def setDaqPtr(self, canID, daqListNumber, odtNumber, elementNumber):
        self.sendCRO(canID, ccp.CommandCodes.SET_DAQ_PTR, self.ctr, daqListNumber, odtNumber, elementNumber)

    def writeDaq(self, canID, elementSize, addressExtension, address):
        address = struct.pack(">L", address)
        self.sendCRO(canID, ccp.CommandCodes.WRITE_DAQ, self.ctr, elementSize, addressExtension, *address)

    def startStop(self, canID, mode, daqListNumber, lastOdtNumber, eventChannel, ratePrescaler):
        ratePrescaler = struct.pack(">H", ratePrescaler)
        self.sendCRO(canID, ccp.CommandCodes.START_STOP, self.ctr, mode, daqListNumber, lastOdtNumber, eventChannel, *ratePrescaler)

    def disconnect(self, canID, permanent, address):
        address = struct.pack("<H", address)
        self.sendCRO(canID, ccp.CommandCodes.DISCONNECT, self.ctr, permanent, 0x00, *address)

    ##
    ## Optional Commands.
    ##
    def test(self, canID):
        pass

    def dnload6(self, canID):
        pass

    def shortUp(self, canID, size, address, addressExtension):
        pass

    def startStopAll(self, canID):
        pass

    def setSStatus(self, canID):
        pass

    def getSStatus(self, canID):
        pass

    def buildChksum(self, canID):
        pass

    def clearMemory(self, canID):
        pass

    def program(self, canID):
        pass

    def program6(self, canID):
        pass

    def move(self, canID):
        pass

    def getActiveCalPage(self, canID):
        pass

    def selectCalPage(self, canID):
        pass

    def unlock(self, canID):
        pass

    def getSeed(self, canID):
        pass

