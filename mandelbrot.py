#!/usr/bin/env python
# =============================================================================

import sys
import os.path
import optparse
import time

import numpy as np

import pickle
# =============================================================================

# =============================================================================
class MandelbrotPoint(object):
    """
    determines if a point is in the mandelbrot set
    """
    # -----------------------------------------------------------------------------
    def __init__( self
                , re
                , im
                , max_itr
                ):
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        self.re = re
        self.im = im
        # self.point = np.complex(re, im)
        self.max_itr = max_itr

        self.escape_speed = self.findEscapeSpeed()

    # -----------------------------------------------------------------------------
    def findEscapeSpeed(self):
        """
        is this point in the mandelbrot set?
        if no, give escape speed, if yes, return -1
        """
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        itr = 0
        escaped = False

        z = complex(0., 0.)
        c = complex(self.re, self.im)

        while not escaped and itr < self.max_itr:
            itr += 1

            # print '============================'
            # print '%s + %s: ' % (z, c)
            z = z**2 + c

            # print '\t%s' % z
            if abs(z) > 2.:
                escaped = True

        escape_speed = -1
        if escaped:
            escape_speed = itr
        return escape_speed

# =============================================================================
class MandelbrotSet(object):
    """
    set of mandelbrot points
    """
    # -----------------------------------------------------------------------------
    def __init__( self
                , x_res
                , x_min
                , x_max
                , y_res
                , y_min
                , y_max
                , max_itr
                ):
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        self.x_res   = x_res
        self.x_min   = x_min
        self.x_max   = x_max
        self.y_res   = y_res
        self.y_min   = y_min
        self.y_max   = y_max
        self.max_itr = max_itr

        self.x_pix = int(x_res*(x_max-x_min) + 1)
        self.y_pix = int(y_res*(y_max-y_min) + 1)

        self.x_points = [x_min + i/float(x_res) for i in xrange(self.x_pix)]
        self.y_points = [y_min + i/float(y_res) for i in xrange(self.y_pix)]
        self.data = np.zeros((self.y_pix, self.x_pix), int)

        total_pix = self.x_pix * self.y_pix
        one_percent_mark = total_pix / 100
        processed_pix = 0
        for y_it, y in enumerate(self.y_points):
            for x_it, x in enumerate(self.x_points):
                # print 'y_it: %d -- x_it: %d' % (y_it, x_it)
                mp = MandelbrotPoint(x, y, max_itr)

                es = mp.escape_speed
                if not es == -1:
                    self.data[y_it][x_it] = es

                processed_pix += 1
                if processed_pix%one_percent_mark == 0:
                    print 'Progress: %0.2f %%' % (100*float(processed_pix)/total_pix)

    # -----------------------------------------------------------------------------
    def dump(self, out_file_name):
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        out_dict = { 'data':self.data
                   , 'x_res':self.x_res
                   , 'x_min':self.x_min
                   , 'x_max':self.x_max
                   , 'y_res':self.y_res
                   , 'y_min':self.y_min
                   , 'y_max':self.x_max
                   , 'max_itr':self.max_itr
                   }
        out_file = open(out_file_name, 'wb')
        pickle.dump(out_dict, out_file)
        out_file.close()


# -----------------------------------------------------------------------------
def main():
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    m = MandelbrotSet( x_res = 1000
                     , x_min = -2
                     , x_max = +0.8
                     , y_res = 1000
                     , y_min = -1.2
                     , y_max = +1.2
                     , max_itr = 75
                     )
    m.dump('mand.p')


# =============================================================================
if __name__ == '__main__':
    main()
