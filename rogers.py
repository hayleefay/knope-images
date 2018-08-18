import re
import random
import string
translator = str.maketrans('', '', string.punctuation)

STATEMENTS = {
    'I am (.*)': ['Did you come to me because you are %s?',
                  'Do you enjoy being %s?']
}

print('Dr. Eliza is in. Type exit if you want the session to end.\
       You will be billed.')

user_response = input('Hello, I am Dr. Eliza. What seems to be the problem?\n')

while user_response != 'exit':
    last_response = user_response

    for key, value in STATEMENTS.items():
        is_match = re.match(key, user_response)
        if is_match:
            eliza_response = random.choice(STATEMENTS[key])
            user_response = input(eliza_response % (is_match.group(1).translate(translator)) + '\n')
        else:
            user_response = input('Tell me more.\n')

    # save last response, if the same, say "Don't repeat yourself"
    if user_response == last_response:
        print("Don't repeat yourself, please.")
