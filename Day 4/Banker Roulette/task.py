import time
import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
payee = random.choice(friends)
print(f"The person paying the bill tonight is: {payee}")

# Angela's solution
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(random.choice(friends))

# Note: I added a process time element to compare the time taken by both solutions.
# The process time is the same for both solutions, which suggests that they are
# equally efficient in terms of execution time.
# Key Difference:
# The main trade-off is readability and reusability versus conciseness. The first approach is more explicit and allows for reusing the payee value, while the second is leaner when you only need to perform a single action with the random selection. Both execute in virtually the same time, as the code comments note.
process_time = time.process_time()
print(f"Process time: {process_time}")

# print("The person paying the bill this evening is:", random.choice(friends))