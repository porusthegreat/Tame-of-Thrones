from StringCount import Count


class Kingdom:

    def __init__(self, name, emblem):
        self.__name = name
        self.__emblem = emblem

    def get_emblem(self):
        return self.__emblem

    def get_name(self):
        return self.__name

    def get_character_count_for_emblem(self):
        return Count(self.get_emblem()).count_letters()

    def is_kingdom_defeated(self, message_count):
        val = True
        for char in str(self.get_emblem()):
            if char not in message_count or message_count.get(char) < self.get_character_count_for_emblem().get(char):
                val = False

        return val

    def get_kingdom_name_if_defeated(self, input_dict, kingdom_in_message):
        message_count = Count(input_dict[kingdom_in_message]).count_letters()
        is_defeated = self.is_kingdom_defeated(message_count)

        if is_defeated:
            return kingdom_in_message
