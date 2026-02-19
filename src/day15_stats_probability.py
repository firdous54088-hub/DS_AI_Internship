# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 12:51:04 2026

@author: Raj Mohammad
"""

# Task 1

actions = ["Click", "Scroll", "Exit"]

# Define sample space S 
S = [(a1, a2) for a1 in actions for a2 in actions]

# Define event E"
E = [outcome for outcome in S if "Click" in outcome]

probability = len(E) / len(S)

# Print results
print("Sample Space S:")
print(S)

print("\nEvent E (at least one Click):")
print(E)

print("\nProbability of at least one Click:")
print(probability)

import random

rolls = 1000
count_sum_7 = 0

for _ in range(rolls):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    
    if die1 + die2 == 7:
        count_sum_7 += 1

experimental_probability = count_sum_7 / rolls

print("Number of times sum was 7:", count_sum_7)
print("Experimental probability:", experimental_probability)

# Task 2

# Independent Events 

p_heads = 1/2
p_six = 1/6

p_independent = p_heads * p_six

print("Independent Event:")
print("P(Heads and 6) =", p_independent)

# Dependent Events 

total_marbles = 10
red_marbles = 5


p_red1 = red_marbles / total_marbles
p_red2 = (red_marbles - 1) / (total_marbles - 1)
p_dependent = p_red1 * p_red2

print("\nDependent Event:")
print("P(Both Red) =", p_dependent)

# Task 3

P_spam = 0.1
P_ham = 0.9
P_free_given_spam = 0.9
P_free_given_ham = 0.05

# Total probability of "Free"
P_free = P_free_given_spam * P_spam + P_free_given_ham * P_ham

# Bayes' Theorem: P(Spam | Free)
P_spam_given_free = (P_free_given_spam * P_spam) / P_free

print("Probability the email is Spam given it contains 'Free':", P_spam_given_free)