#!/anconda/bin/python3
# Author : Abhinav

import argparse
import time
import os
import logging
from threading import Timer

class TimerPy:

    def __init__(self, time, task_name):
        self.duration = time
        self.task_name = task_name

    def start(self):
        print("Starting Timer at ", time.strftime("%H:%M:%S", time.localtime()))
        logging.info("Starting Timer at "+ time.strftime("%H:%M:%S", time.localtime()))

    def finish(self):
        notify("Timer", "Timer for %s is up" %(self.task_name))
        print("Ending Time: ", time.strftime("%H:%M:%S", time.localtime()))
        logging.info("Ending Time for %s: "%(self.task_name)+ time.strftime("%H:%M:%S", time.localtime()))

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

if __name__ == "__main__":
    logging.basicConfig(filename="timer.log",level=logging.INFO)
    parser= argparse.ArgumentParser()
    parser.add_argument("-s", help="set timer", action="store_true",dest="start",required=True)
    subparsers = parser.add_subparsers(title="time",help="time for the timer", dest="type")
    hour_parser=subparsers.add_parser("hour")
    hour_parser.add_argument(dest="hour", type=int)
    minute_parser = subparsers.add_parser("minute")
    minute_parser.add_argument( dest="minute", type=int)
    second_parser = subparsers.add_parser("second")
    second_parser.add_argument(dest="seconds", type=int)
    parser.add_argument("--name", dest="task_name", type=str)
    args = parser.parse_args()
    parser.add_argument("-p", help="pause the timer")
    duration=0
    logging.debug(args)
    if args.start:
        logging.debug(args.start)
        if args.type == "minute":
            duration=args.minute * 60
        if args.type == "hour":
            duration=args.hour * 60 * 60
        if args.type == "second":
            duration=args.seconds
        logging.info("Starting the timer")
        timer = TimerPy(duration, args.task_name)
        timer.start()
        print(duration)
        t=Timer(duration, timer.finish)
        t.start()

