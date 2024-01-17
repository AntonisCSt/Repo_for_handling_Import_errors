print(f"running {__name__}")

import sys
import os

# Get the absolute path of the current script's directory
current_script_directory = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory (helper_functions) to sys.path
sys.path.append(os.path.join(current_script_directory, 'inner_folder'))

# Now you can import modules from the added path
from inner_folder import helper_functions

result_add = helper_functions.add_config_constant(5)

print("Add config result:", result_add)