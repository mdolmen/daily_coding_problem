/*
 * Given a list of integers, write a function that returns the largest sum of
 * non-adjacent numbers. Numbers can be 0 or negative.
 *
 * For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1,
 * 1, 5] should return 10, since we pick 5 and 5.
 *
 * Follow-up: Can you do this in O(N) time and constant space?
 */

#include <stdio.h>

#define MAX(a, b) ((a < b) ? b : a)

int sum_non_adjacents(int *array, int nb_elem)
{
    int inc = array[0]; // sum including the current number
    int exc = 0;        // sum excluding the current number
    int tmp = 0;

    for (int i = 1; i < nb_elem; i++)
    {
        tmp = inc;
        inc = exc + array[i];
        exc = MAX(tmp, exc);
    }

    return MAX(inc, exc);
}

int main(void)
{
    int values_1[4] = {5, 1, 1, 5};
    int values_2[4] = {5, 6, 2, 5};
    int values_3[5] = {5, 1, 10, 5, 8};

    if (sum_non_adjacents(values_1, 4) == 10)
        puts("[+] Test 1 OK.");
    if (sum_non_adjacents(values_2, 4) == 11)
        puts("[+] Test 2 OK.");
    if (sum_non_adjacents(values_3, 5) == 23)
        puts("[+] Test 3 OK.");

    return 0;
}
