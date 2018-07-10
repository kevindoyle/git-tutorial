#!/usr/bin/env python

"""Time spent waiting to cross the street in Cambridge estimate model.
"""

from __future__ import print_function
import sys

# Average blocks per stop light
LIGHT_FREQUENCY_CONSTANT = 5

# Average seconds spent waiting for a crossing sign
LIGHT_WAIT_TIME = 30 

# Average seconds waiting when a car is inching into the crosswalk and you
# have to wait to make eye contact so they don't run over you.
CAR_CREEP_WAIT_TIME = 2

# Probability that a car will be creeping at any given street crossing
CAR_CREEP_PROBABILITY = 0.25

def light_encounters(blocks, light_freq=LIGHT_FREQUENCY_CONSTANT):
    """Calculate the number of street lights encounted for given blocks walked.
    """
    return blocks / light_freq

def car_encounters(blocks, creep_prob=CAR_CREEP_PROBABILITY):
    """Calculate the number of cars encountered for given blocks walked."""
    crossings = blocks - 1
    return crossings * creep_prob

def wait_time(lights, cars, light_wait=LIGHT_WAIT_TIME, car_wait=CAR_CREEP_WAIT_TIME):
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
