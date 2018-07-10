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

def light_encounters(blocks):
    """Calculate the number of street lights encounted for given blocks walked.
    """
    return blocks / LIGHT_FREQUENCY_CONSTANT

def car_encounters(blocks):
    """Calculate the number of cars encountered for given blocks walked."""
    crossings = blocks - 1
    return crossings * CAR_CREEP_PROBABILITY

def wait_time(lights, cars):
    """Calculate time spent waiting for given encounter counts."""
    light_wait = lights * LIGHT_WAIT_TIME
    car_wait = cars * CAR_CREEP_WAIT_TIME
    return light_wait + car_wait

if __name__ == '__main__':
    travel_distance = int(sys.argv[1])  # units: city blocks

    le = light_encounters(travel_distance)
    ce = car_encounters(travel_distance)

    wait = wait_time(le, ce)
    print("wait time:", wait, "seconds")
