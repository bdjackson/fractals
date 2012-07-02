#!/usr/bin/env python
# =============================================================================

import sys
import os.path
import optparse
import time

import math
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
                , escape_radius
                ):
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        self.re = re
        self.im = im
        self.max_itr = max_itr
        self.escape_radius = escape_radius

        self.isInSet()

    # -----------------------------------------------------------------------------
    def isInSet(self):
        """
        """
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        itr = 0
        escaped = False

        z = complex(0., 0.)
        c = complex(self.re, self.im)

        while not escaped and itr < self.max_itr:
            itr += 1

            z *= z
            z += c

            if abs(z) > self.escape_radius:
                escaped = True

        self.in_set = not escaped
        self.escape_speed = -1
        self.normed_escape_speed = -1
        if escaped:
            self.escape_speed = itr
            self.normed_escape_speed = ( itr
                                       - ( math.log( math.log( abs(z) )
                                                   / math.log(self.escape_radius)
                                                   )
                                         / math.log(2)
                                         )
                                       )
            # print 're: %s\tim: %s\t|z|: %s\ti: %s\tnorm factor: %s' % \
            #         ( self.re
            #         , self.im
            #         , abs(z)
            #         , itr
            #         , ( math.log( math.log( abs(z) )
            #                     / math.log(self.escape_radius)
            #                     )
            #           / math.log(2)
            #           )
            #         )
            # print self.escape_radius - self.normed_escape_speed

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
                , escape_radius
                ):
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        print '------------------------------------------------------------------'
        print 'Generating Mandelbrot Set using:'
        print '\tx: [%s, %s] - res: %s' % (x_min, x_max, x_res)
        print '\ty: [%s, %s] - res: %s' % (y_min, y_max, y_res)
        print 'maximum iterations: %d' % max_itr

        self.x_res   = x_res
        self.x_min   = x_min
        self.x_max   = x_max
        self.y_res   = y_res
        self.y_min   = y_min
        self.y_max   = y_max
        self.max_itr = max_itr
        self.escape_radius = escape_radius

        self.x_pix = int(x_res*(x_max-x_min) + 1)
        self.y_pix = int(y_res*(y_max-y_min) + 1)

        self.x_points = [x_min + i/float(x_res) for i in xrange(self.x_pix)]
        self.y_points = [y_min + i/float(y_res) for i in xrange(self.y_pix, 0, -1)]
        # self.escape_speed        = np.zeros((self.y_pix, self.x_pix), int)
        self.escape_speed        = 0
        self.normed_escape_speed = np.zeros((self.y_pix, self.x_pix), float)

        total_pix = self.x_pix * self.y_pix
        one_percent_mark = int(total_pix / 100)
        next_milestone = 0
        processed_pix = 0
        for y_it, y in enumerate(self.y_points):
            for x_it, x in enumerate(self.x_points):
                mp = MandelbrotPoint(x, y, max_itr, escape_radius)

                if not mp.in_set:
                    # self.escape_speed[y_it][x_it] = mp.escape_speed
                    self.normed_escape_speed[y_it][x_it] = mp.normed_escape_speed
                # else:
                #     # self.escape_speed[y_it][x_it]        = 0
                #     self.normed_escape_speed[y_it][x_it] = 0

                processed_pix += 1
                # if (processed_pix%one_percent_mark) == 0:
                if processed_pix > next_milestone:
                    print 'Progress: %0.2f %%' % round(100*float(processed_pix)/total_pix)
                    next_milestone += one_percent_mark

    # -----------------------------------------------------------------------------
    def dump(self, out_file_name):
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        out_dict = { 'escape_speed':self.escape_speed
                   , 'normed_escape_speed':self.normed_escape_speed
                   , 'x_res':self.x_res
                   , 'x_min':self.x_min
                   , 'x_max':self.x_max
                   , 'y_res':self.y_res
                   , 'y_min':self.y_min
                   , 'y_max':self.y_max
                   , 'max_itr':self.max_itr
                   }
        out_file = open(out_file_name, 'wb')
        pickle.dump(out_dict, out_file)
        out_file.close()


# -----------------------------------------------------------------------------
def main():
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    if len(sys.argv) == 1:
        sys.argv.append('full')

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    for region in sys.argv[1:]:
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        if region == 'full':
            m = MandelbrotSet( x_res = 3000
            # m = MandelbrotSet( x_res = 100
                             # , x_min = -2
                             # , x_max = +0.8
                             , x_min = -3.0
                             , x_max = +1.8
                             , y_res = 3000
                             # , y_res = 100
                             # , y_min = -1.2
                             # , y_max = +1.2
                             , y_min = -1.5
                             , y_max = +1.5
                             , max_itr = 150
                             # , max_itr = 20
                             # , max_itr = 50
                             # , escape_radius = 2
                             , escape_radius = 1000
                             )
            m.dump('mand_full.p')

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        if region == 'top':
            m = MandelbrotSet( x_res = 7000
            # m = MandelbrotSet( x_res = 500
                             , x_min = -0.66
                             , x_max = +0.46
                             , y_res = 7000
                             # , y_res = 500
                             , y_min = +0.5
                             , y_max = +1.2
                             , max_itr = 250
                             # , max_itr = 20
                             # , max_itr = 50
                             # , escape_radius = 2
                             , escape_radius = 1000
                             )
            m.dump('mand_top.p')

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        if region == 'valley':
            m = MandelbrotSet( x_res = 40000
            # m = MandelbrotSet( x_res = 500
                             , x_min = -1.1
                             , x_max = -0.55
                             , y_res = 20000
                             # , y_res = 500
                             , y_min = +0.0
                             , y_max = +0.34375
                             , max_itr = 500
                             # , max_itr = 20
                             # , max_itr = 50
                             # , escape_radius = 2
                             , escape_radius = 1000
                             )
            m.dump('mand_valley.p')

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        if region == 'head':
            m = MandelbrotSet( x_res = 20000
            # m = MandelbrotSet( x_res = 1000
                             , x_min = -1.862
                             , x_max = -0.55
                             , y_res = 20000
                             # , y_res = 1000
                             , y_min = -0.41
                             , y_max = +0.41
                             , max_itr = 250
                             # , max_itr = 20
                             # , max_itr = 50
                             # , escape_radius = 2
                             , escape_radius = 1000
                             )
            m.dump('mand_head.p')

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        if region == 'satelite':
            # m = MandelbrotSet( x_res = 26000
            m = MandelbrotSet( x_res = 20000
            # m = MandelbrotSet( x_res = 1000
                             , x_min = -1.53
                             , x_max = -1.35
                             # , y_res = 26000
                             , y_res = 20000
                             # , y_res = 1000
                             , y_min = -0.055
                             , y_max = +0.055
                             # , max_itr = 250
                             , max_itr = 500
                             # , max_itr = 20
                             # , max_itr = 50
                             # , escape_radius = 2
                             , escape_radius = 1000
                             )
            m.dump('mand_satelite.p')

# =============================================================================
if __name__ == '__main__':
    main()
