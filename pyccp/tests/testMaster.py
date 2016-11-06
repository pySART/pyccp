#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from pyccp import ccp
from pyccp.master import Master

class TestMaster(unittest.TestCase):

    def testConnect(self):
        transport = ccp.Transport()
        master = Master(transport)
        master.ctr = 0x27
        master.connect(0x7E1, 0x39)
        self.assertEqual(str(master.transport.message), "07E1  01 27 39 00 00 00 00 00")

    def testGetCCPVersion(self):
        transport = ccp.Transport()
        master = Master(transport)
        master.ctr = 0x27
        master.getCCPVersion(0x7e1)
        self.assertEqual(str(master.transport.message), '07E1  1B 27 02 01 00 00 00 00')

    def testExchangeID(self):
        transport = ccp.Transport()
        master = Master(transport)
        master.ctr = 0x23
        master.exchangeId(0x7e1)
        self.assertEqual(str(master.transport.message), '07E1  17 23 00 00 00 00 00 00')

    def testSetMta(self):
        transport = ccp.Transport()
        master = Master(transport)
        master.ctr = 0x23
        master.setMta(0x7e1, 0x34002000, 0x02, 0x00)
        self.assertEqual(str(master.transport.message), '07E1  02 23 00 02 34 00 20 00')

    def testDnload(self):
        transport = ccp.Transport()
        master = Master(transport)
        master.ctr = 0x23
        master.dnload(0x7e1, 5, bytearray([0x10, 0x11, 0x12, 0x13, 0x14]))
        self.assertEqual(str(master.transport.message), '07E1  03 23 05 10 11 12 13 14')

    def testUpload(self):
        transport = ccp.Transport()
        master = Master(transport)
        master.ctr = 0x23
        master.upload(0x7e1, 4)
        self.assertEqual(str(master.transport.message), '07E1  04 23 04 00 00 00 00 00')

    def testUpload(self):
        transport = ccp.Transport()
        master = Master(transport)
        master.ctr = 0x23
        master.getDaqSize(0x7e1, 3, 0x01020304)
        self.assertEqual(str(master.transport.message), '07E1  14 23 03 00 01 02 03 04')

    def testSetDaqPtr(self):
        transport = ccp.Transport()
        master = Master(transport)
        master.ctr = 0x23
        master.setDaqPtr(0x7e1, 3, 5, 2)
        self.assertEqual(str(master.transport.message), '07E1  15 23 03 05 02 00 00 00')

    def testWriteDaqPtr(self):
        transport = ccp.Transport()
        master = Master(transport)
        master.ctr = 0x23
        master.writeDaq(0x7e1, 0x02, 0x01, 0x02004200)
        self.assertEqual(str(master.transport.message), '07E1  16 23 02 01 02 00 42 00')

    def testStartStopPtr(self):
        transport = ccp.Transport()
        master = Master(transport)
        master.ctr = 0x23
        master.startStop(0x7e1, 0x01, 0x03, 0x07, 0x02, 0x01)
        self.assertEqual(str(master.transport.message), '07E1  06 23 01 03 07 02 00 01')

    def testDisconnect(self):
        transport = ccp.Transport()
        master = Master(transport)
        master.ctr = 0x23
        master.disconnect(0x7e1, 0x00, 0x0208)
        self.assertEqual(str(master.transport.message), '07E1  07 23 00 00 08 02 00 00')

if __name__ == '__main__':
    unittest.main()

