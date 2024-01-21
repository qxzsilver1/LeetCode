from sortedcontainers import SortedSet

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisines_food_map = defaultdict(SortedSet) # map each cuisine to a SortedSet in descending order of ratings/foods pair
        self.cuisines = {}
        self.ratings = {}

        for i in range(len(foods)):
            self.cuisines_food_map[cuisines[i]].add((-ratings[i], foods[i])) # SortedSet only allows ascending order - so negate the ratings in order to sort in descending order
            self.cuisines[foods[i]] = cuisines[i]
            self.ratings[foods[i]] = ratings[i]

    def changeRating(self, food: str, newRating: int) -> None:
        c = self.cuisines[food]
        r = self.ratings[food]

        self.cuisines_food_map[c].remove((-r, food))
        self.cuisines_food_map[c].add((-newRating, food))

        self.ratings[food] = newRating

    def highestRated(self, cuisine: str) -> str:
        return self.cuisines_food_map[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
