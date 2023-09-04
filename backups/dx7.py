#! /usr/bin/env python3

import argparse
import dx7_algo as FM

def fileParse(input_file):

    output_list = []
    with open(input_file) as file:
        for index,line in enumerate(file):
            line = line.replace("\n","")
            if index == 0:
                line = float(line)
            elif index > 0 and index < 7:
                if line != "none":
                    line = line.split(' ')
                    for index1, val in enumerate(line):
                        if index1 < 3:
                            line[index1] = float(val)
                        if index1 == 4 and val == "none":
                            line[index1] = None
                        elif index1 > 3 and line[index1]:
                            line[index1] = line[index1].split(",")
                            for index2, num in enumerate(line[index1]):
                                line[index1][index2] = float(num)
                else:
                    line = [0,0,0,"cosine",None]
            elif index == 7:
                if line == "true":
                    line = True
                else:
                    line = False
            elif index == 8:
                line = int(line)
            output_list.append(line)
    return output_list

def run(args):
    path = args.input

    try:
        input = fileParse(path)
        algorithm = FM.algos()
        func = algorithm.algos[input[8]-1]
        osc = func(input[:8])
        osc.write_wav(f"./{input[9]}")
        
    except FileNotFoundError:
        print("INPUT FILE NOT FOUND")

#####################################################################

def main():
	parser=argparse.ArgumentParser(description="Creates an emulated Yamaha DX-7 wav file.")
	parser.add_argument("-in", help="Input", dest="input", type=str, required=True)
	parser.set_defaults(func=run)
	args=parser.parse_args()
	args.func(args)

if __name__=="__main__":
	main()
