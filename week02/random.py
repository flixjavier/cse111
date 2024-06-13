import random

def get_determiner(quantity):
    # """Return a randomly chosen determiner. A determiner is
    # a word like "the", "a", "one", "some", "many".
    # If quantity is 1, this function will return either "a",
    # "one", or "the". Otherwise this function will return
    # either "some", "many", or "the".
 
    # Parameter
    #     quantity: an integer.
    #         If quantity is 1, this function will return a
    #         determiner for a single noun. Otherwise this
    #         function will return a determiner for a plural
    #         noun.
    # Return: a randomly chosen determiner.
    # """
    if quantity == "single":
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
 
    # Randomly choose and return a determiner.
    word = random.choice(words)
 
    return word
 
 
def get_noun(quantity):
    # """Return a randomly chosen noun.
    # If quantity is 1, this function will
    # return one of these ten single nouns:
    #     "bird", "boy", "car", "cat", "child",
    #     "dog", "girl", "man", "rabbit", "woman"
    # Otherwise, this function will return one of
    # these ten plural nouns:
    #     "birds", "boys", "cars", "cats", "children",
    #     "dogs", "girls", "men", "rabbits", "women"
 
    # Parameter
    #     quantity: an integer that determines if
    #         the returned noun is single or plural.
    # Return: a randomly chosen noun.
    # """
    singular_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    plural_nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
 
    if quantity == "single":
        nouns = singular_nouns
    else:
        nouns = plural_nouns
 
    word = random.choice(nouns)
    return word
 
# print(get_noun(1))
 
 
def get_verb(quantity, tense):
    # """Return a randomly chosen verb.
 
    # Args:
    #     quantity: An integer that determines if the returned verb is singular or plural.
    #     tense: A string that determines the verb conjugation ("past", "present", or "future").
 
    # Returns:
    #     A randomly chosen verb.
    # """
 
# esto estaba en parentesis cuando debio estar en corchetes un "array"
    past_verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    present_singular_verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    present_plural_verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    future_verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
 
    if tense == "past":
        verbs = past_verbs
    elif tense == "present":
        if quantity == "single":
            verbs = present_singular_verbs
        else:
            verbs = present_plural_verbs
    elif tense == "future":
        verbs = future_verbs
    else:
        raise ValueError("Invalid tense. Please use 'past', 'present', or 'future'.")
 
    word = random.choice(verbs)
    return word
 
# print(get_verb(1, "present"))
 
def make_sentence(quantity, tense):
 
    #   """Build and return a sentence with three words:
    # a determiner, a noun, and a verb. The grammatical
    # quantity of the determiner and noun will match the
    # number in the quantity parameter. The grammatical
    # quantity and tense of the verb will match the number
    # and tense in the quantity and tense parameters.
    # """
 
    sentence = f"{get_determiner(quantity)} {get_noun(quantity)} {get_verb(quantity, tense)}"
    sentence.capitalize()
# setence = random.choice (sentence)
# sentence = make_sentence(get_Noun, get_verb, get_determiner)
    return sentence
 
 
def get_preposition():
 
    # """Return a randomly chosen preposition
    # from this list of prepositions:
    # "about", "above", "across", "after", "along",
    # "around", "at", "before", "behind", "below",
    # "beyond", "by", "despite", "except", "for",
    # "from", "in", "into", "near", "of",
    # "off", "on", "onto", "out", "over",
    # "past", "to", "under", "with", "without"
 
    # Return: a randomly chosen preposition.
    # """
    list_of_prepositions = ["about", "above", "across", "after", "along",
    "around", "at", "before", "behind", "below",
    "beyond", "by", "despite", "except", "for",
    "from", "in", "into", "near", "of",
    "off", "on", "onto", "out", "over",
    "past", "to", "under", "with", "without"]
 
    preposition = list_of_prepositions
    return random.choice(preposition)
 
 
def get_prepositional_phrase(quantity):
 
    # """Build and return a prepositional phrase composed
    # of three words: a preposition, a determiner, and a
    # noun by calling the get_preposition, get_determiner,
    # and get_noun functions.
 
    # Parameter
    # quantity: an integer that determines if the
    # determiner and noun in the prepositional
    # phrase returned from this function should
    # be single or pluaral.
    # Return: a prepositional phrase.
    # """
    # preposition = get_preposition()
    # determiner = get_determiner(1)
    # noun = get_noun(1)
 
        phrase = f"{get_preposition()} {get_determiner(quantity)} {get_noun(quantity)}"
        return phrase
# print(get_prepositional_phrase(1))
 
def main():
    quantity = input("Quantity: ")
    tense = input("Tense: ")
    sentence = make_sentence(quantity, tense)  # Example: singular, present tense
    prepositional_phrase = get_prepositional_phrase(quantity)
    return f"{sentence} {prepositional_phrase}"
 
print(main())

