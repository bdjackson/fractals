#!/usr/bin/env python
# =============================================================================

import sys
import os.path
import optparse
import time

import pickle

import matplotlib.cm as cm
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
                , fractal_data
                ):
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        self.data = fractal_data
        # print self.data
        self.im = plt.imshow( fractal_data['data']
                            , extent = [ fractal_data['x_min']
                                       , fractal_data['x_max']
                                       , fractal_data['y_min']
                                       , fractal_data['y_max']
                                       ]
                            # , extent=[data['x_min']
                            # , data['x_max']
                            # , data['y_min']
                            # , data['y_max']]
                            # , cmap=cm.Spectral
                            # , cmap=cm.Blues_r
                            # , cmap=cm.hot
                            )
        plt.show()

    # -----------------------------------------------------------------------------
    def drawSet(self, out_file_name):
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        pass

# -----------------------------------------------------------------------------
def main():
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    m = pickle.load(open('mand.p', 'rb'))


    fd = FractalDrawer(m)
    # fd.drawSet('fract.png')

# =============================================================================
if __name__ == '__main__':
    main()
