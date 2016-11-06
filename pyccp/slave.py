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

    def __init__(self):
        self._mta = 0x0000

    def onConnect(self):
        pass

    def onTest(self):
        pass

    def OnExchangeId(self):
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

