# Application using classes and objects
import time
import webbrowser

''' **INSTRUCTIONS**
1. Make a script that does the following requirements:
2. Create a class of something abstract of your election (say for example, vehicle, fruit, person etc.)
3. The class must have at least 5 properties.
4. Each class must have at least 2 methods (functions) that resemble the classes in real file (for example, a car goes forward, backwards, parks, etc.).
5. Create 2 objects of that class with their respective properties.
6. Change 2 properties of one of the objects created.
7. Execute all the methods you created for the class, with both objects.
8. Delete the objects at the end.
'''
class fruits():
    # DEFINITIONS
    def __init__(fruit, name, color, texture, taste, where, type):
        fruit.name =  name
        fruit.color = color
        fruit.texture = texture
        fruit.taste = taste
        fruit.where = where
        fruit.type = type
    
    # ACTIONS
    def eat(fruit):
        fruit.eat = print(f"I just ate {fruit.name}")
    def smell(fruit):
        fruit.smell = print(f"It smells like {fruit.name}")
    def drink(fruit):
        fruit.drink = print(f"You mash the {fruit.name} into a juice and drink.")
def fruitStats(fruit, name, color, texture, taste, where, type):
    print("Fruit")
    print(f"Name: {name}")
    print(f"Color: {color}")
    print(f"Texture: {texture}")
    print(f"Taste: {taste}")
    print(f"Where: {where}")
    print(f"Type: {type}")

# Fruit 1 - Pineapple
pineapple = fruits("pineapple","orange","tender","sweet and tart","from South America and the Caribbean","composite")
fruitStats(pineapple, pineapple.name, pineapple.color, pineapple.texture, pineapple.taste, pineapple.where, pineapple.type)
print("")
print("Actions")
pineapple.eat()
pineapple.smell()
pineapple.drink()
print("")
print("Attribute Changes")
pineapple.color = "yellow"
pineapple.taste = "old"
fruitStats(pineapple, pineapple.name, pineapple.color, pineapple.texture, pineapple.taste, pineapple.where, pineapple.type)
print("")

# Fruit 2 - Apple
red_apple = fruits("red apple", "red","hard","sweet","from Central Asia","fake fruit")
fruitStats(red_apple, red_apple.name, red_apple.color, red_apple.texture, red_apple.taste, red_apple.where, red_apple.type)
print("")
print("Actions")
red_apple.eat()
red_apple.smell()
red_apple.drink()
print("")
print("Attribute Changes")
red_apple.name = "rotten red apple"
red_apple.taste = "rotten"
fruitStats(red_apple, red_apple.name, red_apple.color, red_apple.texture, red_apple.taste, red_apple.where, red_apple.type)

del red_apple
del pineapple





















def nothingbad():
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=NfuiB52K7X8")
nothingbad()