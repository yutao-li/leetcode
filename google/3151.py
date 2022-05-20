from collections import Counter, defaultdict


class Recipe:
    def __init__(self, name, servings, ingredients: {str: float}):
        self.name = name
        self.servings = servings
        self.ingredients = ingredients


class Cook:
    def __init__(self, recipes: [Recipe], supplies: {str: float}):
        def detectCycle():
            def dfs(recipe):
                i = recipe2int[recipe]
                seen[i] = 2
                for dep in self.adjList[recipe]:
                    if seen[recipe2int[dep]] == 2:
                        return False
                    elif seen[recipe2int[dep]] == 0:
                        if not dfs(dep):
                            return False
                seen[i] = 1
                return True

            n = len(recipeNames)
            recipe2int = dict(zip(recipeNames, range(n)))
            seen = [0] * n
            for recipe in recipeNames:
                if not dfs(recipe):
                    raise ValueError('recipes input includes dependency cycle.')

        self.recipes = recipes
        self.supplies = supplies
        self.rawIngredients = defaultdict(list)
        self.adjList = defaultdict(list)
        recipeNames = set(r.name for r in recipes)
        for recipe in recipes:
            for i in recipe.ingredients:
                if i in recipeNames:
                    self.adjList[recipe].append(i)
                else:
                    self.rawIngredients[recipe].append(i)
        detectCycle()

    def canMakeMeal(self, recipe):
        def canMakeRecipeWithSupply(recipe):
            nonlocal supplies
            supplies -= Counter(self.rawIngredients[recipe])
            if len(supplies) < len(self.supplies):
                return False
            for dep in self.adjList[recipe]:
                if not canMakeRecipeWithSupply(dep):
                    return False
            return True

        supplies = Counter(self.supplies)
        return canMakeRecipeWithSupply(recipe)


class IngredientOption:
    def __init__(self, ingredients):
        self.ingredients = ingredients


class Recipe1:
    def __init__(self, name, servings, ingredients: {str: float}):
        self.name = name
        self.servings = servings
        self.ingredients = ingredients


class Cook1:
    def __init__(self, recipes: [Recipe1], supplies: {str: float}):
        self.recipes = recipes
        self.supplies = supplies
        self.rawIngredients = defaultdict(list)
        for r in self.recipes:
            self.rawIngredients[r.name].append(r.ingredients)

    def canMakeMeal(self, recipe):
        supplies = Counter(self.supplies)
        for ingred in self.rawIngredients[recipe]:
            if supplies >= Counter(ingred):
                return True
        return False
