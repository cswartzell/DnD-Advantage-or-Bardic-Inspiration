import itertools
from collections import Counter
import matplotlib.pyplot as plt

frst_d = range(1, 21)
scnd_d = range(1, 21)

# "ADVANTAGE  -Sometimes a special ability or spell tells you that you have advantage or disadvantage
# on an ability check, a saving throw, or an attack roll. When that happens, you roll a second d20
# when you make the roll. Use the higher of the two rolls if you have advantage" -D&D
# Spells that grant advantage: Guiding Bolt (attacks), Enhance Ability (ability checks)

# generate Cartesian Product of our two d20, then probabilties of each result (0-20)
advntg = Counter(map(max, itertools.product(frst_d, scnd_d)))
advntg_p = [0.0] + [advntg[x] / (len(frst_d) * len(scnd_d)) for x in advntg.keys()]
advntg_at_least = [1 - sum(advntg_p[0:x]) for x in range(len(advntg_p))]

# "BLESS - You bless up to three creatures of your choice within range. Whenever a target makes an
# attack roll or a saving throw before the spell ends, the target can roll a d4 and add the number
# rolled to the attack roll or saving throw." -D&D 5e

# Do the same for 1d20 adding the Bless spell, 1d4 for a level 1 casting
scnd_d = range(1, 5)
bless = Counter(map(sum, itertools.product(frst_d, scnd_d)))
bless_p = [0.0] + [0.0] + [bless[x] / (len(frst_d) * len(scnd_d)) for x in bless.keys()]
bless_at_least = [1 - sum(bless_p[0:x]) for x in range(len(bless_p))]

# Plot Advantage
plt.plot(range(len(advntg_at_least)), advntg_at_least, label="Advantage: ")
# Plot Guidance/Bless (+1d4)
plt.plot(range(len(bless_at_least)), bless_at_least, label="+1d4: ")

plt.xlabel("Roll Result")
plt.ylabel("Probability")
plt.title("Probability of Rolling At Least X")
plt.legend()
plt.show()
