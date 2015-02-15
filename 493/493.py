"Project Euler 493"

from collections import Counter

colors = 7
marbles_per_color = 10
max_draws = 20

total_marbles = colors * marbles_per_color
expected_value = 0.0

def calc_prob_unique(drawn_uniques, drawn_dupes):
    "return the probability of drawing a uniquely colored marble"
    jar_uniques = total_marbles - drawn_uniques * marbles_per_color
    jar_dupes = drawn_uniques * marbles_per_color - (drawn_uniques + drawn_dupes)
    jar_total = float(jar_uniques + jar_dupes)
    return jar_uniques / jar_total

# Include the first draw.
states = {(1, 0): 1.0}
while len(states) > 0:
    next_states = Counter()
    for state, p_state in states.iteritems():
        drawn_uniques, drawn_dupes = state
        if drawn_uniques + drawn_dupes == max_draws:
            # We have reached the draw limit. Update the expected value
            expected_value += drawn_uniques * p_state
            continue
        if p_state == 0.0:
            # No chance. Skip this state.
            continue
        # Draw another marble from the jar.
        prob_unique = calc_prob_unique(drawn_uniques, drawn_dupes)

        # Adjust the probabilities for the next states.
        next_states[(drawn_uniques + 1, drawn_dupes)] += p_state * prob_unique
        next_states[(drawn_uniques, drawn_dupes + 1)] += p_state * (1 - prob_unique)
    states = next_states
print expected_value
