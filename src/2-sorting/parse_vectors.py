#!/usr/bin/env python
 
 
__author__ = "Mari Wahl"
__copyright__ = "Copyright 2014, The Cogent Project"
__credits__ = ["Mari Wahl"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"



import sys, os
from constants import SUBFOLDERS, FEATURES  



def save_vectors(output, lines):
    '''
        Salve output vector
    '''
    with open(output, "w") as f:
    	for l in lines:
            f.write(l)


def create_input_files(subfolder):
    return '../../output/vectors_proc/' + subfolder +'.data'



def create_output_files(subfolder):

    out = '../../output/'
    if not os.path.exists(out):
        os.makedirs(out) 
    out_v = out + 'vectors_sort/'      
    if not os.path.exists(out_v):
        os.makedirs(out_v)     
    return out_v + subfolder +'.data'




if __name__ == '__main__':

    # Loop saving the values for each file
    for subfolder in SUBFOLDERS:
            
        # make output/input file path and create output folders
        input_file  = create_input_files(subfolder)
        output_file = create_output_files(subfolder)

        print 'Sorting ' + input_file + ' ...'
        lines = open(input_file).readlines()
        lines.sort()
        save_vectors(output_file, lines)

          
    print '\nDone!!!'
