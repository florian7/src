#!/usr/bin/python3 

import sys, time
import dragonCurve

steps = 4
if len(sys.argv) >= 2:
    steps = int(sys.argv[1])

start = time.time()
instructions = dragonCurve.Instructions(steps)
instructions.generate()
end = time.time()

print("dragonCurve.Instructions({}) : {}s".format(steps, end - start))

print(instructions)
print(len(str(instructions)))

start = time.time()
line = dragonCurve.Line(instructions)
line.generate()
end = time.time()

print("dragonCurve.Line({}) : {}s".format(steps, end - start))

