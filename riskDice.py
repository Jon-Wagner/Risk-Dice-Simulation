import numpy as np
import matplotlib.pyplot as plt

max_num_units = 20
num_trials = int(1e7)
num_defender_dice = 2
num_attacker_dice = 3
defender_wins_ties = True
results = np.zeros((max_num_units, max_num_units))

# run trial_count simulations of attacking a space with some number of attacking and defending units, then store their result
def Run_Trial(defending_units, attacking_units, result_storage, trial_count):
    attacker_victory_count = 0
                
    for trial_number in range(trial_count):
        remaining_attacking_units = attacking_units
        remaining_defending_units = defending_units
            
        while remaining_attacking_units > 0 and remaining_defending_units > 0:
            attacker_roll = np.random.randint(1,7,num_attacker_dice)
            defender_roll = np.random.randint(1,7,num_defender_dice)
                
            attacker_roll.sort()
            defender_roll.sort()
            
            # check to see who one each die pairing, and decrement the appropriate counter
            for i in range(2):
                if attacker_roll[i] > defender_roll[i]:
                    remaining_defending_units -= 1
                else:
                    remaining_attacking_units -= 1
        
        # check if the attacker lost, otherwise they won
        if remaining_attacking_units == 0:
            attacker_victory_count += 1
                
    result_storage[defending_units, attacking_units] = attacker_victory_count / trial_count

for num_defending_units in range(1,max_num_units+1):
    for num_attacking_units in range(1,max_num_units+1):
        Run_Trial(num_defending_units, num_attacking_units, results, num_trials)        
        
print(results)

# Now for a bunch of plotting stuff
# first, set up the plot
column_labels = range(1,max_num_units+1)
row_labels = range(1,max_num_units+1)
fig, ax = plt.subplots()

# plt.cm.Blues results in a higher chance of attacker victory being a darker blue
heatmap = ax.pcolor(results, cmap=plt.cm.Blues)

# put the major ticks at the middle of each cell
ax.set_xticks(np.arange(results.shape[0])+0.5, minor=False)
ax.set_yticks(np.arange(results.shape[1])+0.5, minor=False)

# label the axis
plt.ylabel("Number of attacking units")
plt.xlabel("Number of defending units")

# label the ticks on each axis
ax.set_xticklabels(row_labels, minor=False)
ax.set_yticklabels(column_labels, minor=False)

plt.show()