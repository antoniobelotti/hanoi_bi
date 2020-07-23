import argparse
import sys
import time

import lib
import string_helpers as helpers


def build_arg_parser():
    parser = argparse.ArgumentParser(description=helpers.PROGRAM_DESCRIPTION)

    parser.add_argument("-nd", "--num_of_disks", type=int, help=helpers.NUM_OF_DISKS_OP)

    parser.add_argument("-b", "--bicolor",   action='store_true', help=helpers.BICOLOR_OP)
    parser.add_argument("-l", "--list",      action='store_true', help=helpers.LIST_OP)
    parser.add_argument("-e", "--enumerate", action='store_true', help=helpers.ENUM_OP)
    parser.add_argument("-o", "--optimize",  action='store_true', help=helpers.OPTIMIZE_OP)
    parser.add_argument("-i", "--info",      action='store_true', help=helpers.INFO_OP)
    parser.add_argument("-s", "--source",                         help=helpers.SOURCE_OP)
    parser.add_argument("-d", "--destination",                    help=helpers.DESTINATION_OP)
    parser.add_argument("-t", "--temporary",                      help=helpers.TEMP_OP)
    return parser


initial_ts = time.time()

parser = build_arg_parser()

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

if args.source and args.destination and args.temporary:
    source = args.source
    dest = args.destination
    tmp = args.temporary
else:
    source = "A"
    dest = "B"
    tmp = "C"

if args.bicolor:
    moves_sol_of_game = lib.hanoi_bicolor_version(args.num_of_disks, source, dest, tmp)
else:
    moves_sol_of_game = lib.hanoi(args.num_of_disks, source, dest, tmp)

if args.optimize and args.bicolor:
    lib.optimize(moves_sol_of_game)

if args.list:
    print(moves_sol_of_game)
else:
    if args.enumerate:
        for counter, move in enumerate(moves_sol_of_game, 1):
            print(counter, "\t", move)
    else:
        print(*moves_sol_of_game, sep="\n")

final_ts = time.time()

if args.info:
    print("\nMODE:\t\t", "Bicolor" if args.bicolor else "Classic")
    if args.bicolor:
        print("OPTIMIZED: \t", args.optimize)
    print("TOTAL MOVES:   \t", len(moves_sol_of_game))
    print("EXECUTION TIME:\t", final_ts-initial_ts, " sec")
    print("SOURCE:     \t", source)
    print("DESTINATION:\t", dest)
    print("TEMPORARY:  \t", tmp)
