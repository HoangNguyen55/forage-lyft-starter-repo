from abc import ABC, abstractmethod


class Tire(ABC):
    @abstractmethod
    def needs_service() -> bool:
        pass


class CarriganTire(Tire):
    def __init__(self, worn_out: list[float]) -> None:
        self._worn_out = worn_out

    def needs_service(self) -> bool:
        for i in self._worn_out:
            if i >= 0.9:
                return True
        return False


class OctoprimeTire(Tire):
    def __init__(self, worn_out: list[float]) -> None:
        self._worn_out = worn_out

    def needs_service(self) -> bool:
        total = sum(self._worn_out)
        return total >= 3
