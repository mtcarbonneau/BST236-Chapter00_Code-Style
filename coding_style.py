"""
Coding Style Examples

This module demonstrates various Python coding style principles and best practices
based on PEP 8 and common conventions.
"""

# =============================================================================
# Naming Objects Examples
# =============================================================================

# Bad example - not self-documenting

def func(y):
    # z is gravitational force
    z = 9.81
    # y is time in seconds
    y = 5
    # x is displacement
    x = 1/2 * z * y**2
    return x

# Good example - self-documenting
def compute_displacement(time_in_seconds):
    gravitational_force = 9.81
    displacement = 1/2 * gravitational_force * time_in_seconds**2
    return displacement

# Even better - with parameters
def compute_displacement(time_in_seconds, gravitational_force=9.81):
    displacement = 1/2 * gravitational_force * time_in_seconds**2
    return displacement

# =============================================================================
# Naming Conventions Examples
# =============================================================================

# snake_case (Python preferred style)
def calculate_average(number_list):
    return sum(number_list) / len(number_list)

# camelCase (less common in Python)
def calculateAverage(numberList):
    return sum(numberList) / len(numberList)

# =============================================================================
# Documentation Examples
# =============================================================================

# Bad example
def f(x, y):
    a = x + y  # What does 'a' represent?
    return a

# Good example
def calculate_total_price(item_price, tax_rate):
    """Calculate final price including tax.
    
    Args:
        item_price (float): Original price of the item
        tax_rate (float): Tax rate as a decimal (e.g., 0.1 for 10%)
    
    Returns:
        float: Total price including tax
    """
    total_price = item_price * (1 + tax_rate)
    return total_price

# =============================================================================
# Spacing and Operators Examples
# =============================================================================

def demonstrate_spacing():
    # Bad spacing
    x=y+z
    if x>0:print(x)

    # Good spacing
    x = y + z
    if x > 0:
        print(x)

# =============================================================================
# Indentation Examples
# =============================================================================

# Good indentation
def process_data():
    if condition:
        do_something()
        for item in items:
            process_item()

# Bad indentation (mixing spaces) - commented out as it would cause syntax error
"""
def process_data():
   if condition:
      do_something()
        for item in items:
         process_item()
"""

# =============================================================================
# Maximum Line Length Examples
# =============================================================================

# Bad - too long
# result = some_long_function_name(very_long_parameter_name1, very_long_parameter_name2, very_long_parameter_name3)

# Good - split into multiple lines
result = some_long_function_name(
    very_long_parameter_name1,
    very_long_parameter_name2,
    very_long_parameter_name3
)

# =============================================================================
# Imports Example
# =============================================================================

# Good import organization
import os
import sys

import numpy as np
import pandas as pd

from myproject.utils import helper
from myproject.core import main

# Note: The following is an example of bad import organization (commented out)
"""
from myproject.utils import helper
import sys
import pandas as pd
from myproject.core import *  # Avoid wildcard imports
import os
""" 