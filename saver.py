import view
import controller
from datetime import datetime as dt
from time import time
def save_first_name(data):
    time = dt.now().strftime('%H:%M')
    with open ('dictionary.txt', 'a') as file:
        file.write('{}; first name;{}\n'
                .format(time, data))
def save_surname(data):
    time = dt.now().strftime('%H:%M')
    with open ('dictionary.txt', 'a') as file:
        file.write('{}; surname;{}\n'
                .format(time, data))
def save_description(data):
    time = dt.now().strftime('%H:%M')
    with open ('dictionary.txt', 'a') as file:
        file.write('{}; description;{}\n'
                .format(time, data))

