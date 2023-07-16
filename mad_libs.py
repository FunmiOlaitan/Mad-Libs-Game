# imports the 'get_story' function from the story module
from stories import get_story

# promt the user for word inputs 
def prompt_word(word_type):
    return(f'Enter a {word_type}')

# generate the story based on those inputs 
def generate_story(adjective, noun1, verb1, adverb1, verb2, noun2, adjective2, verb3, adverb2, verb4, adjective3):
    story_template = get_story()
    story = story_template.replace("[ADJECTIVE]" ,adjective).replace("[NOUN]", noun1).replace("[VERB]", verb1).replce("[ADVERB]", adverb1).replace("[VERB]", verb2).replace("[NOUN]", noun2).replace("[ADJECTIVE]", adjective2).replace("[VERB]", verb3).replace("[ADVERB]", adverb2).replace("[VERB]", verb4).replace("[ADJECTIVE]", adjective3)
    return story

# print the final story
def play_mad_libs_game()
    adjective = prompt_word("adjective")
    noun1 = prompt_word("noun")
    verb1 = prompt_word("verb")
    adverb1 = prompt_word("adverb")
    verb2 = prompt_word("verb")
    noun2 = prompt_word("noun")
    adjective2 = prompt_word("adjective")
    verb3 = prompt_word("verb")
    adverb2 = prompt_word("adverb")
    verb4 = prompt_word("verb")
    adjective3 = prompt_word("adjective")

    story = generate_story(adjective, noun1, verb1, adverb1, verb2, noun2, adjective2, verb3, adverb2, verb4, adjective3)
    print("\nYour Mad Libs Story:")
    print(story)

play_mad_libs_game()