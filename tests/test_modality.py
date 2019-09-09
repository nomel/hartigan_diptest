from __future__ import unicode_literals
from __future__ import print_function

import time
import unittest

import numpy as np

from hartigan_diptest import dip


class testModality(unittest.TestCase):
    def setUp(self):
        self.data = np.random.randn(1000)

    def test_hartigan_diptest(self):
        t0 = time.time()
        dip(self.data)
        t1 = time.time()

        print("Hartigan diptest: {}".format(t1-t0))


if __name__ == '__main__':
    unittest.main()
