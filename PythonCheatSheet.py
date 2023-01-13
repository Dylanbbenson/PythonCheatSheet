"""
#lists
dumbasses = ["Joey", "Mike", "Lawrence", "Karen", "Miles"]

print("List of dumbasses I know: ")
print(dumbasses[0] + "\n" + dumbasses[1] + "\n" + dumbasses[2] + "\n")
"""

"""
#list functions
coworkers = ["Janette", "Doug", "Jon S", "Andrew", "Seth", "JP", "Jon K"]
bosses = ["Jennifer", "Levi", "Sherry"]
emp_ids = [2352, 6234, 8135, 4278, 1164, 1272, 2004]
coworkers_and_bosses = coworkers.extend(bosses) #appends list with another list
print(coworkers_and_bosses)

bosses.append("Scott") #appends list
print(bosses)
print(coworkers[2])
coworkers.clear() #clears list
coworkers_and_bosses.pop() #removes last element
print(bosses.index("Jennifer")) #checks if value in list
bosses.count("Levi") #gets count of value in list\
coworkers.sort() #sorts list alphabetically or numerically
coworkers.reverse() #reverse sorts list
allcoworkers = coworkers.copy() #creates copy of list
print(max(emp_ids)) #prints maximum in list
print(mix(emp_ids)) #prints minimum in list
print(sum(emp_ids)) #prints sum in list
print(sum(emp_ids)/len(emp_ids)) #prints average
x = list()
type(x) #returns variable type
dir(x)  #returns methods available for variable
sentence = "The quick brown fox jumped over the lazy dog"
words = sentence.split(" ") #splits sentence into works seperated by space
print(words)
"""

"""
#Tuples: data doesn't change and can't change
height = (5,7)
print(height[1])
heights = [(5,7), (6,2), (5,3), (6, 0), (5,11)] #list of tuples
print(heights[1])
"""

"""
#Functions
def say_hi(name):
    print("Hello, " + name)

name_input = input("What is your name?\n")
say_hi("Deshaun")
say_hi(name_input)
"""

"""
#Return statement in a function
def cube_number(num):
    return num*num*num

num_input = input("Enter a number to cube: ")
print(cube_number(int(num_input)))
"""

"""
#If Statements
name = input("Hi. I am a sentient program. What is your name? ")
how_do = input("Hello " + name +". How are you doing today? Well or poor? ")
if how_do == "well":
    print("Good to hear! I hope the rest of your day turns out just as good!")
elif how_do == "poor":
    print("Oh, I'm sorry to hear it. Here is a cupcake to cheer you up. Goodbye now!")
    print("This is a digital cupcake. Don't try to eat it, it's just 1's and 0's on a screen.")
else:
    print("I'm sorry. I don't understand what you mean. I'm gonna run away from you now.")
"""

"""
#Try Except
user_input = input("Enter a number: ")

try:
    num = int(user_input)
    if num > 0:
        print("That's a positive number")
    elif num < 0:
        print("That's a negative number")
    elif num == 0:
        print("...really? Zero?")
except:
    valid_answer = False
    print("...that's... not a number. Silly.")
"""

"""
#Loops
n = 5
while n > 0:
    print(n)
    n = n - 1
print("end")
"""

"""
#Loop Break
while True:
    line = input('> ')
    if line == 'end':
        break
    print(line)
print("end")
"""

"""
#Loop Continue
while True:
    line = input("> ")
    if line[0] == '#':
        continue
    if line == 'end':
        break
    print(line)
print("end")
"""

"""
#Definite For Loop
from time import sleep
for i in [5,4,3,2,1]:
    print(i)
    sleep(1)
print("Blastoff")
"""

"""
#Loop Idiom
largest_so_far = -1
print('Before: ', largest_so_far)
for the_num in (9, 41, 12, 3, 74, 15):
    if the_num > largest_so_far:
        largest_so_far = the_num
    print("New Number: " + str(the_num) + " Largest so far: " + str(largest_so_far))
print('After: ', largest_so_far)
"""

"""
#Multiple condition loop
smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)
"""

"""
#Summing in a loop
running_total = 0
numbers = [234, 345, 84, 197, 113, 12, 44]
for counter in numbers:
    running_total = running_total + counter
    print("New number: ", counter, "  Running total: ", running_total)
print("Final Total: ", running_total)
"""

"""
#Looping through string
fruit = 'banana'
for letter in fruit:
    print(letter)
"""
"""
#String operations
fruit = 'banana'
if 'nan' in fruit:
    instring = True
else:
    instring = False
print(instring)

word = "bananana"
uppercase_word = word.upper() #uppercase
i = uppercase_word.find("NA") #finds substring in string
print(i)

greeting = "    Hello World!     "
better_greeting = greeting.strip()
print(better_greeting)

email_addr = "BillyBobJoeJamesonWilliams@email.com"
atpos = email_addr.index('@')
print(atpos)
begin = email_addr[0]
name = email_addr[begin : atpos]
"""

"""
#Reading files
#syntax: open(filename, mode)
count = 0
fhand = open('text.txt', 'r')
print(fhand)                 #prints metadata
for lines in fhand:          #loops through file and prints
    print(lines)
    count = count + 1
print("Line Count: ", count) #print file line count
stuff = 'X\nY'               #\n means new line
print(stuff)


#More reading files
fhand = open('mailbox.txt')
inp = fhand.read() #puts entire file into a string
print(len(inp))    #prints character count
"""

"""
#Searching through a file
fhand = open('mailbox.txt')
for line in fhand:
    line = line.rstrip()           #strips white space
    if line.startswith('Because'): #filters for only lines starting with parameter
        print(line)
"""

"""
#Selecting lines using in
fhand = open('mailbox.txt')
for line in fhand:
    line = line.rstrip()
    if not '?' in line: #filters for only lines with ?
        continue
    print(line)
"""

"""
#prompt for file name
filename = input('Enter the file name: ')
fhand = open(filename)
count = 0
for line in fhand:
    newline = line.strip('\n') #remove line space
    count = count + 1
    print(newline)
    print("Character count: ", len(newline))
    print("\n")
print("Total Line Count: ", count)
"""

"""
#Dealing with bad file name inputs
filename = input('Enter the file name: ')
try:
    fhand = open(filename)
except:
    print("File couldn't be found.\nQuitting program...")
    quit() #quits program
count = 0
for line in fhand:
    count = count + 1
    print(line)
    print("Character count: ", len(line))
    print("\n")
print("Total Line Count: ", count)
"""

"""
#Lists Methods
x = list()
type(x) #returns variable type
dir(x)  #returns methods available for variable
"""

"""
#Dictionaries
purse = dict()          #declare a dictionary type variable
purse['money'] = 12     #assign a key to a value
purse['candy'] = 3
purse['tissues'] = 7
print(purse)
print(purse['candy'])   #prints 3
purse['tissues'] = 5
print(purse['tissues']) #prints 5

student = dict()
student['age'] = 19
student['department'] = "Psychology"
student['gender'] = 'F'
student['name'] = 'Serena'
#faster alternative: student = {'age':19, 'department':'Psychology', 'gender':'F', 'name':'Serena'}
print(student)
"""

"""
#adding to a dictionary
counts = dict()
names = ['Ramos', 'Reese', 'Lindsey', 'Quan']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
   #or  counts[name] = counts.get(name, 0) + 1
print(counts)
print(counts.get('don', 2)) #checks for name in dictionary, provides default key
"""

"""
counts = {'chuck':1, 'Jackson':42, 'Barry':233}
for key in counts:
    print(key)              #prints keys
    print(counts[key])      #prints values
    print(key, counts[key]) #prints both keys and values
print(counts.values())      #prints values
print(counts.keys())        #prints keys
print(counts.items())       #prints items
"""

#Reading a file into a dictionary
filename = input('Enter file name: ')
fhandle = open(filename)

counts = dict()
for line in fhandle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)