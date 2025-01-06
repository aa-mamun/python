# Create a coin flip program . 
# It should randomly print "Heads" or "Tails" everytime it is run.

import random
rand_num = random.randint(1,100)
if rand_num % 2 == 0:
    print("Heads")
else:
    print("Tails")
