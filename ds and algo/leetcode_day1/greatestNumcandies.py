'''
Given the array candies and the integer extraCandies, 
where candies[i] represents the number of candies that the ith kid 
has.

For each kid check if there is a way to distribute extraCandies
 among the kids such that he or she can have the greatest number of 
 candies among them. Notice that multiple kids can have the greatest
 mber of candies.

 '''

def kidsWithCandies(self, candies, extraCandies):
        highest_candies = max(candies)
        new_list = []
        for i in candies:
            if i+extraCandies >= highest_candies:
                new_list.append(True)
            else:
                new_list.append(False)
        return new_list