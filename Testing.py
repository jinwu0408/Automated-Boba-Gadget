from menu import MenuItem, MenuContext, MenuDelegate, Menu

beef = MenuItem("menu", "beef")
pork = MenuItem("menu", "pork")

menu = Menu("menu1")

menu.addOption(beef)
menu.addOption(pork)

delegate = MenuDelegate()
context = MenuContext(menu, delegate)

context.advance()
#context.showMenu()
