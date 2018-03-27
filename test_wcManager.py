#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys
import wcManager


class TestWcManager(unittest.TestCase):
    def test_parseArgs_no_fix(self):
        """
        test for not '--fix'
        """
        
        argv = sys.argv.copy()
        fix = wcManager.parseArgs(argv[1:])
        self.assertEqual(wcManager.workMode.NORMAL, fix)

    def test_parseArgs_fix_mode(self):
        """
        test for '--fix'
        """
        argv = sys.argv.copy()
        argv.append('--fix')
        fix = wcManager.parseArgs(argv[1:])
        self.assertEqual(wcManager.workMode.FIX, fix)

    def test_parseArgs_init_mode(self):
        """
        test for '--initilize'
        """
        argv = sys.argv.copy()
        argv.append('--initialize')
        fix = wcManager.parseArgs(argv[1:])
        self.assertEqual(wcManager.workMode.INITILIZE, fix)
        

if __name__ == '__main__':
    unittest.main()
