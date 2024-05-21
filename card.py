from abc import ABC

class Map:
    def __init__(self, additional_number, main_number):
        self.additional_number = additional_number
        self.main_number = main_number
        self.option_von = main_number + additional_number
        self.option_two = main_number - additional_number
        if self.option_von > 10:
            self.option_von -= 10
        if self.option_two < 1:
            self.option_two += 10

    def __str__(self):
        return f"{self.main_number}+-{self.additional_number}"


