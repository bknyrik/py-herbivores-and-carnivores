class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        self.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, herbivore_animal: Herbivore) -> None:
        if (not herbivore_animal.hidden
                and herbivore_animal.health
                and isinstance(herbivore_animal, Herbivore)):
            herbivore_animal.health -= 50

        if herbivore_animal.health <= 0:
            self.alive.remove(herbivore_animal)
