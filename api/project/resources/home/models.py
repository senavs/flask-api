from pydantic import BaseModel


class HomeRequest(BaseModel):
    id: int
