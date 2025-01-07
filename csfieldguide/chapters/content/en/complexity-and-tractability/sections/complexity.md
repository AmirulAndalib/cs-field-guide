# Complexity

Complexity is a fancy word that usually means an indication of how much time an algorithm will take to complete. 
It is usually measured in the number of steps an algorithm takes, rather than the amount of time, since the time depends on what kind of computer you run it on. 
Complexity for an algorithm is often separated into best, average and worst case. 

For example, the Python “in” function applied to a list does a sequential search by checking each value in sequence until it either finds the value wanted, or gets to the end of the list.
The three complexity cases for this are:

- Best case, when the value being searched for is first in the list e.g. 45 in [45, 32, 52]

This only takes one step - the value 45 is compared with the first 45 in the list, and the algorithm stops. 
You’re probably thinking that the best case is a bit optimistic, and it is! 
If there were a million items in the list, there’s only one chance in a million that the best case will happen. 
The best case is not very useful in this case, but for some algorithms their best case is terrible, in which as it’s not even worth worrying about the other cases.

- Worst case, when the value being searched for is last in the list e.g. 52 in [45, 32, 52]

This example will take 3 comparisons, and you can’t do worse than that. 
If there were a million items in the list, it would take a million steps, and you need to be aware that there’s this possibility that it might occasionally take that long (which would really annoy the person waiting for it.) 
It seems pessimistic, but it’s useful to know that it might happen sometimes, and if that’s not acceptable, you’d use a different algorithm.

- Average case, which is what happens averaged over lots of searches. 

Sometimes the value will be near the start of the list, and sometimes near the end, but on average the algorithm will go about halfway through the list. 
If the list has a million values in it, then on average it will take about half a million steps. 
This is a realistic view of the algorithm’s performance.


