from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import Depends
from typing import Generator

client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client.btg_pactual_db

def get_db():
    return db