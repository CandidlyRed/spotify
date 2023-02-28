# TODO: Implement time blockers
# TODO: Implement random generators

import time
import random

# figure out what terminal command to set up

start = time.time()

PERIOD_OF_TIME = 50400 # 3600=1hr, this is currently set as 14 hours

while True :
    # time.sleep(600.0 - ((time.time() - start) % 600.0))
    rand = random.randint(1,110)
    print(rand)
    if rand == 1:
        break # where action function exists

    if time.time() > start + PERIOD_OF_TIME : break