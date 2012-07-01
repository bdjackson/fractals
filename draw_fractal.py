#!/usr/bin/env python
# =============================================================================

import sys
import os.path
import optparse
import time

import pickle

from mandelbrot import *

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# import numpy as np


# =============================================================================

# =============================================================================
class FractalDrawer(object):
    """
    """
    # -----------------------------------------------------------------------------
    def __init__( self
                , mandelbrot_set
                ):
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        print mandelbrot_set
        # self.data = mandelbrot_set.data
        # print self.data

    # -----------------------------------------------------------------------------
    def drawSet(self, out_file_name):
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        pass

# -----------------------------------------------------------------------------
def main():
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    m = pickle.load(open('mand.p', 'rb'))

    fd = FractalDrawer(m)
    fd.drawSet('fract.png')

# =============================================================================
if __name__ == '__main__':
    main()
