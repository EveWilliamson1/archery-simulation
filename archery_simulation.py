# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 12:47:09 2025

Collaborative academic project - portfolio code retained by Eve Williamson.
"""

import random
import math
import matplotlib.pyplot as plt


def playRound(p1x, p1y, p2x, p2y):
    """
    Simulates one round of the archery match.

    Each player shoots 3 arrows whose x and y coordinates are drawn from
    normal distributions with standard deviations p1x, p1y for Player 1,
    and p2x, p2y for Player 2. The arrow closest to the bullseye (0,0)
    wins the round.
    """
    # Generating three arrow positions for each player
    arrows_p1 = [(random.gauss(0, p1x), random.gauss(0, p1y)) for _ in range(3)]
    arrows_p2 = [(random.gauss(0, p2x), random.gauss(0, p2y)) for _ in range(3)]

    # Compute the Euclidean distance for each arrow and record which player fired it.
    all_arrows = []

    # Process each arrow thrown by Player 1
    for arrow in arrows_p1:
        distance = math.hypot(arrow[0], arrow[1])
        all_arrows.append((arrow[0], arrow[1], distance, 1))

    # Process each arrow thrown by Player 2
    for arrow in arrows_p2:
        distance = math.hypot(arrow[0], arrow[1])
        all_arrows.append((arrow[0], arrow[1], distance, 2))

    # Find the arrow that landed closest to the center (the smallest distance)
    min_distance = float('inf')
    winner_arrow = None

    for arrow in all_arrows:
        if arrow[2] < min_distance:
            min_distance = arrow[2]
            winner_arrow = arrow

    winner = winner_arrow[3]

    print(f"Player {winner} wins!")
    print("Winning arrow details:")
    print("Coordinates:", (winner_arrow[0], winner_arrow[1]))
    print("Distance from center:", winner_arrow[2])

    # Visualisation of the round
    plt.figure(figsize=(6, 6))
    plt.scatter([arrow[0] for arrow in arrows_p1], [arrow[1] for arrow in arrows_p1],
                color='steelblue', label='Player 1', marker='x')
    plt.scatter([arrow[0] for arrow in arrows_p2], [arrow[1] for arrow in arrows_p2],
                color='forestgreen', label='Player 2', marker='x')
    plt.scatter(0, 0, color='firebrick', label='Bullseye')
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.legend()
    plt.title('Archery Match - Arrow Positions')
    plt.grid(True)
    plt.show()

    return winner


def playMatch(p1x, p1y, p2x, p2y):
    """
    Simulates a full archery match.

    Rounds are played until one player scores at least 11 points and is
    ahead by at least 2 points. After each round, the score is updated.

    Parameters:
        p1x, p1y: Standard deviations for Player 1's shots.
        p2x, p2y: Standard deviations for Player 2's shots.
    """
    score1 = 0
    score2 = 0
    round_num = 1

    while not ((score1 >= 11 or score2 >= 11) and abs(score1 - score2) >= 2):
        print(f"Starting Round {round_num}")
        round_winner = playRound(p1x, p1y, p2x, p2y)

        if round_winner == 1:
            score1 += 1
        else:
            score2 += 1

        print(f"After Round {round_num}: Player 1 has {score1} points, Player 2 has {score2} points")
        round_num += 1

    if score1 > score2:
        print("Player 1 wins the match")
    else:
        print("Player 2 wins the match")

    print(f"Final Score: Player 1: {score1}, Player 2: {score2}")


def main():
    # Welcome message and default parameter values
    print("SIMPLE ARCHERY SIMULATOR")
    p1x, p1y, p2x, p2y = 1.5, 1.6, 1.7, 1.8

    # Ask the user if they want to specify their own parameter values
    s = input("Use default input parameters? (y/n) >> ")
    if s != "y" and s != "Y":
        p1x = float(input("Enter Player 1 x parameter >> "))
        p1y = float(input("Enter Player 1 y parameter >> "))
        p2x = float(input("Enter Player 2 x parameter >> "))
        p2y = float(input("Enter Player 2 y parameter >> "))
    else:
        print("Using default parameters")

    # Check that all the parameters have valid values
    assert min(p1x, p1y, p2x, p2y) >= 0, "All parameters must be positive"

    playRound(p1x, p1y, p2x, p2y)

    print("\n--- Now starting the full match ---\n")
    playMatch(p1x, p1y, p2x, p2y)


if __name__ == "__main__":
    main()
