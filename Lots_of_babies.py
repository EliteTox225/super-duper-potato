"""Simulates natural selection in the fictional Neebler population."""

import math
import random


# Starting population with each trait variation.
small_neeblers = 100
big_neeblers = 100
colorful_neeblers = 100
camouflaged_neeblers = 100
neeblers = small_neeblers + big_neeblers + colorful_neeblers + camouflaged_neeblers

for i in range(50):

    flood = random.randint(51, 100)
    if flood == 100:
        small_neeblers -= math.floor(0.7 * small_neeblers)
        big_neeblers -= math.floor(0.7 * big_neeblers)
        colorful_neeblers -= math.floor(0.7 * colorful_neeblers)
        camouflaged_neeblers -= math.floor(0.7 * camouflaged_neeblers)
        print("\nFlood!\n")


    for neebler in range(small_neeblers):
        # Low chance of being spotted by predators since they're small.
        chance_of_being_spotted = random.randint(0, 4)
        if chance_of_being_spotted == 4:
            small_neeblers = small_neeblers - 1

    baby_small_neeblers = 0
    for neebler in range(small_neeblers):
    # Smallness trait gets passed to their babies.
        if neeblers <= 15000:
            num_babies = random.randint(0, 3)
            baby_small_neeblers = baby_small_neeblers + num_babies
        else:
            num_babies = random.randint(0, 2)
            baby_small_neeblers = baby_small_neeblers + num_babies


    # Babies become the starting population of the next generation.
    small_neeblers = baby_small_neeblers
    print(str(small_neeblers) + " small Neeblers")


    for neebler in range(big_neeblers):
        # High chance of being spotted by predators since they're big.
        chance_of_being_spotted = random.randint(0, 1)
        if chance_of_being_spotted == 1:
            big_neeblers = big_neeblers - 1

    baby_big_neeblers = 0
    for neebler in range(big_neeblers):
    # Bigness trait gets passed to their babies.
        if neeblers <= 15000:
            num_babies = random.randint(0, 5)
            baby_big_neeblers = baby_big_neeblers + num_babies
        else:
            num_babies = random.randint(0, 4)
            baby_big_neeblers = baby_big_neeblers + num_babies


    # Babies become the starting population of the next generation.
    big_neeblers = baby_big_neeblers
    print(str(big_neeblers) + " big Neeblers")


    for neebler in range(colorful_neeblers):
        # Moderate chance of being seen as weak by predators since they're colorful.
        chance_of_being_spotted = random.randint(0, 3)
        if chance_of_being_spotted == 3:
            colorful_neeblers = colorful_neeblers - 1

    baby_colorful_neeblers = 0
    for neebler in range(small_neeblers):
    # Colorful trait gets passed to their babies.
        if neeblers <= 15000:
            num_babies = random.randint(0, 4)
            baby_colorful_neeblers = baby_colorful_neeblers + num_babies
        else:
            num_babies = random.randint(0, 3)
            baby_colorful_neeblers = baby_colorful_neeblers + num_babies

    # Babies become the starting population of the next generation.
    colorful_neeblers = baby_colorful_neeblers
    print(str(colorful_neeblers) + " colorful Neeblers")


    for neebler in range(camouflaged_neeblers):
        # Very low chance of being spotted by predators since they're camouflaged.
        chance_of_being_spotted = random.randint(0, 9)
        if chance_of_being_spotted == 9:
            camouflaged_neeblers = camouflaged_neeblers - 1

    baby_camouflaged_neeblers = 0
    for neebler in range(camouflaged_neeblers):
    # Camouflage trait gets passed to their babies.
        if neeblers <= 15000:
            num_babies = random.randint(0, 3)
            baby_camouflaged_neeblers = baby_camouflaged_neeblers + num_babies
        else:
            num_babies = random.randint(0, 2)
            baby_camouflaged_neeblers = baby_camouflaged_neeblers + num_babies

    # Babies become the starting population of the next generation.
    camouflaged_neeblers = baby_camouflaged_neeblers
    print(str(camouflaged_neeblers) + " camouflaged Neeblers")

    print(" ")

    neeblers = small_neeblers + big_neeblers + colorful_neeblers + camouflaged_neeblers

print("End of natural selection simulation.")

# I'm very satisfied with the current result!
