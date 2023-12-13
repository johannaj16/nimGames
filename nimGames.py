import random

# Calculates the Nim sum by performing an exclusive bitwise XOR operation 
# on all the elements (piles) in the input list and returns the resulting value
def nim_sum(piles):
    result = 0
    for pile in piles:
        result ^= pile
    return result

# Determines the optimal move for the computer based on the nim sum and winning strategy algorithm
def optimal_move(piles):
    # Calculates the best move for a Nim game by first computing the Nim sum using def(nim sum). 
    nimSumVal = nim_sum(piles)
    # If the Nim sum is zero, indicating there is no winning strategy here, it randomly selects a non-empty pile to removes a random number of objects. 
    if nimSumVal == 0:
        nonEmptyPiles = [i for i in range(len(piles)) if piles[i] > 0]
        pileInd = random.choice(nonEmptyPiles) # pile index
        toBeRemoved = random.randint(1, piles[pileInd])
    # Otherwise, it iterates through the piles to find the pile and number of objects to remove, 
    # based on a bitwise XOR operation between the piles and the Nim sum, guaranteeing the resulting move leads to a winning position for the computer.
    else:
        for i in range(len(piles)):
            move = piles[i] ^ nimSumVal
            if move <= piles[i]:
                toBeRemoved = piles[i] - move
                pileInd = i
                break
    # removes the right amount from the correct pile in order to complete the winning strategy
    piles[pileInd] -= toBeRemoved
    print(f"Computer removes {toBeRemoved} from pile {pileInd + 1}")
    
# Handles the user's move by taking input for pile number and the number of items to remove
def user_move(piles):
        try:
            pileInd = int(input("Enter pile #: ")) - 1
            toBeRemoved= int(input("Enter # of items to remove: "))
            piles[pileInd] -= toBeRemoved
        except ValueError:
            print("Invalid input. Please enter a valid #.")

# Coordinates the Nim game between the user and the computer
def play_nim():
    piles = [3, 4, 7]  # initial piles - change this to whatever you want

    #prints the updated pile numbers after every move
    while any(piles):
        print("\nPiles:", piles)
        user_move(piles)
        if not any(piles):
            print("You win!")
            break
        print("\nPiles:", piles)
        optimal_move(piles)
    
    print("COMPUTER WINS!!!")

if __name__ == "__main__":
    print("Let's play Nim!")
    play_nim()

