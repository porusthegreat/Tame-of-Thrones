import sys


class InputReader:

    def __init__(self):
        self.input_list = {}
        self.read_input()

    def read_input(self):
        print('Enter number of messages that you want to send:\n')
        number_of_messages = int(sys.stdin.readline())

        print('Type Messages in \"kingdom, message\" format : \n')
        for i in range(number_of_messages):
            text = sys.stdin.readline()
            kingdom_name = text.split(',')[0]
            message = text.split(',')[1]
            self.add_messages(kingdom_name, message)

    def add_messages(self, kingdom, message):
        self.input_list[kingdom] = message

    def get_messages(self):
        return self.input_list
