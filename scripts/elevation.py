#!/usr/bin/env python
import argparse
from planet import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('osmpath', help='output path')
    parser.add_argument('csvpath', help='csv path with bbox definitions')
    args = parser.parse_args()
    p = ElevationDownloader(args.osmpath)
    p.download_bboxes_csv(args.csvpath)
