from foodplaner.logic.ingredient_class.type import Type
from foodplaner.logic.ingredient_class.unit_type import Unit_Type
from foodplaner.logic.ingredient_class.season import Season


class Ingredient:
    type: Type
    amount: float
    unit_type: Unit_Type
    costs: float
    season: Season

    # Nutritions
    calories: int
    fat: float
    sugar: float

    # Properties
    gluten_free: bool
    vegetarian: bool
    vegan: bool

    accessability: int

    def __init__(
        self,
        type: Type = None,
        amount: float = 0,
        unit_type: Unit_Type = None,
        costs: float = 0,
        season: Season = None,
        calories: int = 0,
        fat: float = 0,
        sugar: float = 0,
        gluten_free: bool = True,
        vegetarian: bool = True,
        vegan: bool = True,
        accessability: int = None,
    ):

        self.type = type
        self.amount = amount
        self.unit_type = unit_type
        self.costs = costs
        self.season = season
        self.calories = calories
        self.fat = fat
        self.sugar = sugar
        self.gluten_free = gluten_free
        self.vegetarian = vegetarian
        self.vegan = vegan
        self.accessability = accessability
