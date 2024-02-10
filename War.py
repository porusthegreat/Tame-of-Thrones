from Kingdom import Kingdom


class War:

    def __init__(self):
        self.allies = []
        self.switcher = {
            'air': Kingdom('air', 'owl'),
            'water': Kingdom('water', 'octopus'),
            'land': Kingdom('land', 'panda'),
            'fire': Kingdom('fire', 'dragon'),
            'ice': Kingdom('ice', 'mammoth')
        }

    def get_kingdom(self, argument):
        """
        :rtype: object
        """
        return self.switcher.get(argument)

    def verify_message_for_all_kingdoms(self, input_dictionary):
        for kingdom_in_message in input_dictionary:
            if kingdom_in_message in self.switcher:
                kingdom = self.get_kingdom(kingdom_in_message)
                ally = kingdom.get_kingdom_name_if_defeated(input_dictionary, kingdom_in_message)

                if ally is not None:
                    self.allies.append(ally)

    def get_allies(self):
        print(self.allies)
        return self.allies

