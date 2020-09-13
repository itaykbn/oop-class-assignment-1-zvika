import logging
import json
import random
logging.basicConfig(filename='log.log', level=logging.DEBUG)


class HelpTools:
    @staticmethod
    def clear_log(name):
        with open(name, 'w'):
            pass

    @staticmethod
    def add_to_log(alert_type, message):
        logging.log(alert_type, message)

    @staticmethod
    def delete_log_dialog():
        while True:
            delete_log = input("do you want to delete previous log? enter y/n")
            if delete_log == 'y':
                HelpTools.clear_log('log.log')
                break
            elif delete_log == 'n':
                break
            else:
                print("invalid input")

    @staticmethod
    def turn_dict_to_string(dictionary):
        result = json.dumps(dictionary)
        return result

    @staticmethod
    def generate_random_color():
        color_list = ['blue', 'red', 'white', 'black', 'green', 'orange', 'pink', 'purple', 'yellow', 'gray']
        return color_list[random.randint(0, 9)]
