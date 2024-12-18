# Copyright 2013 Numenta Inc.
#
# Copyright may exist in Contributors' modifications
# and/or contributions to the work.
#
# Use of this source code is governed by the MIT
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.

"""Unit tests for Cells4."""

import sys

import unittest2 as unittest

from nupic.math import lgamma

class LGammaTest(unittest.TestCase):


  @unittest.skipIf(sys.platform.startswith("win32"),
                   "Skipping failed test on Windows.")
  def testLgamma(self):
    items = (
      (0.1,  2.25271265),
      (0.2,  1.52406382),
      (0.3,  1.09579799),
      (0.4,  0.79667782),
      (0.5,  0.57236494),
      (0.6,  0.39823386),
      (0.7,  0.26086725),
      (0.8,  0.15205968),
      (0.9,  0.06637624),
      (1.0,  0.00000000),
      (1.1, -0.04987244),
      (1.2, -0.08537409),
      (1.3, -0.10817481),
      (1.4, -0.11961291),
      (1.5, -0.12078224),
      (1.6, -0.11259177),
      (1.7, -0.09580770),
      (1.8, -0.07108387),
      (1.9, -0.03898428),
      (2.0,  0.00000000),
      (2.1,  0.04543774),
      (2.2,  0.09694747),
      (2.3,  0.15418945),
      (2.4,  0.21685932),
      (2.5,  0.28468287),
      (2.6,  0.35741186),
      (2.7,  0.43482055),
      (2.8,  0.51670279),
      (2.9,  0.60286961),
      (3.0,  0.69314718),
    )
    for v, lg in items:
      print v, lg, lgamma(v)
      self.assertLessEqual(abs(lgamma(v) - lg), 1.0e-8,
                           "log Gamma(%f) = %f; lgamma(%f) -> %f" % (
                               v, lg, v, lgamma(v)))



if __name__ == "__main__":
  unittest.main()
