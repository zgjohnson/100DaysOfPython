import turtle

import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
state_name = turtle.Turtle()
state_name.pu()
state_name.hideturtle()
state_df = pandas.read_csv('50_states.csv')
states_guessed = []

score = 0
while score < 50:

    guess = str(screen.textinput(title=f'{score}/50 States Guessed Correctly', prompt='Guess a state!')).title()
    if guess == 'Exit':
        states_to_learn = [state for state in state_df.state.to_list() if state not in states_guessed]
        pandas.DataFrame(states_to_learn, columns=['State']).to_csv('state_to_learn.csv')
        break
    state = state_df[state_df.state == guess]
    if not state.empty and state.state.item() not in states_guessed:
        score += 1
        states_guessed.append(state.state.item())
        state_name.goto(state.x.item(), state.y.item())
        state_name.write(guess, align='Center', font=('Arial', 8, 'normal'))




