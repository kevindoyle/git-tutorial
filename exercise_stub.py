#!/usr/bin/env python

"""Time spent waiting to cross the street in Cambridge estimate model.
"""

from __future__ import print_function
import sys

#
#
#
#
#

if __name__ == '__main__':
    travel_distance = int(sys.argv[1])  # units: city blocks

    le = light_encounters(travel_distance)
    ce = car_encounters(travel_distance)

    wait = wait_time(le, ce)
    print("wait time:", wait, "seconds")
