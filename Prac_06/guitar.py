

class Guitar:
    def __init__(self, name="",year=0,cost=0):
        """
        name: string, name/make of guitar
        year: int, year guitar was made
        cost: float, cost of guitar
        """
        self.name = name
        self.year = year
        self.cost = cost
    def __str__(self):
        return "{0} ({1}) : ${2}".format(self.name,self.year,self.cost)
    def get_age(self):
        age = 2018 - self.year
        return age
    def is_vintage(self):
        if self.get_age() > 49:
            return True
        else:
            return False