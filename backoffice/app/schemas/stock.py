from pydantic import BaseModel, Field


class StockAdd(BaseModel):

    product_id: str

    quantity: int = Field(gt=0)
