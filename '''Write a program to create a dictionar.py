'''Write a program to create a dictionary of hindi words with values as their english transclation .
   provide user with an option to look it up . '''

words = {
    "Paani" : "Water",
    "Aam" : "Mango",
    "Ghar" : "House",
    "Kitab" : "Book",
    "Ladka" : "Boy",
    "Ladki" : "Girl",
         }

word = input("Enter a word : ")
print(words.get(word))