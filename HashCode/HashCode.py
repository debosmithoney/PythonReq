
class Street:
    def _init_(self, i1, i2, name, length):
        self.intersection = list(map(int, [i1, i2]))
        self.name = name
        self.length = int(length)

class Car:
    def _init_(self, n, s):
        self.numberOfStreets = n
        self.streetsToPass = s

streets = []
cars = []


inputFile = open('a.txt', 'rt')
outputFile = open('a_out.txt', 'wt')

[d, i, s, v, f] = list(map(int, inputFile.readline().split()))

for _ in range(s):
    [i1, i2, name, length] = inputFile.readline().split()
    streets.append(Street(i1, i2, name, length))
    # print(streets[_].intersection)
    # print(streets[_].name)
    # print(streets[_].length)

for _ in range(v):
    n = inputFile.readline().split()
    s, n = n[1:], int(n[0])
    cars.append(Car(n, s))
    # print(cars[_].numberOfStreets)
    # print(cars[_].streetsToPass)

inputFile.close()
outputFile.close()