from ..config import Settings
from functools import lru_cache
from typing import Annotated
from fastapi import Depends


@lru_cache
def get_settings():
    return Settings()

settings = Annotated[Settings, Depends(get_settings)]