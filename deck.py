import random
from card import Map


class Deck:
    def __init__(self):
        self.list_map = []

    def display(self):
        for j in self.list_map:
            print("карта " + str(j.main_number) + " с дополнительной цифрой " + str(j.additional_number))

    def apend_maps(self):
        i = 1
        while i < 11:
            ob = Map(1,i)
            self.list_map.append(ob)
            i += 1

        i = 1
        while i < 11:
            ob = Map(2,i)
            self.list_map.append(ob)
            i += 1

        i = 1
        while i < 11:
            ob = Map(3,i)
            self.list_map.append(ob)
            i += 1

        i = 1
        while i < 11:
            ob = Map(1,i)
            self.list_map.append(ob)
            i += 1

        i = 1
        while i < 11:
            ob = Map(2,i)
            self.list_map.append(ob)
            i += 1

        i = 1
        while i < 11:
            ob = Map(3,i)
            self.list_map.append(ob)
            i += 1

        i = 1
        while i < 11:
            if i < 5:
                ob = Map(1,i)
                self.list_map.append(ob)
            if 5 <= i < 9:
                ob = Map(2,i)
                self.list_map.append(ob)

            if i > 8:
                ob = Map(3,i)
                self.list_map.append(ob)

            i += 1

        i = 1
        while i < 8:
            if i < 5:
                ob = Map(3,i)
                self.list_map.append(ob)

            if i >= 5:
                ob = Map(4,i)
                self.list_map.append(ob)
                self.list_map.append(ob)

            i += 1
    def shufflelist(self):
        random.shuffle(self.list_map)


