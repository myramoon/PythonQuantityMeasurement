import pytest
from main.quantity_measurement_system import QuantityMeasurementSystem


@pytest.fixture
def instance_of_main_class():
    quantity_measurement_system = QuantityMeasurementSystem()
    return quantity_measurement_system
