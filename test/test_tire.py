import unittest

from src.tires import CarriganTire, OctoprimeTire


class TestCarriganTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        worn_out = [0.1, 0.2, 0.3, 0.9]

        tire = CarriganTire(worn_out)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        worn_out = [0.1, 0.2, 0.3, 0.4]

        tire = CarriganTire(worn_out)
        self.assertFalse(tire.needs_service())


class TestOctoprimeTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        worn_out = [1, 1, 0.6, 0.7]

        tire = OctoprimeTire(worn_out)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        worn_out = [0.1, 0.2, 0.3, 0.9]

        tire = OctoprimeTire(worn_out)
        self.assertFalse(tire.needs_service())
