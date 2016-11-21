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


MAX_CTO = 0x0008
MAX_DTO = 0x0008

CCP_VERSION = (2, 1)

class CommandCodes(enum.IntEnum):

    # Mandatory Commands.
    CONNECT             = 0x01
    GET_CCP_VERSION     = 0x1B
    EXCHANGE_ID         = 0x17
    SET_MTA             = 0x02
    DNLOAD              = 0x03
    UPLOAD              = 0x04
    GET_DAQ_SIZE        = 0x14
    SET_DAQ_PTR         = 0x15
    WRITE_DAQ           = 0x16
    START_STOP          = 0x06
    DISCONNECT          = 0x07
    # Optional Commands.
    GET_SEED            = 0x12
    UNLOCK              = 0x13
    DNLOAD_6            = 0x23
    SHORT_UP            = 0x0F
    SELECT_CAL_PAGE     = 0x11
    SET_S_STATUS        = 0x0C
    GET_S_STATUS        = 0x0D
    BUILD_CHKSUM        = 0x0E
    CLEAR_MEMORY        = 0x10
    PROGRAM             = 0x18
    PROGRAM_6           = 0x22
    MOVE                = 0x19
    TEST                = 0x05
    GET_ACTIVE_CAL_PAGE = 0x09
    START_STOP_ALL      = 0x08
    DIAG_SERVICE        = 0x20
    ACTION_SERVICE      = 0x21


class ReturnCodes(enum.IntEnum):
    ACKNOWLEDGE                     = 0x00
    DAQ_PROCESSOR_OVERLOAD          = 0x01    # C0
    COMMAND_PROCESSOR_BUSY          = 0x10    # C1 NONE (wait until ACK or timeout)
    DAQ_PROCESSOR_BUSY              = 0x11    # C1 NONE (wait until ACK or timeout)
    INTERNAL_TIMEOUT                = 0x12    # C1 NONE (wait until ACK or timeout)
    KEY_REQUEST                     = 0x18    # C1 NONE (embedded seed&key)
    SESSION_STATUS_REQUEST          = 0x19    # C1 NONE (embedded SET_S_STATUS)
    COLD_START_REQUEST              = 0x20    # C2 COLD START
    CAL_DATA_INIT_REQUEST           = 0x21    # C2 cal. data initialization
    DAQ_LIST_INIT_REQUEST           = 0x22    # C2 DAQ list initialization
    CODE_UPDATE_REQUEST             = 0x23    # C2 (COLD START)
    UNKNOWN_COMMAND                 = 0x30    # C3 (FAULT)
    COMMAND_SYNTAX                  = 0x31    # C3 FAULT
    PARAMETER_OUT_OF_RANGE          = 0x32    # C3 FAULT
    ACCESS_DENIED                   = 0x33    # C3 FAULT
    OVERLOAD                        = 0x34    # C3 FAULT
    ACCESS_LOCKED                   = 0x35    # C3 FAULT
    RESOURCE_FUNCTION_NOT_AVAILABLE = 0x36    # C3 FAULT


class DTOType(enum.IntEnum):
    COMMAND_RETURN_MESSAGE  = 255
    EVENT_MESSAGE           = 254


class State(enum.IntEnum):
    pass


class CRO(object):
    """Command Receive Object.
    """


class DTO(object):
    """Data Transmission Object.
    """

    COMMAND_RETURN_MESSAGE  = 255
    EVENT_MESSAGE           = 254

    def send(self, pid, err, ctr, b0 = 0, b1 = 0, b2 = 0, b3 = 0, b4 = 0):
        """Transfer up to 5 data bytes from slave (ECU) to master.
        """
        pass


class CRM(DTO):
    """Command Return Message.
    """


class EVM(DTO):
    """Event Message.
    """


class DAQ(object):
    """Data Acquisition Message.
    """

    def send(self, pid, b0 = 0, b1 = 0, b2 = 0, b3 = 0, b4 = 0, b5 = 0, b6 = 0):
        """Transfer up to 7 data bytes from slave (ECU) to master.
        """
        pass


class ODT(object):
    """Object Descriptor Table.
    """


class DAQList(object):
    """Data Acquisition List.
    """
    """
    2401
    360a
    360b
    360c
    360d
    """

# File format not recognized.

class CANMessageObject(object):

    def __init__(self, canID, dlc, data, extendedAddr = False, rtr = False):
        self.canID = canID
        self.dlc = dlc
        self.data = data
        self.extendedAddr = extendedAddr
        self.rtr = rtr

    def __str__(self):
        addrFmt =  "[{:08X}]  " if self.extendedAddr else "{:04X}  "
        fmt = addrFmt + "{}"
        return fmt.format(self.canID, " ".join(["{:02X}".format(x) for x in self.data]))

    __repr__ = __str__


class Transport(object):

    def __init__(self):
        self.parent = None

    def send(self, canID, b0 = 0, b1 = 0, b2 = 0, b3 = 0, b4 = 0, b5 = 0, b6 = 0, b7 = 0):
        self.message = CANMessageObject(canID, 8, bytearray((b0, b1, b2, b3, b4, b5, b6, b7)))
        #print("Sending: {}".format(self.message))

    def receive(self, canID, b0 = 0, b1 = 0, b2 = 0, b3 = 0, b4 = 0, b5 = 0, b6 = 0, b7 = 0):
        self.message = CANMessageObject(canID, 8, bytearray((b0, b1, b2, b3, b4, b5, b6, b7)))
        self.parent.receive(self.message)

    def __str__(self):
        return "[Current Message]: {}".format(self.message)

    __repr__ = __str__


class Memory(object):

    def __init__(self):
        pass

