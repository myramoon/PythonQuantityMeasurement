import logging
from main.IQuantityMeasurement import IQuantityMeasurementSystem

logging.basicConfig(filename='log_quantity_measurement.log',level=logging.DEBUG, format='%(name)s | %(levelname)s | %(message)s')

class QuantityMeasurementSystem(IQuantityMeasurementSystem):

    def __init__(self):
        self.M_TO_CM = 100
        self.M_TO_KM = .001
        self.G_TO_KG = .001
        self.G_TO_MG = 1000
        self.CF_TEMP_CONVERSION = 32
        self.CK_TEMP_COVERSION =273.15


    def convert_m_to_cm_length(self, input_length):
        """
        :param input_length:  length in meters
        :return: length in centimeters or exception
        """
        try:
            centi_meter_length = round((input_length * self.M_TO_CM), 2)
            logging.debug('meter to centimeter: {}'.format(centi_meter_length))
            return centi_meter_length
        except TypeError:
            logging.exception('Exception due to wrong input type')
            print("Please enter a number")

    def convert_m_to_km_length(self, input_length):
        """
        :param input_length:  length in meters
        :return: length in kilometers or exception
        """
        try:
            kilo_meter_length = round((input_length * self.M_TO_KM), 2)
            logging.debug('meter to kilometer: {}'.format(kilo_meter_length))
            return kilo_meter_length
        except TypeError:
            logging.exception('Exception due to wrong input type')
            print("Please enter a number")

    def convert_g_to_kg_weight(self, input_weight):
        """
        :param input_weight: weight in grams
        :return: weight in kilograms or exception
        """
        try:
            kilo_gram_weight = round((input_weight * self.G_TO_KG), 2 )
            logging.debug('gram to kilogram: {}'.format(kilo_gram_weight))
            return kilo_gram_weight
        except TypeError:
            logging.exception('Exception due to wrong input type')
            print("Please enter a number")


    def convert_g_to_mg_weight(self, input_weight):
        """
        :param input_weight: weight in grams
        :return: weight in milligrams or exception
        """
        try:
            milli_gram_weight = round((input_weight * self.G_TO_MG), 2 )
            logging.debug('gram to milligram: {}'.format(milli_gram_weight))
            return milli_gram_weight
        except TypeError:
            logging.exception('Exception due to wrong input type')
            print("Please enter a number")

    def convert_celsius_to_fahrenheit_temperature(self, input_temperature):
        """
        :param input_temperature: temperature in celsius
        :return: temperature in fahrenheit or exception
        """
        try:
            fahrenheit_temperature = round((((9 / 5) * input_temperature) + self.CF_TEMP_CONVERSION), 2 )
            logging.debug('celsius to fahrenheit: {}'.format(fahrenheit_temperature))
            return fahrenheit_temperature
        except TypeError:
            logging.exception('Exception due to wrong input type')
            print("Please enter a number")


    def convert_fahrenheit_to_celsius_temperature(self, input_temperature):
        """
        :param input_temperature: temperature in fahrenheit
        :return: temperature in celsius or exception
        """
        try:
            celsius_temperature = round(((input_temperature - self.CF_TEMP_CONVERSION) * (5 / 9)), 2)
            logging.debug('fahrenheit to celsius: {}'.format(celsius_temperature))
            return celsius_temperature
        except TypeError:
            logging.exception('Exception due to wrong input type')
            print("Please enter a number")


    def convert_celsius_to_kelvin_temperature(self, input_temperature):
        """
        :param input_temperature: temperature in celsius
        :return: temperature in kelvin or exception
        """
        try:
            kelvin_temperature = round((input_temperature + self.CK_TEMP_COVERSION), 2)
            logging.debug('celsius to kelvin: {}'.format(kelvin_temperature))
            return kelvin_temperature
        except TypeError:
            logging.exception('Exception due to wrong input type')
            print("Please enter a number")


    def convert_kelvin_to_celsius_temperature(self, input_temperature):
        """
        :param input_temperature: temperature in kelvin
        :return: temperature in celsius or exception
        """
        try:
            celsius_temperature = round((input_temperature - self.CK_TEMP_COVERSION), 2)
            logging.debug('kelvin to celsius: {}'.format(celsius_temperature))
            return celsius_temperature
        except TypeError:
            logging.exception('Exception due to wrong input type')
            print("Please enter a number")


    def convert_fahrenheit_to_kelvin_temperature(self, input_temperature):
        """
        :param input_temperature: temperature in fahrenheit
        :return: temperature in kelvin or exception
        """
        try:
            kelvin_temperature = round(((input_temperature - self.CF_TEMP_CONVERSION) * (5 / 9)) + self.CK_TEMP_COVERSION, 2)
            logging.debug('fahrenheit to kelvin: {}'.format(kelvin_temperature))
            return kelvin_temperature
        except TypeError:
            logging.exception('Exception due to wrong input type')
            print("Please enter a number")


    def convert_kelvin_to_fahrenheit_temperature(self, input_temperature):
        """
        :param input_temperature: temperature in kelvin
        :return: temperature in fahrenheit or exception
        """
        try:
            fahrenheit_temperature = round(((input_temperature - self.CK_TEMP_COVERSION) * (9 / 5)) + self.CF_TEMP_CONVERSION, 2)
            logging.debug('kelvin to fahrenheit: {}'.format(fahrenheit_temperature))
            return fahrenheit_temperature
        except TypeError:
            logging.exception('Exception due to wrong input type')
            print("Please enter a number")


