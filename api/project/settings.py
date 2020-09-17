import os
from typing import Optional

from pydantic import BaseSettings


class ProjectEnvironment(BaseSettings):
    PROJECT_DIR: Optional[str] = os.path.dirname(__file__)
    RUNTIME_DIR: Optional[str] = os.path.dirname(PROJECT_DIR)

    LOGGING_LEVEL: Optional[int] = 10


class WerkzeugEnvironment(BaseSettings):
    HOST: Optional[str] = '0.0.0.0'
    PORT: Optional[int] = 5000
    DEBUG: Optional[bool] = True


project_env = ProjectEnvironment()
werkzeug_env = WerkzeugEnvironment()
