from __future__ import annotations
import sys
import time
from pathlib import Path
from typing import List


def first_in_first_out(k: int, m: int, requests: List[int]) -> int:
    cache = []
    cache_size = 0
    misses = 0
    hits = 0

    for r in requests:
        found = False
        #Look for ID in cache
        for c in cache:
            if c[0] == r:
                hits += 1
                found = True
            # Increase lifespan of each value in cache
            c[1] += 1
        if not found:
            misses += 1
            if cache_size < k:
                # If cache not full, add ID to cache
                cache_size += 1
                cache.append([r, 0])
            else:
                # If cache full, evict an item
                first_index = 0
                max = 0
                # Search for ID with largest lifespan
                for i in range(len(cache)):
                    if cache[i][1] > max:
                        max = cache[i][1]
                        first_index = i
                cache[first_index][0] = r
                cache[first_index][1] = 0
    return misses


def least_recently_used(k: int, m: int, requests: List[int]) -> int:
    cache = []
    cache_size = 0
    misses = 0
    hits = 0

    for r in requests:
        found = False
        # Look for ID in cache
        for c in cache:
            if c[0] == r:
                hits += 1
                c[1] = -1
                found = True
            # Increase time since accessed by 1
            c[1] += 1
        if not found:
            misses += 1
            if cache_size < k:
                # If cache not full, add item
                cache_size += 1
                cache.append([r, 0])
            else:
                # Cache is full, evict item
                lru_index = 0
                max = 0
                # Search for ID with longest time since accessed
                for i in range(len(cache)):
                    if cache[i][1] > max:
                        max = cache[i][1]
                        lru_index = i
                cache[lru_index][0] = r
                cache[lru_index][1] = 0
    return misses


def farthest_in_future(k: int, m: int, requests: List[int]) -> int:
    cache = []
    cache_size = 0
    misses = 0
    hits = 0

    for r in range(len(requests)):
        found = False
        # Look for ID in cache
        for c in cache:
            if c[0] == requests[r]:
                hits += 1
                found = True

                # Update item with new distance to future copy
                distance = 0
                repeats = False
                # Find distance to future copy
                for j in range(r+1, len(requests)):
                    distance += 1
                    if requests[j] == c[0]:
                        repeats = True
                        break
                if repeats:
                    c[1] = distance + 1
                else:
                    # Set distance to a large value if the item ID does not repeat
                    c[1] = 9999
            if c[1] != 9999:
                c[1] -= 1
        if not found:
            misses += 1
            if cache_size < k:
                # If cache not full, add to cache
                cache_size += 1

                # Find distance to future copy
                distance = 0
                repeats = False
                for j in range(r + 1, len(requests)):
                    distance += 1
                    if requests[j] == requests[r]:
                        repeats = True
                        break
                if repeats:
                    cache.append([requests[r], distance])
                else:
                    # Set distance to a large value if the item ID does not repeat
                    cache.append([requests[r], 9999])
            else:
                # If cache is full, evict an item
                farthest_index = 0
                max = 0
                # Find ID with farthest repetition
                for i in range(len(cache)):
                    if cache[i][1] > max:
                        max = cache[i][1]
                        farthest_index = i
                cache[farthest_index][0] = requests[r]

                distance = 0
                repeats = False
                # Find distance to next repetition
                for j in range(r + 1, len(requests)):
                    distance += 1
                    if requests[j] == requests[r]:
                        repeats = True
                        break
                if repeats:
                    cache[farthest_index][1] = distance
                else:
                    # Set distance to a large value if the item ID does not repeat
                    cache[farthest_index][1] = 9999
        #print(cache)
    return misses


def read_input() -> tuple[int, int, List[int]]:
    # Parse input file and extract variables
    file = open("cache_input/input.txt", "r")
    line_0 = file.readline()
    line_1 = file.readline()
    k, m = line_0.strip().split()
    str_requests = line_1.strip().split()
    int_requests = []
    for r in str_requests:
        int_requests.append(int(r))
    return int(k), int(m), int_requests


def main() -> None:
    k, m, requests = read_input()

    fifo = first_in_first_out(k, m, requests)
    lru = least_recently_used(k, m, requests)
    optff = farthest_in_future(k, m, requests)

    #Format output string
    fifo_out = "FIFO \t: " + str(fifo) + "\n"
    lru_out = "LRU  \t: " + str(lru) + "\n"
    optff_out = "OPTFF \t: " + str(optff) + "\n"

    #Create output file if none exists
    try:
        file = open("cache_output/output.txt", "w")
    except:
        file = open("cache_output/output.txt", "x")
    file.write(fifo_out)
    file.write(lru_out)
    file.write(optff_out)

if __name__ == "__main__":
    main()