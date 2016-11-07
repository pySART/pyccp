#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from pyccp import ccp
from pyccp.master import Master

class TestMaster(unittest.TestCase):

    def setUp(self):
        transport = ccp.Transport()
        self.master = Master(transport)
        self.master.ctr = 0x27

    def tearDown(self):
        del self.master

    def runTest(self, func, expectedResult, *params):
        getattr(self.master, func)(*params)
        result = str(self.master.transport.message)
        self.assertEqual(result, expectedResult)

    def testConnect(self):
        self.runTest("connect", "07E1  01 27 39 00 00 00 00 00", 0x7E1, 0x39)

    def testGetCCPVersion(self):
        self.runTest("getCCPVersion", "07E1  1B 27 02 01 00 00 00 00", 0x7E1)

    def testExchangeID(self):
        self.runTest("exchangeId", "07E1  17 27 00 00 00 00 00 00", 0x7E1)

    def testSetMta(self):
        self.runTest("setMta", "07E1  02 27 00 02 34 00 20 00", 0x7E1, 0x34002000, 0x02, 0x00)

    def testDnload(self):
        self.runTest("dnload", "07E1  03 27 05 10 11 12 13 14", 0x7e1, 5, bytearray([0x10, 0x11, 0x12, 0x13, 0x14]))

    def testUpload(self):
        self.runTest("upload", "07E1  04 23 04 00 00 00 00 00", 0x7e1, 4)

    def testUpload(self):
        self.runTest("getDaqSize", "07E1  14 27 03 00 01 02 03 04", 0x7e1, 3, 0x01020304)

    def testSetDaqPtr(self):
        self.runTest("setDaqPtr", "07E1  15 27 03 05 02 00 00 00", 0x7e1, 3, 5, 2)

    def testWriteDaqPtr(self):
        self.runTest("writeDaq", "07E1  16 27 02 01 02 00 42 00", 0x7e1, 0x02, 0x01, 0x02004200)

    def testStartStopPtr(self):
        self.runTest("startStop", "07E1  06 27 01 03 07 02 00 01", 0x7e1, 0x01, 0x03, 0x07, 0x02, 0x01)

    def testDisconnect(self):
        self.runTest("disconnect", "07E1  07 27 00 00 08 02 00 00", 0x7e1, 0x00, 0x0208)

if __name__ == '__main__':
    unittest.main()

