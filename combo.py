import random

def nim_sum(piles):
    result = 0
    for pile in piles:
        result ^= pile
    return result

def optimal_move(piles):
    nimSumVal = nim_sum(piles)
    if nimSumVal == 0:
        nonEmptyPiles = [i for i in range(len(piles)) if piles[i] > 0]
        pileInd = random.choice(nonEmptyPiles) # pile index
        toBeRemoved = random.randint(1, piles[pileInd])
    else:
        for i in range(len(piles)):
            move = piles[i] ^ nimSumVal
            if move <= piles[i]:
                toBeRemoved = piles[i] - move
                pileInd = i
                break
    piles[pileInd] -= toBeRemoved
    print(f"Computer removes {toBeRemoved} from pile {pileInd + 1}")
#allows user to take their turn and alters the pile accordingly
def user_move(piles):
        try:
            pileInd = int(input("Enter pile #: ")) - 1
            toBeRemoved= int(input("Enter # of items to remove: "))
            piles[pileInd] -= toBeRemoved
        except ValueError:
            print("Invalid input. Please enter a valid #.")

def play_nim():
    piles = [3, 4, 7]  # initial piles - change this to whatever you want

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

