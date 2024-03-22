PLACEHOLDER = '[name]'

with open('./Input/Names/invited_names.txt') as invited_names:
    names = invited_names.readlines()

with open('./Input/Letters/starting_letter.txt') as starting_letter:
    outline = starting_letter.read()
    for name in names:
        with open(f'./Output/ReadyToSend/{name.strip()}', mode='w') as completed_letter:
            new_letter = outline.replace(PLACEHOLDER, name.strip())
            completed_letter.write(new_letter)

