print(
    """
    Please pick your option:
    1) Percolation model for Small Pox
    2) 
    3) Instructions
    4) Exit
    """
)

option = input("Which option[1,2,3,4]? ")

if option == '1':

    import random

    perc = input("Please enter a thresold between 0-1.   ")
    perc = float(perc)

    ###
    PERSON, EMPTY = '*', '.'


    ###

    ###

    def percolation(perc):
        randval = random.random()
        if randval > perc:
            return EMPTY
        else:
            return PERSON


    def make_random_world(M, N):
        """Constructs a new random game world of size MxN."""
        world = {}
        for j in range(N):
            for i in range(M):
                world[i, j] = percolation(perc)
        world['dimensions'] = (M, N)
        return world


    def print_world(world):
        """Prints out a string representation of a world."""
        M, N = world['dimensions']
        for j in range(N):
            for i in range(M):
                print(world[i, j])
        #print("")


    n = int(input("Please enter a n dimension.   "))
    m = int(input("Please enter a m dimension.   "))

    input("Press return to make a world")
    print_world(make_random_world(n, m))
