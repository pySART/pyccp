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


if __name__ == '__main__':
    unittest.main()

