import os

env = os.environ.get("PYTHON_ENV", "development")

all_environments = {
    "development": {"port": 5000, "debug": True, "swagger-url": "/doc", "pathbase": "/pwd"},
    "production": {"port": 8080, "debug": False, "swagger-url": "/doc", "pathbase": "/pwd"}
}

environment_config = all_environments[env]
