
import numpy as np

def gambler_ruin_2():
    import numpy as np
    
    # input
    a = int(input("Enter the starting $ (a): "))
    b = int(input("Enter the desired winning $, where to stop (b >= a): "))
    p = float(input("Enter the probability of winning each match, p (0 <= p <= 1): "))
    n = int(input("Enter the number of matches to play (n): "))

    # range check    
    if b < a or p < 0 or p > 1 or n < 0:
        print("check your input parameters.")
        return


    # Initialize probability distribution: all money amounts from 0 to b
    # Probability of being at starting amount a is 1 initially
    prob_dist = np.zeros(b + 1)
    prob_dist[a] = 1.0

    # absorbing states
    if a == 0 or a == b:
        prob_dist = np.zeros(b + 1)
        prob_dist[a] = 1.0
    else:
        for _ in range(n): # for each game
            new_prob_dist = np.zeros(b + 1)
            for i in range(1, b):  # only update between [1,b) 
                                # win & reaching 'goal'    # lose & reaching 'goal'
                new_prob_dist[i] = p * prob_dist[i -1] + (1 - p) * prob_dist[i + 1]
                                            # += lose from a+1 $
            new_prob_dist[0] = prob_dist[0] + (1 - p) * prob_dist[1]
                                            # += win from b-1 $
            new_prob_dist[b] = prob_dist[b] + p * prob_dist[b - 1]

            prob_dist = new_prob_dist

    # print the prob dist 
    print("\nProbability Distribution Vector at time n:")
    for i, probability in enumerate(prob_dist):
        print(f"${i}: {probability:.5f}")

def absorption_times():
    # To be implemented
    pass

def random_walk_distance():
    # To be implemented
    pass

def random_walk_intersection():
    # To be implemented
    pass

def main_menu():
    while True:
        print("\nSelect a simulation to run:")
        print("1: Gambler's Ruin 2")
        print("2: Absorption Times")
        print("3: Random Walk (Distance)")
        print("4: Random Walk (Intersection)")
        print("0: Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            gambler_ruin_2()
        elif choice == "2":
            absorption_times()
        elif choice == "3":
            random_walk_distance()
        elif choice == "4":
            random_walk_intersection()
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please choose again.")

if __name__ == "__main__":
    main_menu()
