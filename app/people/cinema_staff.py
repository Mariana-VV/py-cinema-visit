class Cleaner:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"{self.name}"

    def clean_hall(self, hall_number):
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")
