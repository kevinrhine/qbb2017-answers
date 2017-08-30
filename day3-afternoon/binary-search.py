#!/usr/bin/env python

nums = range(0,100,10)
print nums

key = 90

for i in xrange(len(nums)):
    v = nums[i]

lo = 0
hi = len(nums)

while lo < hi:
    mididx = (lo + hi) / 2
    mid = nums[mididx]
    if mid == key:
        print mid
        print "found it! the key is %s" % (mid)
        break   
    elif mid > key:
        hi = mididx
    elif mid < key:
        lo = mididx + 1
            
    