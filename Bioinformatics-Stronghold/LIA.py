# Every creature in each (non-0) generation has a 50% chance of being Aa, and Bb independantly => a 25% chance of being both
# Why? Because of the table for crossing anything with Aa, or with Bb
import usefulFunctions
f = open("rosalind_lia.txt", "r")
nums = f.readline().split(" ")
nums = [int(n) for n in nums]
print(nums[0])

print(usefulFunctions.choose(4,2))
print(sum([usefulFunctions.choose(2**nums[0],i)* 0.25**i *0.75**(2**nums[0]-i) for i in range(nums[1], 2**nums[0] + 1)]))