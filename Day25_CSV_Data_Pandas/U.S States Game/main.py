import turtle
import pandas

# def get_mouse_click_coordinate(x,y):
#     print(x,y)

# Read the csv
data_states = pandas.read_csv("50_states.csv")

# Create the screen
screen = turtle.Screen()
screen.title("U.S states name")

# Add the states image as background
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []


game_on = True
while len(guessed_states) < 50:
    
    # Prompt the user to insert it's option
    answer_state = screen.textinput(title=f"Guess a state {len(guessed_states)}/50 !", prompt="Guess another state name:").title()

    # Check if the state exist
    guessed_state = data_states[data_states.state == answer_state]

    if not guessed_state.empty:
        guessed_states.append(answer_state)
        # Extract information
        state_x_coor = guessed_state["x"].iloc[0]
        state_y_coor = guessed_state["y"].iloc[0]
        # Create the turtle object to print
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(state_x_coor, state_y_coor)
        t.write(answer_state)
    elif answer_state == "Exit":
        all_states = data_states.state.to_list()
        missing_states = []
        for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)
                
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break

    # Useful function to retrieve coordinates 
    #turtle.onscreenclick(get_mouse_click_coordinate)


# Keep the program running when clicking on screen
turtle.mainloop()