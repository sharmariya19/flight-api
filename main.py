from fastapi import FastAPI
from routers import passenger, flight, route, booking, discount, payment
from database import Base, engine

app = FastAPI(title="Flights API")

Base.metadata.create_all(bind=engine)

app.include_router(passenger.router)
app.include_router(flight.router)
app.include_router(route.router)
app.include_router(booking.router)
app.include_router(discount.router)
app.include_router(payment.router)

