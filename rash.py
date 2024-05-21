import time
from abc import ABC
import random
from deck import  Deck
from tkinter import *
import tkinter

listbtn = []

class Player(ABC):
    def __init__(self, name):
        self.name = name
        self.list_current_maps = []

    def get_cards(self, current_deck, player):
        i = 1
        while i < 8:
            map = random.choice(current_deck)
            ind = current_deck.index(map)
            player.list_current_maps.append(map)
            current_deck.pop(ind)
            i += 1


    def get_card(self, current_deck):
        map = random.choice(current_deck)
        ind = current_deck.index(map)
        self.list_current_maps.append(map)
        current_deck.pop(ind)
        message = "Bot взял карту" + str(map)
        text_box.insert(END, message + '\n')



class Bot(Player):
    def __init__(self):
        super().__init__(name="Bot")

    def game(self, current_deck, current_map):
        while True:
            for i in self.list_current_maps:
                if i.option_von == current_map.main_number or i.option_two == current_map.main_number:
                    return i
            if len(current_deck) != 0:
                self.get_card(current_deck)
            else:
                break

    def game_bot(self):
        global current_map,current_deck,game_deck
        look_maps_bot = []
        
        count = 0
        for i in gamer.list_current_maps:
            if i == None:
                count += 1
        if count > 10:
            message = "победил " + gamer.name
            text_box.insert(END,message)
        else:
            if len(current_deck) < 2:
                print("колода пустая")
                ind = game_deck.index(current_map)
                game_deck.pop(ind)
                current_deck = game_deck.copy()
                game_deck = []
                game_deck.append(current_deck)

            if len(self.list_current_maps) > 1:

                map = self.game(current_deck, current_map)
                game_deck.append(map)
                current_map = map
                ind = self.list_current_maps.index(map)
                self.list_current_maps.pop(ind)

                for i in self.list_current_maps:
                    look_maps_bot.append(i.main_number)
                print(*look_maps_bot)
                mes = str(look_maps_bot)
                message = f"Игрок {self.name} кидает карту {current_map} "
                text_box.insert(END, message + '\n')
                if float(text_box.index(END)) > 20:
                    text_box.delete(1.0,END)

                look_maps_bot = []
                btn_curent.config(text=str(current_map.main_number) + "+-" + str(current_map.additional_number))
                root.after(100, self.game_bot)




            else:
                message = "победил " + self.name
                text_box.insert(END, message)


class Gamer(Player):
    def __init__(self, name):
        super().__init__(name=name)

    def game_player(self, button, card):
        count = 0
        global current_map

        if card != None:
            if card.option_von == current_map.main_number or card.option_two == current_map.main_number:
                btn_curent.configure(text=button.config().get('text')[4])
                button.config(text=" ")
                current_map = card
                ind = self.list_current_maps.index(current_map)
                game_deck.append(card)
                self.list_current_maps[ind] = None
                message = f"Игрок {self.name} кидает карту {current_map} "
                text_box.insert(END, message + '\n')
                self.update_card()






    def take_card(self):
        for i in range(len(self.list_current_maps)):
            if self.list_current_maps[i] is None and len(current_deck) > 0:
                card = random.choice(current_deck)
                self.list_current_maps[i] = card
                ind = current_deck.index(card)
                current_deck.pop(ind)
                message = f"Игрок {self.name} взял карту {card} "
                text_box.insert(END, message + '\n')
                break


        else:
            message = "колода полная!"
            text_box.insert(END, message + '\n')
        self.update_card()

    def update_card(self):
        for i in range(len(list_btn)):
            if self.list_current_maps[i] is None:
                list_btn[i].configure(text="")
            else:
                list_btn[i].configure(text=str(self.list_current_maps[i]))




class Paint_Card:
    def __init__(self):
        pass

    def paint_slot(self, card, xs, root, y):
        cell = Button(root, text=str(card), background="red", font=("Arial", 20),
                      width=10, height=6)
        cell.configure(command=lambda: gamer.game_player(cell, card))
        cell.place(x=xs, y= y)
        list_btn.append(cell)



deck = Deck()
deck.apend_maps()
deck.shufflelist()

current_deck = deck.list_map.copy()
current_map = random.choice(current_deck)
game_deck = []
game_deck.append(current_map)
bot = Bot()
gamer = Gamer("Колян")
gamer.get_cards(current_deck, gamer)
bot.get_cards(current_deck, bot)
look_maps_bot = []



xs = 0
root = Tk()
list_btn = []
btn_curent = Button(text='ddd', background="red", font=("Arial", 20), width=10,
                    height=6)
btn_curent.place(x=380, y=60)
for j in range(6):
    p = Paint_Card()

    p.paint_slot(gamer.list_current_maps[j], xs, root, 300)
    xs += 176

xs = 0
for j in range(6):
    gamer.list_current_maps.append(None)
    p = Paint_Card()
    p.paint_slot(" ", xs, root, 530)
    xs += 176

cell = Button(root, text="7x9", background="orange", font=("Arial", 20), width=10, height=6,
              command=gamer.take_card)
cell.place(x=880, y=60)

root.title("Game 7x9")
root.configure(background='green')
root.geometry('{}x{}'.format(root.winfo_screenwidth(),root.winfo_screenheight()))
text_box = Text(
    root,
    height=20,
    width=40
)
text_box.pack(expand=True)
text_box.insert('end', "")
text_box.place(x= 1150 , y= 100)




bot.game_bot()
root.mainloop()
