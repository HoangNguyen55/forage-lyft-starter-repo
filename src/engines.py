from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def needs_service() -> bool:
        pass


class CapuletEngine(Engine):
    def __init__(self, current_mileage: int, last_service_mileage: int) -> None:
        self._current_mileage: int = current_mileage
        self._last_service_mileage: int = last_service_mileage

    def needs_service(self) -> bool:
        return self._current_mileage - self._last_service_mileage > 30000


class WilloughbyEngine(Engine):
    def __init__(self, current_mileage: int, last_service_mileage: int) -> None:
        self._current_mileage: int = current_mileage
        self._last_service_mileage: int = last_service_mileage

    def needs_service(self) -> bool:
        return self._current_mileage - self._last_service_mileage > 60000


class SternmanEngine(Engine):
    def __init__(self, warning_light_on: bool) -> None:
        self._warning_light_on: bool = warning_light_on

    def needs_service(self) -> bool:
        return self._warning_light_on
