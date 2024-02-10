from InputReader import InputReader
from War import War


class WarService:
    input_dict = InputReader().get_messages()
    war = War()
    war.verify_message_for_all_kingdoms(input_dict)
    war.get_allies()
