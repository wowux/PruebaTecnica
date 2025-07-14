from app.models.fund_model import Subscription
from app.database.db import get_db
from app.utils.notification_utils import send_email_notification, send_sms_notification
import uuid
from datetime import datetime

async def subscribe_to_fund(db, user, fund_id: int):
    funds_data = {
        1: {"name": "FPV_BTG_PACTUAL_RECAUDADORA", "min_amount": 75000},
        2: {"name": "FPV_BTG_PACTUAL_ECOPETROL", "min_amount": 125000},
        3: {"name": "DEUDAPRIVADA", "min_amount": 50000},
        4: {"name": "FDO-ACCIONES", "min_amount": 250000},
        5: {"name": "FPV_BTG_PACTUAL_DINAMICA", "min_amount": 100000}
    }

    fund = funds_data.get(fund_id)
    if not fund:
        raise Exception("Fondo no encontrado")

    if user["balance"] < fund["min_amount"]:
        raise Exception(f"No tiene saldo disponible para vincularse al fondo {fund['name']}")

    subscription_id = str(uuid.uuid4())
    now = datetime.now()

    new_subscription = Subscription(
        subscription_id=subscription_id,
        user_id=user["id"],
        fund_id=fund_id,
        amount=fund["min_amount"],
        status="active",
        created_at=now
    ).dict()

    await db.subscriptions.insert_one(new_subscription)

    # Actualizar el balance del usuario
    await db.users.update_one(
        {"id": user["id"]},
        {"$inc": {"balance": -fund["min_amount"]}}
    )

    # Enviar notificación
    if user["notification_preference"] == "email":
        send_email_notification(user["email"], f"Suscripción exitosa al fondo {fund['name']}")
    else:
        send_sms_notification(user["phone"], f"Suscripción exitosa al fondo {fund['name']}")

    return new_subscription


async def cancel_subscription(db, subscription_id: str, user_id: str):
    sub = await db.subscriptions.find_one({"subscription_id": subscription_id, "user_id": user_id})
    if not sub or sub["status"] == "cancelled":
        raise Exception("Suscripción no encontrada o ya cancelada")

    await db.subscriptions.update_one(
        {"subscription_id": subscription_id},
        {"$set": {"status": "cancelled", "cancelled_at": datetime.now()}}
    )

    # Reembolsar el monto
    amount_refunded = sub["amount"]
    await db.users.update_one(
        {"id": user_id},
        {"$inc": {"balance": amount_refunded}}
    )

    return {"message": f"Suscripción cancelada y COP ${amount_refunded} reembolsados."}