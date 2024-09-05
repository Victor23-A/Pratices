from random import randint

def Password_generator(length):
    
    letters = "abcdefghijklmnopqrstuvwxyz"
    special_characters = "!#$%&/()[]"
    count = 0
    password = ""
    
    while count < length:
        
        choice = randint(1,3)
        
        if choice == 1:
            
            if randint(1,2) == 1:
                password = password + letters[randint(0,25)]
                
            else:
                letter = letters[randint(0,25)]
                password = password + letter.upper()
                
        elif choice == 2:
            
            password = password + special_characters[randint(0,9)]
            
        elif choice == 3:
            
            a = str(randint(0,9))
            password = password + a
            
        count = count + 1
        
    return password    
        
x = int(input("How many characters do you want your password to be: "))
password = Password_generator(x)     
print(f"Your password is {password}")         