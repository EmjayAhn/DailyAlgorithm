# https://www.hackerrank.com/challenges/30-scope/problem

class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0
	# Add your code here
    def computeDifference(self):
        for index, element in enumerate(self.__elements):
            for comparison in self.__elements[index+1:]:
                difference = abs(element - comparison)
                if self.maximumDifference < difference:
                    self.maximumDifference = difference
        
# End of Difference class
_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)