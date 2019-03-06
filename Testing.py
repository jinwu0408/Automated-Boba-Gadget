from menu import MenuItem, MenuContext, MenuDelegate, Menu
from drinks import drink_options, drink_list


m = Menu("Main Menu")
drink_opts = []
for d in drink_list:
    drink_opts.append(MenuItem('drink', d["name"], {"ingredients": d["ingredients"]}))
print(drink_opts)

m.addOptions(drink_opts)
print(m.getSelection())
m.nextSelection()
print(m.getSelection())


"""
menu.addOption(beef)
menu.addOption(pork)

delegate = MenuDelegate()
context = MenuContext(menu, delegate)

context.advance()
#context.showMenu()
"""
