#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from pyccp import ccp
from pyccp.slave import Slave


def createMessageObject(message):
    values = [int(x, 16) for x in message.split()]
    cmo = ccp.CANMessageObject(values[0], 8, values[ 1 : ])
    return cmo
    return values

STATION_ADDRESS = 0x39

class TestSlave(unittest.TestCase):

    def setUp(self):
        transport = ccp.MockTransport()
        memory = ccp.Memory()
        self.slave = Slave(STATION_ADDRESS, transport, memory)
        self.slave.logger.setLevel("DEBUG")

    def tearDown(self):
        del self.slave

    def runTest(self, func, message, expectedResult, *params):
        cmo = createMessageObject(message)
        self.slave.receive(cmo)
        self.assertEqual(str(self.slave.transport.message), expectedResult)

    def testConnect(self):
        self.runTest("connect", "07E1  01 27 39 00 00 00 00 00", "0815  FF 00 27 00 00 00 00 00", 0x7E1, 0x39)

    def testGetCCPVersion(self):
        self.runTest("getCCPVersion", "07E1  1B 27 02 01 00 00 00 00", "0815  FF 00 27 02 01 00 00 00", 0x7E1)

    @unittest.skip
    def testExchangeID(self):
        self.runTest("exchangeId", "07E1  17 27 00 00 00 00 00 00", 0x7E1)


class TestUnconnectedServices(unittest.TestCase):
    pass


class TestConnectedServices(unittest.TestCase):
    pass


def main():
    unittest.main()

if __name__ == '__main__':
    main()

