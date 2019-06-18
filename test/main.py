import sys
import unittest
import os

sys.path.append('.')
from subfiles import get_subfiles

class TestSubfiles(unittest.TestCase):
    def test_get_subfiles(self):
        subfiles = get_subfiles()

        this_pass = False

        for subfile in subfiles:
            if os.path.isfile(subfile):
                this_pass = True
            else: 
                this_pass = False
                break

        self.assertTrue(this_pass)

        

if __name__ == '__main__':
    unittest.main()