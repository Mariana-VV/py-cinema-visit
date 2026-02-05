from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    hall = CinemaHall(hall_number)

    new_customers = []
    for customer in customers:
        temp = Customer(name=customer["name"], food=customer["food"])
        new_customers.append(temp)

    for customer in customers:
        CinemaBar.sell_product(product=customer["food"], customer=customer["name"])

    hall.movie_session(movie, new_customers, cleaner)
