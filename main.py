# Parent drug class
class Drug:
    def __init__(self, cost, hours):
        self.cost = cost
        self.hours = hours


class Prices:
    def __init__(self, weed, addy, acid):
        self.weed_price = weed
        self.addy_rate = addy
        self.acid_price = acid


class Percocet(Drug):
    def __init__(self, mgs):
        self.mgs = mgs

    # derived from Drug class


class Weed(Drug):
    def __init__(self, grams):
        self.grams = grams
        hours = 4
        cost = self.grams * 8
        Drug.__init__(self, cost, hours)


# derived from Drug class
class Adderall(Drug):
    def __init__(self, mgs, type):
        self.mgs = mgs
        self.rate = 10 / 30
        cost = self.rate * mgs
        hours = self.calc_hours(type)
        Drug.__init__(self, cost, hours)

    def calc_hours(self, type):
        if type == "xr":
            return 10
        elif type == "ir":
            return 4
        else:
            return 0


# derived from Drug class
class Acid(Drug):
    def __init__(self, ug, cost):
        self.ug = ug
        hours = 12
        Drug.__init__(self, cost, hours)

    def get_tabs(self):
        return self.ug / 100


class User:
    def __init__(self):
        self.hours = self.set_hours()
        self.usage = []
        self.total_cost = 0
        self.set_cost()

    def get_addy_total(self):
        total = 0
        for i in self.usage:
            total += i.cost

    def take_addy(self, mgs, type):
        self.usage.append(Adderall(mgs, type))
        self.set_cost()

    # Checks times a certain drug has been taken
    def times(self, drug_name):
        count = 0
        for i in self.usage:
            if drug_name == type(i):
                count += 1
        return count

    def change_time(self, hours):
        self.hours += hours

    def get_hours(self):
        return self.hours

    def set_hours(self):
        hours = 0
        for i in self.usage:
            hours += i.hours
        return hours

        # Checks total times

    def total_times(self):
        return len(self.usage)

    def smoke_weed(self, grams):
        self.usage.append(Weed(grams))
        self.set_cost()

    def addy_cost(self):
        cost = 0
        for i in self.usage:
            if isinstance(i, Adderall):
                cost += i.cost
        return cost

    def weed_cost(self):
        cost = 0
        for i in self.usage:
            if isinstance(i, Weed):
                cost += i.cost
        return cost

    def set_cost(self):
        cost = 0
        for i in self.usage:
            cost += i.cost
        self.total_cost = cost



local_prices = Prices(8, 10 / 30, 5)

me = User()
me.take_addy(30, "xr")
me.smoke_weed(10)
