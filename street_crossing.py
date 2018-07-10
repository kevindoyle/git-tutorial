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

travel_distance = int(sys.argv[1])  # units: city blocks

lights_encountered = travel_distance / LIGHT_FREQUENCY_CONSTANT

street_crossings = travel_distance - 1
creeping_car_encounters = street_crossings * CAR_CREEP_PROBABILITY

wait_time = (lights_encountered * LIGHT_WAIT_TIME) + (creeping_car_encounters * CAR_CREEP_WAIT_TIME) 

print("wait time:", wait_time, "seconds")

