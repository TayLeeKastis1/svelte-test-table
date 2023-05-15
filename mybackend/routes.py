'''
from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models import Exchange, ExchangeUpdate

router = APIRouter()

#POST (all)

@router.post("/", response_description="Create a new exchange", status_code=status.HTTP_201_CREATED, response_model=Exchange)
def create_exchange(request: Request, exchange: Exchange = Body(...)):
    exchange = jsonable_encoder(exchange)
    new_exchange = request.app.database["bidvest"].insert_one(exchange)
    created_exchange = request.app.database["bidvest"].find_one(
        {"_id": new_exchange.inserted_id}
    )

    return created_exchange




# GET (all)
@router.get("/", response_description="List all exchanges", response_model=List[Exchange])
def list_exchanges(request: Request):
    exchanges = list(request.app.database["bidvest"].find(limit=100))
    return exchanges
'''
'''
#GET (id)
@router.get("/{id}", response_description="Get a single book by id", response_model=Book)
def find_book(id: str, request: Request):
    if (book := request.app.database["books"].find_one({"_id": id})) is not None:
        return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with ID {id} not found")
'''

'''
#PUT (id)
@router.put("/{id}", response_description="Update a book", response_model=Book)
def update_book(id: str, request: Request, book: BookUpdate = Body(...)):
    book = {k: v for k, v in book.dict().items() if v is not None}
    if len(book) >= 1:
        update_result = request.app.database["books"].update_one(
            {"_id": id}, {"$set": book}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with ID {id} not found")

    if (
        existing_book := request.app.database["books"].find_one({"_id": id})
    ) is not None:
        return existing_book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with ID {id} not found")

#DELETE
@router.delete("/{id}", response_description="Delete a book")
def delete_book(id: str, request: Request, response: Response):
    delete_result = request.app.database["books"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with ID {id} not found")
'''
