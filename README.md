# COP4533-PA2








## Questions

###Question 1:
<img width="632" height="88" alt="image" src="https://github.com/user-attachments/assets/6d15d0d5-0bc7-4751-a790-0082b14952fb" />

	
OPTFF has the fewest misses for all 3 files. FIFO and LRU tend to have a similar number of misses regardless of input size and cache size. The exact sequence of numbers that is used might determine which of the two algorithms is best in that context.

###Question 2:
Sequence: 1, 2, 3, 4, 1, 2
<img width="634" height="50" alt="image" src="https://github.com/user-attachments/assets/e312bcd6-2107-4177-92a7-b896ff6eda8c" />


In this sequence, only OPTFF provides the fewest number of misses because it can correctly evict 3 from the cache when 4 is requested. At that stage of the sequence, 1, 2, and 3 had all only been used once, so 1 would be both the first item in the cache and the least recently used item and would therefore be evicted by both FIFO and LRU and replaced with 4. OPTFF would instead have evicted 3 because both 1 and 2 are requested again in the future. The next step would be to request 1, but since the FIFO and LRU caches don’t contain 1, they have a miss that the OPTFF cache doesn’t have. At this point, 2 is both the first item in the cache and the least recently used item, so 2 would be replaced by 1. Since 2 is no longer in the cache, the final request leads to a second miss that was avoided by the OPTFF cache.

###Question 3:
Proof: 
-	Suppose we have a cache of size k > 1 and a series of integer requests, r_1, r_2, …, r_m
-	If k = 1, the number of misses will be the minimum possible since the OPTFF algorithm only evicts the current item when a different item is requested
-	Suppose then that there are at least two items c_1 and c_2 in the cache, and that c_2 has a request farther in the future than c_1
-	When request r_x arrives, the algorithm must decide whether to evict item c_1 or item c_2 and replace it with c_x
-	Case 1: c_2 is evicted by OPTFF
  -	Items c_1 and c_x remain in the cache
  -	Item c_1 is requested before item c_2, but no misses occur since c_1 is already in the cache
  -	When request r_y arrives, OPTFF determines that item c_1 should be evicted
  -	It is possible that c_1 may be requested at least one more time before c_2, so the minimum number of misses from this interaction is 2
-	Case 2: c_1 is evicted by algorithm A
  -	Items c_x and c_2 remain in the cache
  -	Item c_1 is requested before item c_2, so another eviction will have to occur
  -	When request r_y arrives, algorithm A may once again evict c_1
  -	It is possible that c_1 may be requested at least one more time before c_2, so the minimum number of misses from this interaction is 3
  -	If algorithm A had evicted c_1 initially, like what OPTFF had done, then the two algorithms would have the same number of misses from this interaction
  -	Therefore, A can at best have the same number of misses as OPTFF
