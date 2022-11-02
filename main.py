import csv

#Prompt Column has been trimmed
csv_filename = 'LowerEng2Nah_Nah2Eng_Combined.csv'

dict_Nah_2_Eng_Eng2Nah = {} # Declare Empty Dictionary


#Created a function to prompt the user for input to be translated and check
# the dictionary to see if the value is available if not it will let the user
# and ask if another translation would be desired. If they user Enters 1 then it will continue , 2 it will terminate

def translationRequest():
    # Need a function to repeat this
    transRqst = True

    while transRqst:
        prompt = input('What do you want to say: ')
        # prompt = prompt.strip()

        if prompt in dict_Nah_2_Eng_Eng2Nah:
            print(dict_Nah_2_Eng_Eng2Nah[prompt])
        else:
            print("The translation is not available")

        checkRqst = input('Translate Another ? \n Enter 1(Yes) or 2(No): ')
        if checkRqst == '1':
            transRqst = True

            #Check if input is 2 if so end the loop
        elif checkRqst =='2':
            print("Terminating program, Good-Bye")
            break
            #If 1 or 2 not entered then repeat process
        elif not checkRqst =='1' and not checkRqst == '2':
            print("1 or 2 was not entered \n")
            transRqst == True





# with open(csv_filename, encoding='utf-8-sig') as f:
#     reader = csv.DictReader(f)
#
#     for row in reader:
#          print(row)

# with open(csv_filename, mode = 'r', encoding='utf-8-sig') as infile:
#     reader = csv.reader(infile)
#     with open ('NewHgFcNah2Eng.csv', mode = 'w') as outfile:
#         writer = csv.writer(outfile)
#         dict_Eng_2_Nah = {for rows in reader}


#Open the csv reader and cut off unnecessary chars in CSV
reader = csv.reader(open(csv_filename, 'r', encoding='utf-8-sig'))
#For each Key : Value pair write it to the dictionary
for k,v in reader:
    #k,v=row
    dict_Nah_2_Eng_Eng2Nah[k]=v



print(dict_Nah_2_Eng_Eng2Nah)

translationRequest()
#Need a function to repeat this
#transRqst = True

# while transRqst:
#     prompt = input('What do you want to say: ')
# #prompt = prompt.strip()
#
#     if prompt in dict_Nah_2_Eng_Eng2Nah:
#         print(dict_Nah_2_Eng_Eng2Nah[prompt])
#     else: print("The translation is not available")
#
#     checkRqst = input('Translate Another ? \n Enter 1(Yes) or 2(No): ')
#     if checkRqst == '2':
#         transRqst = False

#Need to add more to dictionary
#Need to work on sentence
#Need to make sure punctuation is included
#Need to make sure that Case is matched
#Need a function to convert a sentence into a list and then translate that