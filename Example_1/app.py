# This is a script has multiple code blocks
# app.py 

# Configs block
database_url = "example.com/db"
api_key = "your_api_key"
debug_mode = True
config_constant = 10

# Functions block
def add_config_constant(a:int)->int:
    return a + config_constant

# Prints and usage of the previous parameters and funcion blocks
print("Database URL:", database_url)
print("API Key:", api_key)
print("Debug Mode:", debug_mode)

result_add = add_config_constant(5)
print("Add config Result:", result_add)