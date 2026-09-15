#!/usr/bin/env python3
"""Print structured, deterministic output values."""

pi_value = 3.14159
pi_approx = round(pi_value, 2)
computation_valid = (2 + 2) == 4

print("Language: Python")
print("Version: 3")
print(f"Pi approx: {pi_approx:.2f}")
print(f"Computation valid: {computation_valid}")
