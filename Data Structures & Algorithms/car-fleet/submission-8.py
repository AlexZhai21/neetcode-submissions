class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        der_cars = []
        ans = 0
        for i in range(len(position)):
            der_cars.append([position[i], speed[i]])
        der_cars = sorted(der_cars, reverse = True)
        def t_to_t(p, s, t):
            time = (t-p)/s
            return time
        for d in der_cars:
            d.append(t_to_t(d[0], d[1], target))
        # print(der_cars)
        der_fleets = []
        for d in der_cars:
            if not der_fleets:
                der_fleets.append(d)
            else:
                if der_fleets[-1][-1] < d[-1]:
                    der_fleets.append(d)
        return len(der_fleets)




        