#!/usr/bin/env python3
from calculator_adapter import run


### ADD AT LEAST TWO TESTS HERE!
# Checks that program outputs "2" for an input "8 / 4"
assert run("8 / 4").output == "2"

# Checks that program output "-2" for an input "1 - 3"
assert run("1 - 3").output == "-2"

# Checks that program outputs "0" for an input "0 * 5"
assert run("0 * 5").output == "0"

# Checks that program outputs "9" for an input "7 + 2"
assert run("7 + 2").output == "9"
###

print("All tests passed!")
