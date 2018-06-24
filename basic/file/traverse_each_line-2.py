#!/usr/bin/env python

with open("score.txt") as file:
    for line in file:
        line= line.rstrip("\n")
        print(line)

