print(f"running {__name__}")

from inner_folder import helper_functions

result_add = helper_functions.add_config_constant(5)

print("Add config result:", result_add)