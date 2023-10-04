from engines import Engine
from batteries import Battery
from tires import Tire
from abc import ABC, abstractmethod


class Serviceable(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass


class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery, tire: Tire):
        # self.last_service_date = last_service_date
        self._engine: Engine = engine
        self._battery: Battery = battery
        self._tire: Tire = tire

    def needs_service(self) -> bool:
        return (
            self._engine.needs_service()
            or self._battery.needs_service()
            or self._tire.needs_service()
        )
