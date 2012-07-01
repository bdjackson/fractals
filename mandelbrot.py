#!/usr/bin/env python
# =============================================================================

import sys
import os.path
import optparse
import time

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
                , res
                , x_min
                , x_max
                , y_min
                , y_max
                , max_itr
                ):
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        self.res = res
        self.x_min  = x_min
        self.x_max  = x_max
        self.y_min  = y_min
        self.y_max  = y_max
        self.max_itr = max_itr

        self.x_pix = res*(x_max-x_min)
        self.y_pix = res*(y_max-y_min)

        self.x_points = [x_min + i*res for i in xrange(self.x_pix)]
        self.y_points = [y_min + i*res for i in xrange(self.y_pix)]

        self.mandelbrot_set = []
        self.data = []
        for x in self.x_points:
            self.data.append([])
            for y in self.y_points:
                mp = MandelbrotPoint(x, y, max_itr)
                self.mandelbrot_set.append(mp)
                self.data[-1].append([mp.re, mp.im, mp.escape_speed])

        # for mp in self.mandelbrot_set:
        #     print 're: %s - im: %s -- %s' % (mp.re, mp.im, mp.escape_speed)


# -----------------------------------------------------------------------------
def main():
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # m = MandelbrotSet(-2, 1, 100, -1, 1, 100, 100)
    # m = MandelbrotSet(-2, 1, 300, -1, 1, 200, 100)
    # m = MandelbrotSet(-2, 1, 300, -1, 1, 200, 1000)
    m = MandelbrotSet(100, -2, +1, -1, 1, 100)

    pickle.dump(m.data, open('mand.p', 'wb'))


# =============================================================================
if __name__ == '__main__':
    main()
