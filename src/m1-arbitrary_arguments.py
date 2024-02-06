###############################################################################
# Done: 1. (3 pts)
#
#   Arbitrary arguments may not be something that you end up using all that
#   often and we may not use them often in this class, but I wanted to make
#   sure you had seen them. We will do a couple of examples and move on.
#
#   Under this _TODO_ write a function called roll_call() that takes an
#   arbitrary number of arguments (in our case it will be an arbitrary number
#   of names). It should then print the list of names. The example in the
#   reading showed how to print one item from the list, but you can print the
#   whole list instead.
#       (HINT: leave off the part that uses the square brackets [])
#
#   Once you have defined the function, write a line of code to call that
#   function and give it a list of students as its parameters.
#
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def roll_call(*names):

    print (f"The names of the students are: {names}")
    print ("The name of the first student is: " + names[0])
    print (f"The name of the second student is: {names[1]}")

roll_call("Fred", "Lucia", "Agnus")

###############################################################################
# Done: 2. (3 pts)
#
#   This time, let's create a function that uses arbitrary keyword arguments.
#
#   Under this _TODO_ write a function called pet_bio() that takes an arbitrary
#   number of keyword arguments (in this case it takes an arbitrary amount of
#   information about a pet). You could use things like name, age, date of
#   birth, species, etc. The function should then use the keywords to print out
#   some information about the pet. It can use some or all of the keywords that
#   you input, but it should use at least a couple.
#
#   Once you have defined the function, write a line of code that calls it
#   using the keyword arguments.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def pet_bio(**petinformation):

    print(f"The name of the pet is {petinformation["name"]}. Moonlight's birthday is {petinformation["birthday"]}. The color of Moonlight's fur is {petinformation["color"]}.")

pet_bio(name = "Moonlight", birthday = "July 4", color = "black")