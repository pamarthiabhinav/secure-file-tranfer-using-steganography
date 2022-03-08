import itertools
import threading
import time
import sys, os
from termcolor import colored

# print colored('world', 'green')

done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        os.system('color')
        sys.stdout.write(colored('\rloading ' + c, 'cyan'))
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r')
    sys.stdout.flush()

#long process here
def main():
    global done
    done = False
    t = threading.Thread(target=animate)
    t.start()
    time.sleep(5)
    done = True
    time.sleep(0.3)