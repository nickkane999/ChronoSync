import keyboard
from GameKeyListener import GameKeyListener
from Actor import Actor
from Macros import Macros

macros = Macros()
actor = Actor(macros)
key_listener = GameKeyListener(actor)

# Listen for all key events and print their information
keyboard.on_press(key_listener.processKey)
keyboard.wait('esc')
