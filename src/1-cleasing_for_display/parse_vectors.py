#!/usr/bin/env python
 
 
__author__ = "Mari Wahl"
__copyright__ = "Copyright 2014, The Cogent Project"
__credits__ = ["Mari Wahl"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"



import math
import os
from collections import defaultdict
from constants import SUBFOLDERS, FEATURES  



def parse_feature_vector(fraw):
    '''
        Create dictionary of features
    '''
    d = defaultdict(dict)
    for line in open(fraw,'r'):
        line = line.strip('\n')
        linea = line.split(': ')
        if linea[0] != ''  and len(linea)>1 and  linea[1][0] != '[' and not math.isnan(float(linea[1])):
            d[linea[0]] = linea[1]

    return d


def save_vectors(d, output):
    '''
        Salve output vector
    '''
    with open(output, "a") as f:
        if d:
            for feat in FEATURES:
                value = d[feat]
                if value:
                    f.write( value)
                else:
                    f.write( '-')
                if feat != FEATURES[-1]:
                    f.write( ',')
        f.write('\n')


def create_input_files(subfolder):
    return '../../data/' +  subfolder + '/'



def create_output_files(subfolder):

    out = '../../output/'
    if not os.path.exists(out):
        os.makedirs(out) 
    out_v = out + 'vectors_disp/'      
    if not os.path.exists(out_v):
        os.makedirs(out_v)     
    return out_v + subfolder +'.data'




if __name__ == '__main__':

    # Loop saving the values for each file
    for subfolder in SUBFOLDERS:
            
        # make output/input file path and create output folders
        input_file  = create_input_files(subfolder)
        output_file = create_output_files(subfolder)

        # create the vector file and save some label info
        with open(output_file, "w") as f:
            f.write('#')
            for feat in FEATURES:
                f.write(feat + ' ')
            f.write('\n')            
            

        print 'Processing ' + input_file + ' ...'
        for fraw in os.listdir(input_file):
            # get dictionary of values
            dic = parse_feature_vector(input_file + fraw)

            # save the dictionary in files
            save_vectors(dic, output_file)

          
    print '\nDone!!!'
