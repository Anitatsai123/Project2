from gpiozero import Button
from signal import pause
#https://gpiozero.readthedocs.io/en/stable/recipes.html#button
def say_hello():
    print("Hello!")

def say_goodbye():
    print("Goodbye!")

button = Button(18) #號碼對應GPIO實體接線位置

button.when_pressed = say_hello
button.when_released = say_goodbye

pause()