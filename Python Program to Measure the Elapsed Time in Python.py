# Example 1: Using time module

import time

start = time.time()

print(23*2.3)

end = time.time()
print(end - start)

# Output
# 52.9
# 0.0004525184631347656

# Example 2: Using timeit module

from timeit import default_timer as timer

start = timer()

print(23*2.3)

end = timer()
print(end - start)

# Output
# 52.9
# 0.00023180001880973577
