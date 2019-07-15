#!/usr/bin/env python3

import unittest
import ppcomponentparser

class PPResistorTest(unittest.TestCase):

    # Reading a TOML file should return a dict object
    def test_read_single_resistor(self):
        resfile = 'RES_10k_0.1%_63mW_0402_Thin_50ppm_-55-155C.toml'
        res = PPResistor(resfile)
        self.assertIsInstance(res.read_toml(), dict)


if __name__ == '__main__':
    unittest.main()
