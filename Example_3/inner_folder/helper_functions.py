# inner_folder/helper_functions.py 

# Idea for the example was taken from: 
# https://stackoverflow.com/questions/43728431/relative-imports-modulenotfounderror-no-module-named-x

print(f"running {__name__}")

# Relative import for config
try:
    from . import config

    print('Relative import (from . import config) was successful')

except (ImportError, ModuleNotFoundError):
    print('Config relative import (from . import config) failed')

# Absolute import for config
try:
    import config

    print('Absolute import (import config) was successful')

except (ImportError, ModuleNotFoundError):
    print('Config absolute import (import config) failed')

def add_config_constant(a: int)-> int:
    return a + config.config_constant
