from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal


class AccountCreate(BaseModel):
    name: str


class AccountResponse(BaseModel):
    id: int
    name: str
    balance: Decimal
    created_at: datetime | None = None
    model_config = {"from_attributes": True}
