import os

# Display current environment variables
print("Current environment variables:")
for key, value in os.environ.items():
    print(f"{key}: {value}")

# Define the environment variable name and value
env_var_name = "MY_ENV_VAR"
env_var_value = "MyValue123"

# Set the environment variable using os.putenv()
os.putenv(env_var_name, env_var_value)

# Retrieve the environment variable using os.getenv()
retrieved_value = os.getenv(env_var_name)
print(f"\nEnvironment variable '{env_var_name}' set to '{retrieved_value}'")

# Display updated environment variables
print("\nUpdated environment variables:")
for key, value in os.environ.items():
    print(f"{key}: {value}")