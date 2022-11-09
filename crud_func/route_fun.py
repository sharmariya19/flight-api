from fastapi import HTTPException, status
from schemas.routes import RouteCreate
from sqlalchemy.orm import Session
from models.routes import Route
from models.flights import Flight


def create_new_route(route: RouteCreate, db: Session):
    new_route = Route(**route.dict())
    db.add(new_route)
    db.commit()
    db.refresh(new_route)
    return new_route


def get_all_routes(db: Session):
    obj = db.query(Route).all()
    return obj

def delete_route_by_id(id:int, db:Session):
    ref = db.query(Route).get(id)
    if not ref:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Route with id {id} not found"
        )
    else:
        db.delete(ref)
    db.commit()

    return ref