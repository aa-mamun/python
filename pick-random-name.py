# Figure out how to pick a random name from the list of friends.
import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
rand_num = random.randint(0, len(friends)-1)
print(friends[rand_num])
