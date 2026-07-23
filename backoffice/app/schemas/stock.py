from pydantic import BaseModel, Field


class StockUpdate(BaseModel):
    """
    Request body for adding or removing stock.
    """

    product_id: str = Field(..., min_length=1)
    quantity: int = Field(..., gt=0)


class StockResponse(BaseModel):
    """
    Response returned after a stock operation.
    """

    product_id: str
    quantity: int


class StockItem(BaseModel):
    """
    One product in a branch.
    """

    product_id: str
    quantity: int

    class Config:
        from_attributes = True
