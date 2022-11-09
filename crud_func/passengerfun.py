from fastapi import HTTPException, status
from schemas.passengers import PassengerCreate
from sqlalchemy.orm import Session
from models.passengers import Passenger
from hashing import Hasher


def create_new_passenger(passenger: PassengerCreate, db: Session):
    obj = db.query(Passenger).filter(Passenger.email==passenger.email)
    if obj:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Passenger with this email already exist")
    new_passenger = Passenger(
        name = passenger.name,
        gender = passenger.gender,
        age = passenger.age,
        contact = passenger.contact,
        email = passenger.email,
        nationality =  passenger.nationality,
        hash_password = Hasher.get_password_hash(passenger.password)
    )
    db.add(new_passenger)
    db.commit()
    db.refresh(new_passenger)
    return new_passenger


def get_all_passengers(db: Session):
    obj = db.query(Passenger).all()
    return obj

def delete_passenger_by_id(id:int, db:Session):
    ref = db.query(Passenger).get(id)
    if not ref:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Passenger with id {id} not found"
        )
    else:
        db.delete(ref)
    db.commit()

    return ref