#!/usr/bin/python3
"""
Author: Temitope <bamideletemitope42@gmail.com>
Purpose: Say hello
"""

import argparse

def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(description="Say hello")
    parser.add_argument("-n", "--name", metavar="name", default="World", help="Name to greet")
    return parser.parse_args()


def main():
    """The program begins here"""
    args = get_args()
    #name = args.name
    print("Hello, " + args.name + "!")

if __name__ == "__main__":
    main()
