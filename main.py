from fastapi import FastAPI
from routers import coupon, passenger, flight, route, booking, payment, flight_route
from database import Base, engine

app = FastAPI(title="Flights API")

Base.metadata.create_all(bind=engine)

app.include_router(passenger.router)
app.include_router(flight.router)
app.include_router(route.router)
app.include_router(flight_route.router)
app.include_router(booking.router)
app.include_router(coupon.router)
app.include_router(payment.router)
# app.include_router(transaction.router)
