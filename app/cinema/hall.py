from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


class CinemaHall:
    def __init__(self, number):
        self.number = number

    def movie_session(self, movie_name, customers: list, cleaning_staff: str):
        print(f"\"{movie_name}\" started in hall number {self.number}.")

        for customer in customers:
            customer.watch_movie(movie=movie_name)

        print(f"\"{movie_name}\" ended.")
        cleaner = Cleaner(name=cleaning_staff)
        cleaner.clean_hall(hall_number=self.number)
