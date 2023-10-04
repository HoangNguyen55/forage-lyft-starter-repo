from datetime import date
from battery import NubbinBattery, SpindlerBattery
from car import Car
from engine import CapuletEngine, SternmanEngine, WilloughbyEngine


def create_calliope(
    current_date: date,
    last_service_date: date,
    current_mileage: int,
    last_service_mileage: int,
) -> Car:
    battery = SpindlerBattery(current_date, last_service_date)
    engine = CapuletEngine(current_mileage, last_service_mileage)

    return Car(engine, battery)


def create_glissade(
    current_date: date,
    last_service_date: date,
    current_mileage: int,
    last_service_mileage: int,
) -> Car:
    battery = SpindlerBattery(current_date, last_service_date)
    engine = WilloughbyEngine(current_mileage, last_service_mileage)

    return Car(engine, battery)


def create_palindrome(
    current_date: date, last_service_date: date, warning_light_on: bool
) -> Car:
    battery = SpindlerBattery(current_date, last_service_date)
    engine = SternmanEngine(warning_light_on)

    return Car(engine, battery)


def create_rorschach(
    current_date: date,
    last_service_date: date,
    current_mileage: int,
    last_service_mileage: int,
) -> Car:
    battery = NubbinBattery(current_date, last_service_date)
    engine = WilloughbyEngine(current_mileage, last_service_mileage)

    return Car(engine, battery)


def create_thovex(
    current_date: date,
    last_service_date: date,
    current_mileage: int,
    last_service_mileage: int,
) -> Car:
    battery = NubbinBattery(current_date, last_service_date)
    engine = CapuletEngine(current_mileage, last_service_mileage)

    return Car(engine, battery)
