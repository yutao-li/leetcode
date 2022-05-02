class Menu:
    def getItems(self) -> ['MenuItem']:
        pass


class MenuItem:
    def getSubMenu(self) -> Menu:
        pass

    def hasSubMenu(self) -> bool:
        pass

    def hasIcon(self) -> bool:
        pass

    def getIconId(self) -> str:
        pass


def checkAllMenusForIcons(menubarMenus: [Menu]):
    def checkMenuItemsForIcons(menuItems: [MenuItem], hasIcon=True):
        if not all(m.hasIcon() == hasIcon for m in menuItems):
            return False
        if hasIcon:
            icons = [m.getIconId() for m in menuItems]
            if len(set(icons)) != len(icons):
                return False
        for menuItem in menuItems:
            if menuItem.hasSubMenu():
                if not checkMenuItemsForIcons(menuItem.getSubMenu().getItems(), hasIcon):
                    return False
        return True

    def checkIconConsistency(hasIcon):
        for menu in menubarMenus:
            if not checkMenuItemsForIcons(menu.getItems(), hasIcon):
                return False
        return True

    return checkIconConsistency(True) or checkIconConsistency(False)


def checkAllMenusForIcons1(menubarMenus: [Menu]):
    def checkMenuItemsForIcons(menuItems: [MenuItem]):
        if not (all(m.hasIcon() for m in menuItems) or all(m.hasIcon() for m in menuItems)):
            return False
        if menuItems[0].hasIcon():
            icons = [m.getIconId() for m in menuItems]
            if len(set(icons)) != len(icons):
                return False
        for menuItem in menuItems:
            if menuItem.hasSubMenu():
                if not checkMenuItemsForIcons(menuItem.getSubMenu().getItems()):
                    return False
        return True

    for menu in menubarMenus:
        if not checkMenuItemsForIcons(menu.getItems()):
            return False
    return True
