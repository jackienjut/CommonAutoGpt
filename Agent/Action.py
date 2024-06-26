from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any


class Action(BaseModel):
    name: str = Field(default_factory="Tool Name")
    args: Optional[Dict[str, Any]] = Field(description="Tool input arguments, containing arguments names and values")
