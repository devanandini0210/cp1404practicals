from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        Taxi.price_per_km *= fanciness

    def __str__(self):
        return f"{super().__str__()}, plus flagfall of {self.flagfall}"

    def get_fare(self):
        return super().get_fare()+self.flagfall
