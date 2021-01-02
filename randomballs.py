#!/usr/bin/env python3

import argparse
import random
import json
import string

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Generate a random permutation of balls in tubes")
	parser.add_argument("colours", help="number of colours", type=int)
	parser.add_argument("height", help="height of tubes", type=int)
	parser.add_argument("json", help="output filename (will be written in JSON format)")
	args = parser.parse_args()
	if(args.colours < 2 or args.colours > 52):
		exit("Colours must be between 2-52")
	if(args.height < 2):
		exit("Height must be 2 or more")

	l = []
	for i in range(args.colours):
		colour = string.ascii_letters[i]
		cs = [colour]*args.height
		l += cs
	random.shuffle(l)

	grid = []
	pos = 0
	for i in range(args.colours):
		grid.append(l[pos:pos+args.height])
		pos += args.height
	grid.append([])
	grid.append([])

	obj = dict()
	obj["tubes"] = grid

	with open(args.json, "w") as json_file:
		json.dump(obj, json_file, indent=4)
