"""Chapter 11 Assessment Program - Creatures

Assignment Requirements:
Download the file creature_class.py Download creature_class.pycontaining a description of the class Creature.

You are working on designing some classes that will be used in a simple video game. Your partner has already designed
the basic class for creatures in the game:

Creature_UML.png

Using the class Creature for the parent class, create a subclass of Creature called Orc. Orc should have attributes
for weapon (string), max_hit_points (integer), and current_hit_points (integer). Create appropriate setter and getter
methods and an appropriate __str__() method. (Remember, __str__() should return a string value.) For all Orcs, the
friendly attribute should be set to False and the type_of_creature should be "Orc".

Then, using the class Orc for the parent class, create a subclass of Orc called OrcBoss. OrcBoss should include
attributes for name (string) and a special_move (string). Create appropriate setter and getter methods and an
appropriate __str__() method.

You will then create a simple program that creates an instance of each of the three classes and uses the __str__()
method to display them.

Tip-full-size-gold-1.png Hint: When you override the __str__() method in the child class, you can fetch the string
generated by the parent class with <parent-class-name>.__str__(), e.g. Creature.__str__()"""
import creature_class


def main():  # Define main
    # Create instance object for each class setting the attributes
    creature = creature_class.Creature("Rabbit", True, "(10, 250, 10)", "bunny.gif")
    orc = creature_class.Orc("Orc", False, "(-100, 200, 50)", "orc.gif", "axe", 150, 150)
    orc_boss = creature_class.OrcBoss("Orc", False, "(300, 150, 35)", "orc_boss.gif", "greatsword", 350, 200,
                                      "Griksnak", "jump and slash")

    # Display the state of the instances
    print(creature)
    print(orc)
    print(orc_boss)


main()  # Call main
