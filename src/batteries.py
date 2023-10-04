from abc import ABC, abstractmethod
from datetime import date, datetime


class Battery(ABC):
    @abstractmethod
    def needs_service() -> bool:
        pass


class SpindlerBattery(Battery):
    def __init__(self, current_date: date, last_service_date: date) -> None:
        self._last_service_date: date = last_service_date
        self._current_date: date = current_date

    def needs_service(self) -> bool:
        thredshold = self._last_service_date.replace(
            year=self._last_service_date.year + 2
        )

        return thredshold < self._current_date


class NubbinBattery(Battery):
    def __init__(self, current_date: date, last_service_date: date) -> None:
        self._last_service_date: date = last_service_date
        self._current_date: date = current_date

    def needs_service(self) -> bool:
        thredshold = self._last_service_date.replace(
            year=self._last_service_date.year + 4
        )

        return thredshold < self._current_date
