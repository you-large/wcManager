#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Only python3.x

"""

import sys
import argparse
import pandas as pd
from enum import Enum

class workMode(Enum):
    """
    define work mode
    """
    #通常動作
    NORMAL = 0

    #データベース初期化
    INITILIZE = 1

    #fixモード
    FIX = 2
    

def parseArgs(argv):
    """
    parse args
    """
    parser = argparse.ArgumentParser(description='Work time Manager.')
    parser.add_argument('--fix',  dest='fix', action='store_true',
                        default=False,
                        help='work fix mode')
    parser.add_argument('--initialize', dest='init',action='store_true',
                        default=False, help='initialize Database')
    # set args daringly to use unittest this function
    args = parser.parse_args(args=argv)

    if args.init == True:
        mode = workMode.INITILIZE
    elif args.fix == True:
        mode = workMode.FIX
    else:
        mode = workMode.NORMAL
        
    return mode

def initializeMode():
    result = input('初期化してもよいですか？(Y/N): ')
    if(result in {'y','yes','Y','Yes','YES'}):
        print('データベースを初期化します')
        data = pd.DataFrame(columns=['ID','作業名','PJ','種別'])
        data.to_csv('manage_data.csv',index=None)
        print('データベースを初期化しました')
    else:
        print('初期化を実施しませんでした')


def main():

    mode = parseArgs(sys.argv[1:])

    if(mode == workMode.FIX):
        # fix mode
        pass
    elif (mode == workMode.INITILIZE):
        initializeMode()
        quit()
    else:
        # normal mode
        pass

if __name__ == '__main__':
    main()
