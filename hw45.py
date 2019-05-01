# Team AwesomeSauce - Agata Regula, Abir Taheer
# IntroCS pd1
# HW45 -- ...Love It When a Plan Comes Together...
# 2019-05-01

"""
Mechanism for Madlibification:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The Double Loop Method:

We would have variables containing lists with all of the nouns and verbs, etc.
We’d loop through the input mad lib template once, first to see how many of each type of word we need.
We then prompt the user for each specific type of word the number of times it appears.
After doing that, we loop through the entire template again and fill it in with words from the user.

The inputs would be:
The basic string. (madlib)
Lists made up of nouns, verbs, adjectives, adverbs, numbers, etc
This is under the assumption that each part of speech required by the paragraph has its own list.
Ex.
    Nouns = [‘apples’, ‘dogs’, ‘pizza’]
    Verbs = [‘run’, ‘drink’, ‘cry’]
    Adjectives = [‘green’, ‘crazy’, ‘yummy’, ‘sleepy’]
Something that needs to be taken under consideration is whether the word needed and provided is plural or singular.
The words from the list would be randomly selected and then deleted from the list as to not be repeated again.

Steps:
1. Make counters for # of necessary verbs and nouns and etc

2. Make variables to store the nouns, verbs, adjectives, etc from the user

3. Use split and split up the mad lib template at all of the spaces to get a list of all of the words.

4. Iterate through the list of all of the words.

5. If a word’s first and last letter are opening and closing gang brackets, respectively,
look at what type of filler word is needed and increment the counter for that type of word.

6. Prompt the user, the number of times in each counter, for each type of word and add it to the
appropriate list every time.

7. Iterate through the original list of words again and every time the gang brackets appear, choose a word from the
appropriate list and replace it with the list item containing the gang brackets.

8. Remove the item that was used from whichever list it was retrieved from to prevent duplicates and missing words.

9. Join together the list of words from the template using the space as the separator
"""

import random

# A bunch of test cases containing the madlibs
test_stories = [
    'They went to the park and had <noun>',
    'A <noun> and a <noun> <verb> <noun> <adverb>',
    'They went to the <noun> and had <noun> for breakfast while <verb>',
    'I <adverb> washed my <adjective> <noun> before I had to eat the <adjective> <noun>'
]

# Setup our lists of the different parts of speech
nouns = ['cat', 'book', 'leg', 'bobblehead', 'turtle', 'hat', 'spigot', 'bar of gold', 'bag', 'nugget', 'watch',
         'flower', 'furnace', 'fire', 'pimple', 'brownie']  # possible input nouns
verbs = ['find', 'eat', 'become', 'run', 'watch', 'attack', 'repeat', 'leap', 'peel', 'morph', 'sing', 'roll',
         'caress']  # possible verbs
adjectives = ['large', 'red', 'scaly', 'mean', 'funny', 'blue', 'greedy', 'awe-inspiring', 'cool-with-a-k',
              'argumentative', 'pained', 'oblivious', 'slimy', 'girthy', 'gnarly']  # possible adjectives
adverbs = ['hungrily', 'quickly', 'smartly', 'cunningly', 'secretly', 'deftly', 'amazingly', 'daintily',
           'sloppily']  # possible adverbs


full_story = "Today I went to the zoo. I saw a <adjective> <noun> jumping up and down in its tree. He " \
             "<verb> <adverb> through the large tunnel <adjective> <noun>. I got some peanuts" \
             " and passed them through the case to a gigantic gray <noun> towering above my head. " \
             "Feeding that animal made me hungry. I wet to get a <adjective> scoop of ice cream. " \
             "It filled my stomach. Afterwards I had to <verb> to catch our bus. When I got " \
             "home I asked my mom for a <adjective> day at the zoo."


def fill_blanks(story):
    """
    Replaces the blanks in a string with the appropriate word types.

    :param story: The string in which to replace the blanks
    :returns: The new string without any of the blanks

    """
    # First we separate the story into the words that make it up
    words = story.split(" ")

    # Loop through all of the words, looking for any of the blanks
    for word_index in range(len(words)):
        # Store the current word in a variable since we'll be referencing it a lot
        # Make it lowercase for better searching
        word = words[word_index].lower()

        # Depending on which type of blank of the current word, set a variable word_list equal to the appropriate
        # word bank to replace the word with
        if "<noun>" in word:
            match = "<noun>"
            word_list = nouns
        elif "<verb>" in word:
            match = "<verb>"
            word_list = verbs
        elif "<adjective>" in word:
            match = "<adjective>"
            word_list = adjectives
        elif "<adverb>" in word:
            match = "<adverb>"
            word_list = adverbs
        else:
            # If the word is not a blank, then the word bank is equal to just the word itself, the word does not get
            # replaced
            match = word
            word_list = [word]

        # Replace the current word we're checking with a random word from word_list
        words[word_index] = words[word_index].replace(match, word_list[random.randrange(len(word_list))])

    # Once all the words have been checked, return the new list of words, concatenated into a string separated by spaces
    return ' '.join(words)


def test_fill_blanks():
    """
    Tests our fill_blanks function with predefined test cases
    :returns: -1 if all of the tests succeeded or the index of the first story to fail
    """

    # Check the function for each of our test_stories
    for story_index in range(len(test_stories)):

        # Set the current story being tested to a variable
        test_story = test_stories[story_index]

        # Call our fill_blanks function with the test story and store the returned value in a variable
        result = fill_blanks(test_story)

        # Print it to the terminal so that we can see it for the lulz
        print(result)

        # Check if the returned value still contains any of the blanks
        for x in ["<noun>", "<verb>", "<adjective>", "<adverb>"]:
            # In the case that one of the blanks is found, return the index of the test story that failed
            if x in result.lower():
                return story_index

    # If all of the different blank types were searched and they not appear in the returned value,
    # the test succeeded, return -1
    return -1


print(fill_blanks(full_story))
# First run hehe:
# they went to the park and had pizza
# a cat and a house run house badly
# they went to the cat and had cat for breakfast while cry
# i quickly washed my red sheep before i had to eat the sweaty house

