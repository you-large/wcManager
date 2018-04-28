#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Only python3.x

"""

import sys
import pyperclip
import argparse
import pandas as pd

class WCText:
    def __init__(self):
        self.Text1 = '　　・作業名　xxh(hh:mm-hh:mm)'
        

    def getText(self,level):
        print(level)
        
        if(level == 0):
            ret = self.Text1
        else:
            ret =  None
            
        return ret

    
    

def parseArgs(argv):
    """
    parse args
    """
    parser = argparse.ArgumentParser(description='Work time Text Paster.')
    parser.add_argument('-l',  dest='level', type=int,
                        help='text level')
    # set args daringly to use unittest this function
    args = parser.parse_args(args=argv)

    mode = args.level
        
    return mode


def main():

    mode = parseArgs(sys.argv[1:])

    if(mode == None):
        print('set option -l and text number')
        quit()
        
    cl = WCText()    
    text = cl.getText(mode)
    
    if(text != None):
        pyperclip.copy(text)

if __name__ == '__main__':
    main()
