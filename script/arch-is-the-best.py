#!/usr/bin/env python2

import signal
import sys

def arch_is_the_best(are_the_cats_out=False):
        answer = "no answer yet"
        what = "the best"
        if are_the_cats_out:
                what = "DA GUD KITTEH"
        while answer != "y" :
                try:
                        print "Arch is %s!" % what
                        print "Do you agree?(y/n)",
                        answer = sys.stdin.readline().rstrip('\n')
                        print
                        if answer == "n" :
                                print "Maybe you should reconsider your opinion."
                        elif answer != "y" :
                                print "There are only two possible answers and this is none of them."
                        print
                except KeyboardInterrupt:
                        print
                        print "What are you trying to do?"
                        what = "devilish"
                        pass

def let_the_cats_out(signum, frame):
        print
        print
        print "U R BAD BAD BAD KITTEH!"
        print
        arch_is_the_best(True)

for signum in range(32):
        try:
                signal.signal(signum, let_the_cats_out)
        except:
                pass
# Shush... Kitten says nyan nyan da SIGKILL.

if __name__ == "__main__":
        arch_is_the_best()
        print "Glad you agree!"
