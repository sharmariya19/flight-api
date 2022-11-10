from fastapi import HTTPException, status
from schemas.flightroute import CreateFlightRoute, ShowFlightRoute
from sqlalchemy.orm import Session
from models.flightroute import FlightRoute
from models.flights import Flight
from models.routes import Route


def flight_route(id:int, db:Session):
    object = db.query(FlightRoute).get(id)
    flight = db.query(Flight).get(object.flight_id)
    route = db.query(Route).get(object.route_id)

    ref = ShowFlightRoute(
        id = object.id,
        airline_name = flight.airline_name,
        source = route.source,
        destination = route.destination,
        fare = object.fare,
        takeoff_time = object.takeoff_time,
        landing_time = object.landing_time,
        available_seats= object.available_seats 
    )
    return ref


def new_flight_route(flight: CreateFlightRoute, db: Session):
    new_flight = FlightRoute(**flight.dict())
    db.add(new_flight)
    db.commit()
    db.refresh(new_flight)
    return new_flight


def get_all_flight_route(db: Session):
    obj = db.query(FlightRoute).all()
    lst = []
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No flights on this route")
    
    for flightroute in obj:
        object = flight_route(flightroute.id, db)
        lst.append(object)
    return lst


def get_flight_route(source:str, destination:str, db:Session):
    route = db.query(Route).filter(Route.source == source , Route.destination == destination).first()
    if not route:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "No flights between these citites")
    obj = db.query(FlightRoute).filter(FlightRoute.route_id == route.id).all()
    lst = []
    for flightroute in obj:
        object = flight_route(flightroute.id, db)
        lst.append(object)
    return lst


def delete_flight_route(id:int, db:Session):
    ref = db.query(FlightRoute).get(id)
    if not ref:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Flight with id {id} not found"
        )
    else:
        db.delete(ref)
    db.commit()

    return ref

