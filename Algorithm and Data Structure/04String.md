# String

## String Python Function

```python
str.index(str, beg = 0 end = len(string))
# Index if found otherwise raises an exception if str is not found.
str.find(str, beg = 0 end = len(string))
#Determine if str occurs in string or in a substring of string if starting index beg and ending index end are given returns index if found and -1 otherwise.
str.count()
str.join()
str.split()
str.strip()
str.isalnum()
str.isalpha()
str.isdigit()
```

## KMP (Knuth-Morris-Pratt)

Given a string *S* and a pattern *p*, find all occurrences of *p* in *s*.

- Naive Algorithm (Brutal Force)
  - Worst Case : O(n * m)
  - Average Case : O(n + m)
- KMP (Fast Pattern Matching in Strings)
  - Guaranteed worst case performance : O(m + n)
    - Two stages :
      - Pre-processing : table building : O(m)
      - Matching : O(n)
  - Space complexity : O(m)

```python
def build(p) :
    """
    Args :
        p : pattern to build
    """
    

def match(s, p) :
    """
    Args :
        s : input string
        p : pattern to search
    """
    ans = []
    nxt = build(p)
    idx = 0
    for i in range(len(s)) :
        while idx > 0 and s[i] != p[idx] :
            idx = nxt[idx]
        if s[i] == p[idx] :
            idx += 1
        if idx = len(p) :
            ans.append(i - len(p) + 1)
            idx = nxt[idx]
    return ans
```


