# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import time
import matplotlib.pyplot as plt

def power_naive(a, n):
  result = 1
  for i in range(n):
    result *= a
  return result

"iterative method is O(n)"

def power_divide_and_conquer(a, n):
  if n == 0:
    return 1
  elif n % 2 == 0:
    return power_divide_and_conquer(a * a, n // 2)
  else:
    return a * power_divide_and_conquer(a * a, n // 2)

"divide-and-conquer algorithm is O(log n)"

def plot_running_times(naive_running_times, divide_and_conquer_running_times):
  plt.plot(naive_running_times, label="Naive iterative method")
  plt.plot(divide_and_conquer_running_times, label="Divide-and-conquer method")
  plt.xlabel("n")
  plt.ylabel("Running time (seconds)")
  plt.legend()
  plt.show()

if __name__ == "__main__":
  naive_running_times = []
  divide_and_conquer_running_times = []
  for n in range(1, 10**6):
    naive_start_time = time.time()
    power_naive(2, n)
    naive_end_time = time.time()
    naive_running_time = naive_end_time - naive_start_time
    naive_running_times.append(naive_running_time)

    divide_and_conquer_start_time = time.time()
    power_divide_and_conquer(2, n)
    divide_and_conquer_end_time = time.time()
    divide_and_conquer_running_time = divide_and_conquer_end_time - divide_and_conquer_start_time
    divide_and_conquer_running_times.append(divide_and_conquer_running_time)

  plot_running_times(naive_running_times, divide_and_conquer_running_times)
  
  "YES , the experimental results confirm the theoretical analysis results in 1.(b)."

plt.show()

def find_pairs_with_sum(S, sum):

  S.sort()

  left = S[:len(S) // 2]
  right = S[len(S) // 2:]

  left_pairs = find_pairs_with_sum(left, sum)
  right_pairs = find_pairs_with_sum(right, sum)

  merged_pairs = []
  i = 0
  j = 0
  while i < len(left_pairs) and j < len(right_pairs):
    if left_pairs[i][0] + right_pairs[j][0] == sum:
      merged_pairs.append((left_pairs[i], right_pairs[j]))
      i += 1
      j += 1
    elif left_pairs[i][0] + right_pairs[j][0] < sum:
      i += 1
    else:
      j += 1

  for left_element in left:
    right_element = sum - left_element
    index = binary_search(right, right_element)
    if index != -1:
      merged_pairs.append((left_element, right[index]))

  return merged_pairs
plt.show()

def binary_search(S, element):
  low = 0
  high = len(S) - 1
  while low <= high:
    mid = (low + high) // 2
    if S[mid] == element:
      return mid
    elif S[mid] < element:
      low = mid + 1
    else:
      high = mid - 1

  return -1
plt.show()

"O(n log n) "
"""The algorithm divides the input problem into two subproblems of equal size.
    The algorithm solves the subproblems recursively.
    The cost of merging the solutions from the subproblems is O(n)."""
    
def experiment_with_scalability(n_range):
  results = []
  for n in n_range:
    S = set(range(n))
    sum = n // 2

    start_time = time.time()
    find_pairs_with_sum(S, sum)
    end_time = time.time()

    running_time = end_time - start_time

    results.append((n, running_time))

  return results
plt.show()

# Run the experiment.
results = experiment_with_scalability(range(1, 10**6))

# Plot the experimental results.
plt.plot([result[0] for result in results], [result[1] for result in results], 'bo-')
plt.xlabel('Input size (n)')
plt.ylabel('Running time (seconds)')
plt.title('Scalability of the proposed algorithm')
plt.show()


"O(n log n)"
plt.show()

