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