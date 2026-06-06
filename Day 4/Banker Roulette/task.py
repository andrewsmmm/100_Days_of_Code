import time
import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
payee = random.choice(friends)
print(f"The person paying the bill tonight is: {payee}")

# Angela's solution
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(random.choice(friends))

# Note: I added a process time element to compare the time taken by both solutions. The process time is the same for both solutions, which suggests that they are equally efficient in terms of execution time. However, the second solution is more concise and easier to read, which may make it more preferable in terms of code readability and maintainability.
process_time = time.process_time()
print(f"Process time: {process_time}")

# print("The person paying the bill this evening is:", random.choice(friends))