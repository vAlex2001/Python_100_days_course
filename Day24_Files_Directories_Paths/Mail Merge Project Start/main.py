#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

# Save the letter template
with open("./Input/Names/invited_names.txt") as names_input_file:
    names = names_input_file.readlines()


with open("./Input/Letters/starting_letter.txt") as letter_input_file:
    letter_template = letter_input_file.read()
    # Create the letters
    for name in names:
        stripepd_name = name.strip()
        new_letter = letter_template.replace(PLACEHOLDER, stripepd_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripepd_name}.docx", mode="w") as complete_letter:
            complete_letter.write(new_letter)
        