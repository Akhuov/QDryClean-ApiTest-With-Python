from pydantic import BaseModel

class BaseSchema(BaseModel):
    class Config:
        extra = "forbid"   # Запрещаем неожиданные поля
        orm_mode = True    # Позволяет работать с объектами (если надо)
