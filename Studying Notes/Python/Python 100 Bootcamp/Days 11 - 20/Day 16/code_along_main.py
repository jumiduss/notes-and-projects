# import code_along_another_module
# print(code_along_another_module.code_along_another_variable)

# from turtle import Turtle, Screen

# timmy  = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("CornflowerBlue")

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# timmy.forward(100)

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Pokemon Type",["Electric","Water","Fire"])
table.align = 'l'
print(table)
