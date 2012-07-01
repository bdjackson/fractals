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

# -----------------------------------------------------------------------------
def draw_fractal(in_file_name):
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    in_file = open('%s.p' % in_file_name, 'rb')
    fractal_data = pickle.load(in_file)
    in_file.close()

    print 'data:'
    print fractal_data['data']
    print type(fractal_data['data'])
    print '--------------------------------'

    im = plt.imshow( fractal_data['data']
                   , extent = [ fractal_data['x_min']
                              , fractal_data['x_max']
                              , fractal_data['y_min']
                              , fractal_data['y_max']
                              ]
                   )
    plt.axis('off')
    plt.savefig('%s_default.png' % in_file_name)
    # plt.show()

    im = plt.imshow( fractal_data['data']
                   , extent = [ fractal_data['x_min']
                              , fractal_data['x_max']
                              , fractal_data['y_min']
                              , fractal_data['y_max']
                              ]
                   , cmap=cm.gray
                   )
    plt.axis('off')
    plt.savefig('%s_gray.png' % in_file_name)

    im = plt.imshow( fractal_data['data']
                   , extent = [ fractal_data['x_min']
                              , fractal_data['x_max']
                              , fractal_data['y_min']
                              , fractal_data['y_max']
                              ]
                   , cmap=cm.hot
                   )
    plt.axis('off')
    plt.savefig('%s_hot.png' % in_file_name)

    im = plt.imshow( fractal_data['data']
                   , extent = [ fractal_data['x_min']
                              , fractal_data['x_max']
                              , fractal_data['y_min']
                              , fractal_data['y_max']
                              ]
                   , cmap=cm.winter
                   )
    plt.axis('off')
    plt.savefig('%s_winter.png' % in_file_name)

    im = plt.imshow( fractal_data['data']
                   , extent = [ fractal_data['x_min']
                              , fractal_data['x_max']
                              , fractal_data['y_min']
                              , fractal_data['y_max']
                              ]
                   , cmap=cm.summer
                   )
    plt.axis('off')
    plt.savefig('%s_summer.png' % in_file_name)

    im = plt.imshow( fractal_data['data']
                   , extent = [ fractal_data['x_min']
                              , fractal_data['x_max']
                              , fractal_data['y_min']
                              , fractal_data['y_max']
                              ]
                   , cmap=cm.autumn
                   )
    plt.axis('off')
    plt.savefig('%s_autumn.png' % in_file_name)

    im = plt.imshow( fractal_data['data']
                   , extent = [ fractal_data['x_min']
                              , fractal_data['x_max']
                              , fractal_data['y_min']
                              , fractal_data['y_max']
                              ]
                   , cmap=cm.spring
                   )
    plt.axis('off')
    plt.savefig('%s_spring.png' % in_file_name)

    im = plt.imshow( fractal_data['data']
                   , extent = [ fractal_data['x_min']
                              , fractal_data['x_max']
                              , fractal_data['y_min']
                              , fractal_data['y_max']
                              ]
                   , cmap=cm.spectral
                   )
    plt.axis('off')
    plt.savefig('%s_spectral.png' % in_file_name)

    im = plt.imshow( fractal_data['data']
                   , extent = [ fractal_data['x_min']
                              , fractal_data['x_max']
                              , fractal_data['y_min']
                              , fractal_data['y_max']
                              ]
                   , cmap=cm.bone
                   )
    plt.axis('off')
    plt.savefig('%s_bone.png' % in_file_name)

    im = plt.imshow( fractal_data['data']
                   , extent = [ fractal_data['x_min']
                              , fractal_data['x_max']
                              , fractal_data['y_min']
                              , fractal_data['y_max']
                              ]
                   , cmap=cm.cool
                   )
    plt.axis('off')
    plt.savefig('%s_cool.png' % in_file_name)

    im = plt.imshow( fractal_data['data']
                   , extent = [ fractal_data['x_min']
                              , fractal_data['x_max']
                              , fractal_data['y_min']
                              , fractal_data['y_max']
                              ]
                   , cmap=cm.copper
                   )
    plt.axis('off')
    plt.savefig('%s_copper.png' % in_file_name)

    im = plt.imshow( fractal_data['data']
                   , extent = [ fractal_data['x_min']
                              , fractal_data['x_max']
                              , fractal_data['y_min']
                              , fractal_data['y_max']
                              ]
                   , cmap=cm.hsv
                   )
    plt.axis('off')
    plt.savefig('%s_hsv.png' % in_file_name)

    im = plt.imshow( fractal_data['data']
                   , extent = [ fractal_data['x_min']
                              , fractal_data['x_max']
                              , fractal_data['y_min']
                              , fractal_data['y_max']
                              ]
                   , cmap=cm.jet
                   )
    plt.axis('off')
    plt.savefig('%s_jet.png' % in_file_name)

    im = plt.imshow( fractal_data['data']
                   , extent = [ fractal_data['x_min']
                              , fractal_data['x_max']
                              , fractal_data['y_min']
                              , fractal_data['y_max']
                              ]
                   , cmap=cm.pink
                   )
    plt.axis('off')
    plt.savefig('%s_pink.png' % in_file_name)

# -----------------------------------------------------------------------------
def main():
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # draw_fractal('mand_full_low')
    # draw_fractal('mand_top_low')
    # draw_fractal('mand_valley_low')
    draw_fractal('mand_full')
    draw_fractal('mand_top')
    draw_fractal('mand_valley')

# =============================================================================
if __name__ == '__main__':
    main()
