#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


 

with open("./Input/Names/invited_names.txt") as names:
    letter_to_string = ""
    name_list = names.readlines()
    for name in name_list:
        with open("./Input/Letters/starting_letter.txt") as letter:
            new_letter = letter.readlines()
        new_name = name.strip()
        greeting = new_letter[0].replace("[name]", new_name)
        print("greeting line:"+ greeting)
        letter_to_string = greeting + ''.join(new_letter[1:]) 
        # print(letter_to_string)
        with open("./Output/ReadyToSend/letter_for_" + name + ".txt", "w") as file:
            file.write(letter_to_string)
            
        # pass


