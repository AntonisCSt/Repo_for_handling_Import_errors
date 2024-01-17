from inner_folder import config

print(config.database_url)
print(config.config_constant)


def add_config_constant(a: int) -> int:
    return a + config.config_constant
