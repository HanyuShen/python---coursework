from difflib import SequenceMatcher
import os,sys,time,datetime

print("Welcome to spellchecker!")

#load dictionary
def load_dict():
    with open('EnglishWords.txt','r') as f:
        for line in f:
            wd = line.strip('\n') 
            word_set.append(wd)
         
#after finding the wrong words
def display_semi_menu():
    Menu2 = ["ignore","mark","add to dictionary","suggest likely spelling"]

    for idx,val in enumerate(Menu2,start=1):
        print(" " + str(idx) + " . "+val) 


def make_suggestions(word):
    ratios = []
    for each in word_set:
        ratios.append(SequenceMatcher(None, word, each).ratio())
    sugg = word_set[ratios.index(max(ratios))]
    return sugg


def spellcheck(a):
    st_tm = time.time()

    no_of_word_added = 0
    no_of_incorrect = 0
    no_of_correct = 0
    incorrect = []

    for i in a:
        if i not in word_set:
            #print wrong words
            print(f'{i}')
            display_semi_menu()
            x = int(input('please enter your choice:'))

            if x == 1:
                no_of_incorrect += 1
                incorrect.append(i)
                ignore()
                print("It is ignored!")

            elif x == 2:
                no_of_incorrect += 1
                i = mark(i)
                incorrect.append(i)
                print("It is marked!")

                
            elif x == 3:
                add_to_dictionary(i)
                no_of_word_added += 1
                no_of_correct += 1
                print("It is added to the dictionary!")

            elif x == 4:
                correct = make_suggestions(i)
                print(f'Suggestion:  {correct}')
                accept_or_decline_menu()
                x = int(input("accept or decline?"))

                if x == 1:
                    i.replace(sugg)
                    no_of_correct += 1

                elif x == 2:
                    no_of_incorrect += 1
                    incorrect.append(i)



        else:
            no_of_correct += 1

    ed_tm = time.time()
    #collect statistics
    print(f'spellcheck has done!! {len(incorrect)} mistakes encountered,{ed_tm - st_tm:.2f} seconds used')
    semi_spellcheck()
    option = int(input('enter your choice:'))
    after_spell_check(option)

#suggestion
def accept_or_decline_menu():
    print(f'(1) accept')
    print(f'(2) decline')

#after spell check
def after_spell_check(option):
    try:
        if option == 1:
            menu()

        elif option == 2:
            print('Goodbye!')
            sys.exit(0)

    except ValueError:
        print('please enter again:')
        option = int(input('enter your choice:'))
        after_spell_check(option)

def display_main_choice():
    Menu = ["quit the spellchecker","check a sentence","check a file"]

    for idx,val in enumerate(Menu,start=0):
        print(" " + str(idx) + " . " + val)


def convert_sentence_to_lst(sentence):
    intermediate = sentence.lower().split(' ')
    return intermediate


#load files
def load_file(p):
    wd_lst = []
    with open(p,'r') as f:
        for line in f:
            wd_lst.append(line.strip('\n'))
    return wd_lst



def ignore():
    pass

def mark(word):
    word = f'?{word}?'
    return word

def add_to_dictionary(word):
    word_set.append(word)


#if the file doesn't exist
def semi():
    print(f'(1) enter the name again:')
    print(f'(2) return to main menu')


def semi_spellcheck():
    print(f'(1) return to main menu')
    print(f'(2) quit')


def SPELLCHECK():

    load_dict()
    menu()

#user menu 
def menu():

    while True:
        display_main_choice()
        choice = int(input('enter your choice:'))

        if choice == 1:
            #sentence_check
            sentence = str(input('please enter your sentence:'))
            #print out words separately
            words = []
            index = 0
            start = 0
            while index < len(sentence):
                start = index
                while sentence[index] != " " and sentence[index] not in[",","."]:
                    index += 1
                    if index == len(sentence):   
                        break
                words.append(sentence[start:index])
                if index == len(sentence):
                    break
                while sentence[index] == " " or sentence[index] in [",","."]:
                    index += 1
                    if index == len(sentence):
                        break
            print(words)
            
            s1 = convert_sentence_to_lst(sentence)
            spellcheck(s1)

            

        elif choice == 2:
            #file_check
            while True:
                p = str(input('please enter the name of the file:'))
                try:
                    spellcheck(load_file(p))

                except FileNotFoundError:
                    print('file not found')
                    semi()
                    x = int(input('enter your choice:'))

                    if x == 1:
                        pass

                    elif x == 2:
                        break


        elif choice == 0:
            e = input("Are you sure?")
            while e in ("yes","YES","y","Y"):
                print(f'Goodbye!')
                sys.exit(0)
            else:
                #return to the choice
                semi_spellcheck()
            

        else:
            print(f'invalid number,please enter again:')

if __name__ == '__main__':
    word_set = []
    SPELLCHECK()
 
 
   
