/*
 * There exists a staircase with N steps, and you can climb up either 1 or 2
 * steps at a time. Given N, write a function that returns the number of unique
 * ways you can climb the staircase. The order of the steps matters.
 * 
 * For example, if N is 4, then there are 5 unique ways:
 * 
 *     1, 1, 1, 1
 *     2, 1, 1
 *     1, 2, 1
 *     1, 1, 2
 *     2, 2
 * 
 * What if, instead of being able to climb 1 or 2 steps at a time, you could climb
 * any number from a set of positive integers X? For example, if X = {1, 3, 5}, you
 * could climb 1, 3, or 5 steps at a time.
 */

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

#define COUNT_OF(array) (sizeof(array) / sizeof(0[array]))

int ways_to_climb(int *x, int nb_elem, int n)
{
    int result = 0;

    for (int i = 0; i < nb_elem; i++)
    {
        if (x[i] == n)
        {
            result += 1;
            break;
        }

        if (x[i] < n)
            // we can climb x[i] steps at a time, check how many possible ways
            // we can climb the rest of them
            result += ways_to_climb(x, nb_elem, n-x[i]);
    }

    return result;
}

int main(void)
{
    int array_0[2] = {1, 2};
    int array_1[3] = {1, 3, 5};
    int n = 4, result = 0;

    result = ways_to_climb(array_0, COUNT_OF(array_0), n);
    assert(result == 5);

    n = 5;
    result = ways_to_climb(array_1, COUNT_OF(array_1), n);
    assert(result == 5);

    n = 6;
    result = ways_to_climb(array_1, COUNT_OF(array_1), n);
    assert(result == 8);

    puts("[+] All tests done.");

    return 0;
}
