from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal


class TransactionResponse(BaseModel):
    id: int
    account_id: int
    amount: Decimal
    description: str
    category: str
    created_at: datetime | None = None
    model_config = {"from_attributes": True}


class TransactionCreate(BaseModel):
    account_id: int
    amount: Decimal
    description: str
    category: str
