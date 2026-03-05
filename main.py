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
        for c in cache:
            if c[0] == r:
                hits += 1
                found = True
            c[1] += 1
        if not found:
            misses += 1
            if cache_size < k:
                cache_size += 1
                cache.append([r, 0])
            else:
                first_index = 0
                max = 0
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
        for c in cache:
            if c[0] == r:
                hits += 1
                c[1] = -1
                found = True
            c[1] += 1
        if not found:
            misses += 1
            if cache_size < k:
                cache_size += 1
                cache.append([r, 0])
            else:
                lru_index = 0
                max = 0
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
        for c in cache:
            if c[0] == requests[r]:
                hits += 1
                found = True

                distance = 0
                repeats = False
                for j in range(r+1, len(requests)):
                    distance += 1
                    if requests[j] == c[0]:
                        repeats = True
                        break
                if repeats:
                    c[1] = distance + 1
                else:
                    c[1] = 9999
            if c[1] != 9999:
                c[1] -= 1
            #print("distance: ", c[1])
        if not found:
            misses += 1
            if cache_size < k:
                cache_size += 1

                distance = 0
                repeats = False
                for j in range(r + 1, len(requests)):
                    distance += 1
                    if requests[j] == requests[r]:
                        repeats = True
                        break
                if repeats:
                    cache.append([requests[r], distance])
                    #print(" nf distance: ", distance)
                else:
                    cache.append([requests[r], 9999])
                    #print(" nf distance:  9999")

            else:
                farthest_index = 0
                max = 0
                for i in range(len(cache)):
                    if cache[i][1] > max:
                        max = cache[i][1]
                        farthest_index = i
                cache[farthest_index][0] = requests[r]

                distance = 0
                repeats = False
                for j in range(r + 1, len(requests)):
                    distance += 1
                    if requests[j] == c[0]:
                        repeats = True
                        break
                if repeats:
                    c[1] = distance
                else:
                    c[1] = 9999
                cache[farthest_index][1] = 0
        print(cache)
    return misses


def read_input() -> tuple[int, int, List[int]]:
    # If an input file exists under ./cache_input, use the first one.
    file = open("cache_input/input.in", "r")
    line_0 = file.readline()
    line_1 = file.readline()
    k, m = line_0.strip().split()
    str_requests = line_1.strip().split()
    int_requests = []
    for r in str_requests:
        int_requests.append(int(r))
    return int(k), int(m), int_requests


def main() -> None:
    #Main file
    k, m, requests = read_input()
    print(k)
    print(m)
    print(requests)

    fifo = first_in_first_out(k, m, requests)
    lru = least_recently_used(k, m, requests)
    optff = farthest_in_future(k, m, requests)

    print("FIFO \t:", fifo)
    print("LRU  \t:", lru)
    print("OPTFF\t:", optff)


if __name__ == "__main__":
    main()