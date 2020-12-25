import numpy as np

def distributeCandies(numCandies, numPeople):
    # first we have to find where we'll stop counting
    # the sum of natural numbers up to n is n(n+1)/2 so if we want the sum to equal at most the numCandies,
    # we should need to stop at the floor of the solution when solving for n
    # using the max value given by the quadratic formula

    lastFullGive = int(np.floor(np.max(np.roots([1, 1, -2 * numCandies]))))
    indexOfRemainingGive = lastFullGive % numPeople
    
    person = 0
    people = [0] * numPeople
    
    for give in range(1, lastFullGive + 1):
        people[person] += give
        numCandies -= give
        person += 1
        if person == numPeople:
            person = 0
    people[indexOfRemainingGive] += numCandies
    return people

if __name__ == "__main__":
    numCandies = 100
    numPeople = 14

    print(f"(TEST)\n\tnumber of Candies: {numCandies}\n\tnumber of Peope: {numPeople}")
    result = distributeCandies(numCandies, numPeople)
    print(f"\tresult of function: {result}")