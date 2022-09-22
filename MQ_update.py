#not sure if anything is better, but I tried to understand your comments
#and change my code the best I could.

def greet_player():
    print("Hello! Welcome to Ben's Math Quiz!")


def get_name():
    print("What is your name user?")
    name = input(str('Name: ').strip())
    print('Hello, ' + name + '!')


def ready_to_begin():
    ready = str(input('Are you ready to begin ' + name + '? Please type y or n: ')) #isn't this a local variable? Is this okay or does it need to be changed?
    while ready != 'y' or 'n':
        if ready.startswith('y'.lower()):
            print("Okay, let's begin.")
            break
        elif ready.startswith('n'.lower()):
            print('Okay, see ya!')
            exit()
        else:
            print('Invalid Answer. Please restart and remember your input must begin with a y or a n.') #couldn't figure out how to loop this to the beginning question, so I used exit(). Any advice?                                                                                             #Used exit() and made the user restart. Any advice?
            exit()                                                                                      
    return
   
   
def question0():
    print('What is 1 + 1?')
    answer = input('Answer: ')
    while answer != 2:
        if int(answer) < 2:
             print('Sorry ' + name + '. That number us too low.')
        elif int(answer) > 2:
            print('Sorry, ' + name + '. That number is too high' )
        else:
            print("That's correct!")
            break
    return

    
    
if __name__ == '__main__':
    name = ''
    greet_player()
    get_name()
    ready_to_begin()
    question0()
