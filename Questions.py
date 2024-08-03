class Questions:
    # Class responsible to store the questions methods to be used in the main program
    # The methods are static and can be called without the need to instantiate the class
    # The methods are used to ask the user for input and return the value that will be used to generate the wordlist

    @staticmethod
    def ask_string():
        # Method to ask the user for a string to be used in the wordlist
        # The method will return the string provided by the user
        return input('Enter a string: ')

    @staticmethod
    def ask_number():
        # Method to ask the user for a number to be used in the wordlist
        # The method will return the number provided by the user
        return input('Enter a number: ')

    @staticmethod
    def ask_parents_names():
        # Method to ask the user for the parents names to be used in the wordlist
        # The method will return the parents names provided by the user
        return input('Enter the parents names: ')

    @staticmethod
    def ask_birth_year():
        # Method to ask the user for the birth year to be used in the wordlist
        # The method will return the birth year provided by the user
        return input('Enter the birth year: ')

    @staticmethod
    def ask_birth_month():
        # Method to ask the user for the birth month to be used in the wordlist
        # The method will return the birth month provided by the user
        return input('Enter the birth month: ')

    @staticmethod
    def ask_birth_day():
        # Method to ask the user for the birth day to be used in the wordlist
        # The method will return the birth day provided by the user
        return input('Enter the birth day: ')

    @staticmethod
    def ask_birth_city():
        # Method to ask the user for the birth city to be used in the wordlist
        # The method will return the birth city provided by the user
        return input('Enter the birth city: ')

    @staticmethod
    def ask_birth_country():
        # Method to ask the user for the birth country to be used in the wordlist
        # The method will return the birth country provided by the user
        return input('Enter the birth country: ')

    @staticmethod
    def ask_birth_place():
        # Method to ask the user for the birth place to be used in the wordlist
        # The method will return the birth place provided by the user
        return input('Enter the birth place: ')

    @staticmethod
    def ask_birth_street():
        # Method to ask the user for the birth street to be used in the wordlist
        # The method will return the birth street provided by the user
        return input('Enter the birth street: ')
