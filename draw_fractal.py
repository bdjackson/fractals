#!/usr/bin/env python
# =============================================================================

import sys
import os.path
import optparse
import time

import pickle
import math

import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# import numpy as np


# =============================================================================

def to_log_scale( fractal_data ):
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    for i in xrange(fractal_data['normed_escape_speed'].shape[0]):
        for j in xrange(fractal_data['normed_escape_speed'].shape[1]):
            if not fractal_data['normed_escape_speed'][i][j] == 0.:
                fractal_data['normed_escape_speed'][i][j] = math.log(fractal_data['normed_escape_speed'][i][j])

# -----------------------------------------------------------------------------
def draw_all_cmaps( fractal_data
                  , in_file_name
                  , algorithm
                  , algo_tag
                  ):
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # im = plt.imshow( fractal_data[algorithm]
    #                , extent = [ fractal_data['x_min']
    #                           , fractal_data['x_max']
    #                           , fractal_data['y_min']
    #                           , fractal_data['y_max']
    #                           ]
    #                )
    # plt.axis('off')
    # plt.savefig('%s_%s.png' % (in_file_name, algo_tag))

    im = plt.imshow( fractal_data[algorithm]
                   , extent = [ fractal_data['x_min']
                              , fractal_data['x_max']
                              , fractal_data['y_min']
                              , fractal_data['y_max']
                              ]
                   , cmap=cm.gray
                   )
    plt.axis('off')
    plt.savefig('%s_%s_gray.png' % (in_file_name, algo_tag))

    im = plt.imshow( fractal_data[algorithm]
                   , extent = [ fractal_data['x_min']
                              , fractal_data['x_max']
                              , fractal_data['y_min']
                              , fractal_data['y_max']
                              ]
                   , cmap=cm.hot
                   )
    plt.axis('off')
    plt.savefig('%s_%s_hot.png' % (in_file_name, algo_tag))

    im = plt.imshow( fractal_data[algorithm]
                   , extent = [ fractal_data['x_min']
                              , fractal_data['x_max']
                              , fractal_data['y_min']
                              , fractal_data['y_max']
                              ]
                   , cmap=cm.spectral
                   )
    plt.axis('off')
    plt.savefig('%s_%s_spectral.png' % (in_file_name, algo_tag))

    im = plt.imshow( fractal_data[algorithm]
                   , extent = [ fractal_data['x_min']
                              , fractal_data['x_max']
                              , fractal_data['y_min']
                              , fractal_data['y_max']
                              ]
                   , cmap=cm.bone
                   )
    plt.axis('off')
    plt.savefig('%s_%s_bone.png' % (in_file_name, algo_tag))

    im = plt.imshow( fractal_data[algorithm]
                   , extent = [ fractal_data['x_min']
                              , fractal_data['x_max']
                              , fractal_data['y_min']
                              , fractal_data['y_max']
                              ]
                   , cmap=cm.copper
                   )
    plt.axis('off')
    plt.savefig('%s_%s_copper.png' % (in_file_name, algo_tag))

    im = plt.imshow( fractal_data[algorithm]
                   , extent = [ fractal_data['x_min']
                              , fractal_data['x_max']
                              , fractal_data['y_min']
                              , fractal_data['y_max']
                              ]
                   , cmap=cm.jet
                   )
    plt.axis('off')
    plt.savefig('%s_%s_jet.png' % (in_file_name, algo_tag))

    # im = plt.imshow( fractal_data[algorithm]
    #                , extent = [ fractal_data['x_min']
    #                           , fractal_data['x_max']
    #                           , fractal_data['y_min']
    #                           , fractal_data['y_max']
    #                           ]
    #                , cmap=cm.winter
    #                )
    # plt.axis('off')
    # plt.savefig('%s_%s_winter.png' % (in_file_name, algo_tag))

    # im = plt.imshow( fractal_data[algorithm]
    #                , extent = [ fractal_data['x_min']
    #                           , fractal_data['x_max']
    #                           , fractal_data['y_min']
    #                           , fractal_data['y_max']
    #                           ]
    #                , cmap=cm.summer
    #                )
    # plt.axis('off')
    # plt.savefig('%s_%s_summer.png' % (in_file_name, algo_tag))

    # im = plt.imshow( fractal_data[algorithm]
    #                , extent = [ fractal_data['x_min']
    #                           , fractal_data['x_max']
    #                           , fractal_data['y_min']
    #                           , fractal_data['y_max']
    #                           ]
    #                , cmap=cm.autumn
    #                )
    # plt.axis('off')
    # plt.savefig('%s_%s_autumn.png' % (in_file_name, algo_tag))

    # im = plt.imshow( fractal_data[algorithm]
    #                , extent = [ fractal_data['x_min']
    #                           , fractal_data['x_max']
    #                           , fractal_data['y_min']
    #                           , fractal_data['y_max']
    #                           ]
    #                , cmap=cm.spring
    #                )
    # plt.axis('off')
    # plt.savefig('%s_%s_spring.png' % (in_file_name, algo_tag))

    # im = plt.imshow( fractal_data[algorithm]
    #                , extent = [ fractal_data['x_min']
    #                           , fractal_data['x_max']
    #                           , fractal_data['y_min']
    #                           , fractal_data['y_max']
    #                           ]
    #                , cmap=cm.cool
    #                )
    # plt.axis('off')
    # plt.savefig('%s_%s_cool.png' % (in_file_name, algo_tag))

    # im = plt.imshow( fractal_data[algorithm]
    #                , extent = [ fractal_data['x_min']
    #                           , fractal_data['x_max']
    #                           , fractal_data['y_min']
    #                           , fractal_data['y_max']
    #                           ]
    #                , cmap=cm.hsv
    #                )
    # plt.axis('off')
    # plt.savefig('%s_%s_hsv.png' % (in_file_name, algo_tag))

    # im = plt.imshow( fractal_data[algorithm]
    #                , extent = [ fractal_data['x_min']
    #                           , fractal_data['x_max']
    #                           , fractal_data['y_min']
    #                           , fractal_data['y_max']
    #                           ]
    #                , cmap=cm.pink
    #                )
    # plt.axis('off')
    # plt.savefig('%s_%s_pink.png' % (in_file_name, algo_tag))
    

# -----------------------------------------------------------------------------
def draw_fractal(in_file_name):
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    plt.figure(figsize=[28.8, 18], dpi=100)
    plt.axes([0,0,1,1], frameon = True) 
    plt.axis('off')

    in_file = open('%s.p' % in_file_name, 'rb')
    fractal_data = pickle.load(in_file)
    in_file.close()

    draw_all_cmaps( fractal_data
                  , in_file_name
                  , algorithm = 'normed_escape_speed'
                  , algo_tag = 'norm'
                  )
    to_log_scale(fractal_data)
    draw_all_cmaps( fractal_data
                  , in_file_name
                  , algorithm = 'normed_escape_speed'
                  , algo_tag = 'norm_log'
                  )
    # draw_all_cmaps(fractal_data, in_file_name, norm=True)
    # draw_all_cmaps(fractal_data, in_file_name, norm=False)

# -----------------------------------------------------------------------------
def main():
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # print 'printing full mandelbrot set'
    # draw_fractal('mand_full')
    # print 'printing top portion of mandelbrot set'
    # draw_fractal('mand_top')
    # print 'printing valley region of mandelbrot set'
    # draw_fractal('mand_valley')
    # print 'printing head of mandelbrot set'
    # draw_fractal('mand_head')
    print 'printing satelite of mandelbrot set'
    draw_fractal('mand_satelite')

# =============================================================================
if __name__ == '__main__':
    main()
