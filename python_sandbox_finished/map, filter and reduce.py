from functools import reduce  # reduce not nativaly available since python ver 3.0
from functional import seq  # needs the package pyfunctional
import re

l1 = [2, 3, 4, 5, 6]

# map
mapping_the_l1 = list(map(lambda x: x * 2, l1))

print("mapping the list", mapping_the_l1)

# filter
# filter down to whatever returned True (filter out whatever returned False)
filtering_the_l1 = list(filter(lambda x: x % 2 == 0, l1))
print("filtering the list", filtering_the_l1)


l2 = [1, 1, 1, 1, 1]

# reduce
reducing_with_initial = reduce(lambda acc, curr: acc + curr * 2, l2, 10)
print("reducing the list with initial", reducing_with_initial)

# reduce (if no initial value supplied, the first element is used as return value
# and we start from the second iteration)
reducing = reduce(lambda acc, curr: acc + curr * 2, l2)
print("reducing the list", reducing)

#####################################################################

# map and filter do not return a list, but an iterable
# print(map(lambda x: x * 2, l1)) # <map object at 0x7f89f01ea950>

# However, they can be chained using the seq func (also reduce):

res = (
    seq(l1)
    .map(lambda x: x**2)
    .filter(lambda x: x % 2 == 0)
    .reduce(lambda acc, curr: acc + curr, 100)
)

print("chaining with seq:", res)

# can also do seq() on a dict and then in the lambda use x[0] and x[1] for key and value

# https://stackoverflow.com/questions/13638898/how-to-use-filter-map-and-reduce-in-python-3
"""python as a language is a mess - but it has v good to excellent libraries:
  numpy, pandas, statsmodels and friends..
  I had been buliding convenience libraries like you show here to reduce the pain of the native language
  - but have lost the energy and try not to stray far from a data.frame / datatable, or xarray.
  But kudos for trying"""


# From Kaggle:
def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword.
    Returns list of the index values into the original list for all documents
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    return (
        seq(enumerate(doc_list))
        .map(
            lambda item: (
                item[0] if keyword.lower() in re.split(" |\.", item[1].lower()) else -1
            )
        )
        .filter(lambda x: x > -1)
    )


doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
print(word_search(doc_list, "casino"))
