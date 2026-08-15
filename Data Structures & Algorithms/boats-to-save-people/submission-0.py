class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0
        print(people)
        light, heavy = 0, len(people) - 1

        while light <= heavy:
            if people[light] + people[heavy] <= limit:
                res += 1
                light += 1
                heavy -= 1
            else:
                res += 1
                heavy -= 1
        
        return res