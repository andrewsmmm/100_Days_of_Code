import time
import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
payee = random.choice(friends)
print(f"The person paying the bill tonight is: {payee}")

# Angela's solution
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(random.choice(friends))


process_time = time.process_time()
print(f"Process time: {process_time}")

# print("The person paying the bill this evening is:", random.choice(friends))