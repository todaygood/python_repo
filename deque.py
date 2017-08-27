#!/usr/bin/env python

from collections import deque

queue=deque(["Today","Tommy","Jonh"])

queue.append("Mike")
queue.append("Mark")

print queue.popleft()

print queue.popleft()

print queue



