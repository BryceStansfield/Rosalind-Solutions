import re
f = open('rosalind_iprb.txt', 'r');
regex = re.search('([0-9]*) ([0-9]*) ([0-9]*)', f.read());
organisms = [int(regex.group(1)), int(regex.group(2)), int(regex.group(3))];																# [dom-homo, hetero, rec-homo]
children = [0, 0];					# [dom, non-dom]

# Dom part
children[0] += 4 * (organisms[0] * (organisms[0] - 1) + organisms[0] * organisms[1] + organisms[0] * organisms[2]);							# Whoever a dom-homo mates with produces a dom or hetero

# Hetero part
children[0] += 4 * (organisms[0] * organisms[1]) + 3 * organisms[1] * (organisms[1] - 1) + 2 * organisms[1] * organisms[2];
children[1] += (organisms[1] * (organisms[1] - 1)) + 2 * (organisms[1] * organisms[2]);

# Rec part
children[0] += 4 * (organisms[2] * organisms[0]) + 2 * organisms[2] * organisms[1];
children[1] += 2 * organisms[2] * organisms[1] + 4 * (organisms[2] * (organisms[2] - 1));

print(children[0] / (children[0] + children[1]));