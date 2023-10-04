from engine import Engine
from battery import Battery
from abc import ABC, abstractmethod


class Serviceable(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass


class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery):
        # self.last_service_date = last_service_date
        self._engine: Engine = engine
        self._battery: Battery = battery

    def needs_service(self) -> bool:
        return self._engine.needs_service() or self._battery.needs_service()
