# Upper_bound and Lower_bound in Python

## Return First Number Larger than Target

```python
def upper(nums, target) :
    low, high = 0, len(nums) - 1
    pos = len(nums) :
    while low < high :
        mid = (low + high) // 2
        if nums[mid] <= target : low = mid + 1
        else : 
            high = mid
            pos = high
    if nums[low] > taget : pos = low
    return pos
```

## Return First Number Larger than or Equal to Target

```python

def upper_bound(nums, target):
    low, high = 0, len(nums)-1
    pos = len(nums)
    while low<high:
        mid=(low+high)/2
        if nums[mid]<=target:
            low = mid+1
        else:#>
            high = mid
            pos = high
    if nums[low]>target:
        pos = low
    return pos
```