from fastapi import APIRouter, Depends, HTTPException
from app.database.db import get_db
from app.services.fund_service import subscribe_to_fund, cancel_subscription
from pymongo import MongoClient

router = APIRouter()


@router.post("/subscribe/{fund_id}")
async def subscribe(fund_id: int, user_id: str, db: MongoClient = Depends(get_db)):
    user = await db.users.find_one({"id": user_id})
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    try:
        result = await subscribe_to_fund(db, user, fund_id)
        return {"success": True, "data": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/unsubscribe/{subscription_id}")
async def unsubscribe(subscription_id: str, user_id: str, db: MongoClient = Depends(get_db)):
    try:
        result = await cancel_subscription(db, subscription_id, user_id)
        return {"success": True, "data": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))