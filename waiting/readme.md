# Waiting
## Problem Statement
After a controversial exam, students at LHS are eager to confront their teacher about their test scores. N students numbered 1 through N each attempt to enter a classroom at a unique time T[i], and argue with the teacher for M minutes before leaving in a fit of anger. However, if the amount of people inside the room exceeds a limit of L students, a student must wait for another student to leave before he may enter. If multiple students are waiting outside the room at once, the student who arrived first has priority to enter first.

Find the total amount of time for which the teacher is the only person in the room, starting from when the first student enters, until the last student leaves.

### Additional Notes
Time Limit:
C++: 2.5 seconds
Java, Python: 5 seconds
Memory Limit: 128mb
Finally, the problem uses standard IO(so not reading files)

### Constraints
1 ≤ N ≤ 1000
1 ≤ M ≤ 100
1 ≤ L ≤ 100
1 ≤ t[i] ≤ 100000

### Input format
On line 1, N, M, L are given.
On line 2, there are N integers, with the ith integer being t[i]. Is it guaranteed that they are in increasing order and are distinct.

### Output format
You should output one integer equivialent to the total amount of time for which the teacher is the only person in the room.

### Sample input:
5 4 2
1 3 4 13 18

### Sample output
5

### Sample Explanation
The first student comes in at 1 and will leave at 4. The second student comes in at 3 and will leave at 6. The third student comes in at 4; however, since there are two students already, he waits 1 second for the first student to leave, hence entering at 5, and will be leaving at 8. After the second and third students leave, the teacher is alone for 4 minutes (9,10,11,12). Then the fourth student comes in at 13 and leaves at 16. The teacher is again alone for another minute. Finally, the final student comes at 18 and leaves at 21. This gives a total alone time of 5 minutes.

Credit: Hannah S

# Solution
TODO
