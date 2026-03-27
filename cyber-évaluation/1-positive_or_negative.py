#!/usr/bin/env python3
import random
n = random.randint(-10, 10)
print(f"{n} is positive" if n > 0 else f"{n} is zero" if n == 0 else f"{n} is negative")
