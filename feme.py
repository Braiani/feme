import Export as Exporter
import Questions
import Utils


string_list = []
numbers_list = []


def show_menu(show_draw=True):
    if show_draw:
        Utils.Utils().show_draw()

    print('''
    +-------------------------+
    | 1. Start Generation     |
    | 2. Show List of Answers |
    | 3. Exit                 |
    +-------------------------+
    ''')


def start_generation():
    print('Starting generation... Preparing the questions...')
    try:
        string_list.append(Questions.Questions.ask_string())
        numbers_list.append(Questions.Questions.ask_number())
        string_list.append(Questions.Questions.ask_parents_names())
        numbers_list.append(Questions.Questions.ask_birth_year())
        string_list.append(Questions.Questions.ask_birth_month())
        string_list.append(Questions.Questions.ask_birth_day())
        string_list.append(Questions.Questions.ask_birth_city())
        string_list.append(Questions.Questions.ask_birth_country())
        string_list.append(Questions.Questions.ask_birth_place())
        string_list.append(Questions.Questions.ask_birth_street())
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print()
        print('Generation interrupted')
        return


if __name__ == '__main__':
    try:
        first_run = True
        while True:
            show_menu(first_run)
            choice = input('Enter your choice: ')
            first_run = False

            if choice == '1':
                start_generation()
            elif choice == '2':
                print('Showing the list of answers...')
                print('String list:', string_list)
                print('Numbers list:', numbers_list)
            elif choice == '3':
                break
            else:
                print('Invalid choice')
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print()
        print('Closing the program...')