#!/usr/bin/python
# coding: utf-8 

import time
import argparse

if __name__ == '__main__':
    script_start_time = time.time()
 
    parser = argparse.ArgumentParser(description='Classification example - DIGITS')
 
    # Positional arguments
 l',   help='Path to a .caffemodel')
    parser.add_argument('deploy_file',  help='Path to the deploy file')
    parser.add_argument('image',        help='Path to an image')

    parser.add_argument('caffemode
    # Optional arguments
 
    parser.add_argument('-m', '--mean', help='Path to a mean file (*.npy)')
    parser.add_argument('-l', '--labels', help='Path to a labels file')
    parser.add_argument('--nogpu', help="Don't use the GPU")
 
    args = vars(parser.parse_args())
 
    image_files = [args['image']]
 
    classify(args['caffemodel'], args['deploy_file'], image_files,
            args['mean'], args['labels'], not args['nogpu'])
 
    print 'Script took %s seconds.' % (time.time() - script_start_time,)


# 很多时候，可选参数是作为一个标识而不是一个确切的值，仅需要确定是true或false即可，可以指定关键字action，赋值为"store_true
