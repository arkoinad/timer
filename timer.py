#!/anconda/bin/python3
# Author : Abhinav

import argparse
import time
import asyncio
import os
import logging

class Timer:

    def __init__(self, time):
        self.timer = timer

    def start(self):
        print("Starting Timer at ", time.strftime("%H:%M:%S", time.localtime()))
        logging.info("Starting Timer at "+ time.strftime("%H:%M:%S", time.localtime()))
        time.sleep(self.timer)
        #notify("Timer", "Timer is up")
        self.finish()

    def finish(self):
        print("Ending Time: ", time.strftime("%H:%M:%S", time.localtime()))
        logging.info("Ending Time: "+ time.strftime("%H:%M:%S", time.localtime()))

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
    timer=0
    logging.debug(args)
    if args.start:
        logging.debug(args.start)
        loop = asyncio.get_event_loop()
        if args.type == "minute":
            timer=args.minute * 60
        if args.type == "hour":
            timer=args.hour * 60 * 60
        if args.type == "second":
            timer=args.seconds
        logging.info("Starting the timer")
        timer = Timer(timer)
        timer.start()