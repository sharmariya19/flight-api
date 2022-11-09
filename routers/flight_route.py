from fastapi import APIRouter, Depends, status, HTTPException
from schemas.flight_route import CreateFlightRoute, ShowFlightRoute
from database import get_db
from sqlalchemy.orm import Session
from crud_func.flightroute_fun import get_flight_route, new_flight_route, delete_flight_route
from typing import List
from models.routes import Route
from models.flight_route import FlightRoute

router = APIRouter( tags= ['flight_route'])


@router.post(
    "/flightroute", status_code=status.HTTP_201_CREATED
)
def create_flightroute(flight: CreateFlightRoute, db: Session = Depends(get_db)):
    new_flight = new_flight_route(flight=flight, db=db)
    return "flight route created"



@router.get( "/flightroute",response_model=List[ShowFlightRoute],status_code=status.HTTP_200_OK)
def get_flightroute(db: Session = Depends(get_db)):
    ref = get_flight_route(db=db)
    return ref


@router.delete("/flightroute/{id}",status_code=status.HTTP_200_OK)
def delete_flightroute(id:int , db:Session= Depends(get_db)):
    obj = delete_flight_route(id=id, db=db)
    return "Successfully deleted"



@router.get("/route/{source}/{destination}",response_model = List[ShowFlightRoute],  status_code=status.HTTP_200_OK)
def get_flights(source:str, destination:str, db:Session = Depends(get_db)):
    route = db.query(Route).filter(Route.source == source , Route.destination == destination).first()
    obj = db.query(FlightRoute).filter(FlightRoute.route_id == route.id).all()
    if obj:
        return obj
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "No flights between these citites")