#!/usr/bin/env python3

import sys
import argparse

parser = argparse.ArgumentParser(description='Text File to Python List')

parser.add_argument('--input', help='text file path')
parser.add_argument('--output', help='python file path')

args = parser.parse_args()

in_file = open(args.input, "rt")
out_file = open(args.output, "wt")

out_file.write("words = [\n")
words = [word[:-1] for word in in_file.readlines()]
for data in words[:-1]:
    if not(data.startswith("#!")):
        out_file.write("    \"" + data + "\"")
        out_file.write(",\n")
out_file.write("    \"" + words[-1] + "\"")
out_file.write("\n]\n")

in_file.close()
out_file.close()
