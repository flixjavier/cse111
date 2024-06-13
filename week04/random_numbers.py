import random
def main():
    #orginal list
    numbers = [16.2, 75.1, 52.3, 55.3, 22, 33.4 , 443.2, 233.2]
    words = ["mountain", "river", "forest", "desert", "ocean", "valley", "island", "glacier", "volcano", "waterfall"]

    dealers_choice = int(input("What number do you want to add? "))
    index = int(input("What is your favorite number between 1-5? "))
    print(numbers)

    append_random_numbers(numbers)
    #print appended list
    print(numbers)

    append_random_numbers(numbers, 3)
    print(numbers)

    append_random_words(words)
    #print appended list
    print(words)

    append_random_words(words, 3)
    print(words)

    replace_random_words(words)
    print(words)

    replace_random_words(words, 3)
    print(words)

    replace_random_number(numbers, dealers_choice, index)
    print(numbers)

    dealers_choice = int(input("What number do you want to add? "))
    index = int(input("What is your favorite number between 1-5? "))

    replace_random_number(numbers, dealers_choice, index)
    print(numbers)

def append_random_numbers(numbers_list, quantity=1):
    count = 0
    while count < quantity:
        random_number = round(random.uniform(0,100),1)
        # print(random_number)
        numbers_list.append(random_number)
        count +=1

def append_random_words(words_list, quantity=1):
    list_of_words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
    count = 0
    while count < quantity:
        random_index = int(random.uniform(0, len(list_of_words)))
        # print(random_index)
        random_word = list_of_words[random_index]
        # print(random_word)
        words_list.append(random_word)
        count +=1

def replace_random_words(list_words, index=0):
    list_of_words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
    if len(list_words) < 0:
        print("No List")
    else:
        list_words[index] = list_of_words[index]


def replace_random_number(list_num, dealers_choice, index=0):
    if len(list_num) < 0 and index < len(list_num):
        print("No List or invalid index")
    else:
        list_num[index] = round(dealers_choice,1)

if __name__ == "__main__":
    main()