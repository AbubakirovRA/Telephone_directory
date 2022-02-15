import view
import saver
import reader
import generator_data

def start_programm(user_choice):
    if user_choice == 'f':
        view.view_data(reader.find_data(view.get_data('Enter data to search: ')), 'data')
    elif user_choice == 'a':
        saver.save_data(view.get_data('Enter data to add: '))
    elif user_choice == 'e':
        generator_data.export(view.get_data('Enter a file name to export to csv format: '))
    elif user_choice == 'i':
        saver.add_data(view.get_data('Enter a file name for data import: '))