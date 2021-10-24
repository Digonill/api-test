import os

env = os.environ.get("PYTHON_ENV", "dev")

all_environments = {
    "dev": {"port": 5000, "debug": True, "swagger-url": "/doc", "pathbase": "/pwd", "host": "0.0.0.0"},
    "prd": {"port": 8080, "debug": False, "swagger-url": "/doc", "pathbase": "/pwd", "host": "0.0.0.0"}
}

environment_config = all_environments[env]
