from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class Fund(BaseModel):
    id: int
    name: str
    min_amount: float
    category: str

class Subscription(BaseModel):
    subscription_id: str
    user_id: str
    fund_id: int
    amount: float
    status: str  # active/cancelled
    created_at: datetime
    cancelled_at: Optional[datetime] = None