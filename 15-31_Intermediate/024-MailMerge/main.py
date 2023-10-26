from pathlib import Path
#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

cwd = Path.cwd()

with open(f"{cwd}\\024-MailMerge\\Input\\Names\\invited_names.txt", 'r') as name_file:
    for n in name_file:
        name = n.strip("\n")
        new_file_name = f"letter_for_{name}.txt"

        with open(f"{cwd}\\024-MailMerge\\Input\\Letters\\starting_letter.txt", 'r') as base_letter:
            letter = base_letter.readlines()
            intro = letter[0]
            intro = intro.replace("[name]", f"{name}")
            letter[0] = intro

            with open(f"{cwd}\\024-MailMerge\\Output\\ReadyToSend\\{new_file_name}", 'w') as new_letter:
                for line in letter:
                    new_letter.write(line)