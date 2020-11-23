from abc import ABC , abstractmethod


class IQuantityMeasurementSystem(ABC):
    @abstractmethod
    def convert_m_to_cm_length(self, input_length):
        pass

    @abstractmethod
    def convert_m_to_km_length(self, input_length):
        pass

    @abstractmethod
    def convert_g_to_kg_weight(self, input_weight):
        pass

    @abstractmethod
    def convert_g_to_mg_weight(self, input_weight):
        pass

    @abstractmethod
    def convert_celsius_to_fahrenheit_temperature(self, input_temperature):
        pass

    @abstractmethod
    def convert_fahrenheit_to_celsius_temperature(self, input_temperature):
        pass

    @abstractmethod
    def convert_celsius_to_kelvin_temperature(self, input_temperature):
        pass

    @abstractmethod
    def convert_kelvin_to_celsius_temperature(self, input_temperature):
        pass

    @abstractmethod
    def convert_fahrenheit_to_kelvin_temperature(self, input_temperature):
        pass

    @abstractmethod
    def convert_kelvin_to_fahrenheit_temperature(self, input_temperature):
        pass
