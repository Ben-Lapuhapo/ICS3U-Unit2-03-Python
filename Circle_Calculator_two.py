#!/usr/bin/env python3

# Created by: Ben Lapuhapo
# Created on: September 14 2019
# This program calculates area and circumference.
#  from user input


import constants


def main():
    radius = int(input("Enter Radius of the Circle(mm): "))

    circumference = constants.TAU*radius
    print("")
    print("Circumference is {}mm^2".format(circumference))


if __name__ == "__main__":
    main()
