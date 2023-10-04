from datetime import date
from batteries import NubbinBattery, SpindlerBattery
from engines import CapuletEngine, SternmanEngine, WilloughbyEngine
from tires import CarriganTire, OctoprimeTire
from car import Car


def create_calliope(
    current_date: date,
    last_service_date: date,
    current_mileage: int,
    last_service_mileage: int,
    worn_out: list[float],
) -> Car:
    battery = SpindlerBattery(current_date, last_service_date)
    engine = CapuletEngine(current_mileage, last_service_mileage)
    tire = CarriganTire(worn_out)

    return Car(engine, battery, tire)


def create_glissade(
    current_date: date,
    last_service_date: date,
    current_mileage: int,
    last_service_mileage: int,
    worn_out: list[float],
) -> Car:
    battery = SpindlerBattery(current_date, last_service_date)
    engine = WilloughbyEngine(current_mileage, last_service_mileage)
    tire = CarriganTire(worn_out)

    return Car(engine, battery, tire)


def create_palindrome(
    current_date: date,
    last_service_date: date,
    warning_light_on: bool,
    worn_out: list[float],
) -> Car:
    battery = SpindlerBattery(current_date, last_service_date)
    engine = SternmanEngine(warning_light_on)
    tire = OctoprimeTire(worn_out)

    return Car(engine, battery, tire)


def create_rorschach(
    current_date: date,
    last_service_date: date,
    current_mileage: int,
    last_service_mileage: int,
    worn_out: list[float],
) -> Car:
    battery = NubbinBattery(current_date, last_service_date)
    engine = WilloughbyEngine(current_mileage, last_service_mileage)
    tire = OctoprimeTire(worn_out)

    return Car(engine, battery, tire)


def create_thovex(
    current_date: date,
    last_service_date: date,
    current_mileage: int,
    last_service_mileage: int,
    worn_out: list[float],
) -> Car:
    battery = NubbinBattery(current_date, last_service_date)
    engine = CapuletEngine(current_mileage, last_service_mileage)
    tire = OctoprimeTire(worn_out)

    return Car(engine, battery, tire)
