#!/usr/bin/env python

"""Time spent waiting to cross the street in Cambridge estimate model.
"""

from __future__ import print_function
import sys

def light_encounters(blocks, light_freq=5):
    """Calculate the number of street lights encounted for given blocks walked.
    """
    return blocks / light_freq

def car_encounters(blocks, creep_prob=0.25):
    """Calculate the number of cars encountered for given blocks walked."""
    crossings = blocks - 1
    return crossings * creep_prob

def wait_time(lights, cars, light_wait=30, car_wait=2):
    """Calculate time spent waiting for given encounter counts."""
    l_time = lights * light_wait
    c_time = cars * car_wait
    return l_time + c_time

if __name__ == '__main__':
    travel_distance = int(sys.argv[1])  # units: city blocks

    le = light_encounters(travel_distance)
    ce = car_encounters(travel_distance)

    wait = wait_time(le, ce)
    print("wait time:", wait, "seconds")
