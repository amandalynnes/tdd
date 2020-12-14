#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "Amanda Simmons"


import sys
import argparse


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-h', help='show this help message and exit')
    parser.add_argument('--help', help='show this help message and exit')
    parser.add_argument('-u', help='convert text to uppercase')
    parser.add_argument('--upper', help='convert text to uppercase')
    parser.add_argument('-l', help='convert text to lowercase')
    parser.add_argument('--lower', help='convert text to lowercase')
    parser.add_argument('-t', help='convert text to titlecase')
    parser.add_argument('--title', help='convert text to titlecase')

    return


def main(args):
    """Implementation of echo"""

    ns = parser.parse_args(args)
    return


if __name__ == '__main__':
    main(sys.argv[1:])
