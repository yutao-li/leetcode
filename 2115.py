from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        def checkCookable(iRecipe):
            if canCook[iRecipe] == 1:
                return True
            if canCook[iRecipe] == 0 or canCook[iRecipe] == 2:
                canCook[iRecipe] = 0
                return False
            canCook[iRecipe] = 2
            ingredient = i2ingre[iRecipe]
            for i in ingredient:
                if not (i in supplies or i in recipe2i and checkCookable(recipe2i[i])):
                    canCook[iRecipe] = 0
                    return False
            canCook[iRecipe] = 1
            return True

        n = len(recipes)
        supplies = set(supplies)
        recipe2i = dict(zip(recipes, range(n)))
        i2ingre = dict(zip(range(n), ingredients))
        canCook = [-1] * n
        return [r for i, r in enumerate(recipes) if checkCookable(i)]


print(Solution().findAllRecipes(["ju", "fzjnm", "x", "e", "zpmcz", "h", "q"],
                                [["d"], ["hveml", "f", "cpivl"], ["cpivl", "zpmcz", "h", "e", "fzjnm", "ju"],
                                 ["cpivl", "hveml", "zpmcz", "ju", "h"], ["h", "fzjnm", "e", "q", "x"],
                                 ["d", "hveml", "cpivl", "q", "zpmcz", "ju", "e", "x"], ["f", "hveml", "cpivl"]],
                                ["f", "hveml", "cpivl", "d"]))
