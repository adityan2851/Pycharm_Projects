# import another_module

# print(another_module.another_variable)
#
# from turtle import Turtle,Screen
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon", ["Pikachu", "Snorax", "weedle"])
table.add_column("Type", ["Electric", "Ground", "Poison"])
table.align = "r"


print(table)