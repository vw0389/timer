#!/bin/python3

import sys
import time
import argparse


def main():

    parser = argparse.ArgumentParser("simple timer for simple time."
                                     " -t and -i flags take input in x min(ute)(s) &| y sec(ond)(s)")
    parser.add_argument("-t", "--time", help="amount of time for the timer",
                        required=True, nargs='*')
    parser.add_argument("-i", "--interval", help="interval between timers",
                        nargs='*', default=0)
    parser.add_argument("-r", "--repeats", help="# of repeat(s) of timer and interval",
                        default=0, type=int, nargs=1)
    args = parser.parse_args()
    time_var = parse_time(args.time)
    interval = parse_time(args.interval)
    try:
        repeats = args.repeats[0]
    except TypeError:
        repeats = 0

    if repeats < 0 or time_var == -1 or interval == -1:
        parser.print_usage()
        parser.exit()
        sys.exit(2)
    do_timer(time_var, interval, repeats)


def parse_time(time_list):
    if time_list == 0:
        return 0
    seconds = 0
    seconds_strings = ['sec', 'secs', 'second', 'seconds']
    minute_strings = ['min', 'mins', 'minute', 'minutes']
    if len(time_list) < 2 or len(time_list) == 3 or len(time_list) > 4:
        return -1
    for i in range(0, len(time_list), 2):
        value = time_list[i]
        value_unit = time_list[i+1]
        try:
            value = int(value)
        except ValueError:
            return -1
        if value < 0:
            return -1
        if value_unit in minute_strings:
            seconds = seconds + value * 60
        elif value_unit in seconds_strings:
            seconds = seconds + value
        else:
            return -1
    return seconds


def do_timer(time_var, interval, repeat):
    print("time_var:", str(time_var), " seconds")
    print("interval:", str(interval))
    print("repeats:", str(repeat))

    if repeat is None:
        repeat = 1
    elif repeat == 0:
        repeat = 1
    if interval is None:
        interval = 0

    for i in range(repeat):
        time.sleep(time_var)
        if i == repeat-1:
            print("done")

        else:
            print("interval")
            do_something(interval)
    return


def do_something(interval):
    for i in range(interval):
        time.sleep(1)
        print(str(i+1))
    return


if __name__ == "__main__":
    main()
