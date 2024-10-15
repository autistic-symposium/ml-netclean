#!/usr/bin/env python


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


def save_vectors(d, output, network):
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
                    f.write( '0')
                f.write( ',')

            # Add the class label
            # 4 - bio, 2 - info, 3 - social, 1 - tech          
            if  network == 'atlas' or network == 'carbon' or network == 'cellular' or network == 'metabolic' or network == 'yeast':
                f.write('4')
            elif  network == 'auto' or network == 'road':
                f.write('1')
            elif  network == 'citation' or network == 'collaboration' or network == 'communication' or network == 'p2p' or network == 'products' or network == 'webgraphs' or network == 'wiki':
                f.write('2')
            elif  network == 'ground' or network == 'location' or network == 'social':
                f.write('3')
               
        f.write('\n')



def create_input_files(subfolder):
    return '../../data/' +  subfolder + '/'



def create_output_files(subfolder):

    out = '../../output/'
    if not os.path.exists(out):
        os.makedirs(out) 
    out_v = out + 'vectors_proc/'      
    if not os.path.exists(out_v):
        os.makedirs(out_v)     
    return out_v + subfolder +'.data'




if __name__ == '__main__':

    # Loop saving the values for each file
    for subfolder in SUBFOLDERS:
            
        # make output/input file path and create output folders
        input_file  = create_input_files(subfolder)
        output_file = create_output_files(subfolder)


        print 'Processing ' + input_file + ' ...'
        for fraw in os.listdir(input_file):
            # get dictionary of values
            dic = parse_feature_vector(input_file + fraw)

            # save the dictionary in files
            save_vectors(dic, output_file, subfolder)

          
    print '\nDone!!!'
