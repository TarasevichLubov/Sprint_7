from pydantic import BaseModel
from typing import List, Optional


class Orders(BaseModel):

    id: int
    courierId: Optional[int] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    address: Optional[str] = None
    metroStation: Optional[str] = None
    phone: Optional[str] = None
    rentTime: Optional[int] = None
    deliveryDate: Optional[str] = None
    track: int
    color: Optional[List[str]] = None
    comment: Optional[str] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None
    status: int
