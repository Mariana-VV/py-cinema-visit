class Customer:
    def __init__(self, name, food) -> None:
        self.name = name
        self.food = food

    def __repr__(self) -> str:
        return self.name

    def watch_movie(self, movie: str) -> str:
        print(f"{self.name} is watching \"{movie}\".")
