#!/usr/bin/env python

[print("{}*{}={:<4d}".format(y,x,x*y),end='\n' if x == y else '') for x in range(1,10) for y in range(1,x+1)]
