/* Given an array of integers, return a new array such that each element at index i
 * of the new array is the product of all the numbers in the original array except
 * the one at i.
 * 
 * For example, if our input was [1, 2, 3, 4, 5], the expected output would be
 * [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be
 * [2, 3, 6].
 * 
 * Follow-up: what if you can't use division?
 */

#include <stdio.h>
#include <stdlib.h>

#define PRINT_ARRAY(values, nb) \
    for (int i = 0; i < nb; i++) printf("%d ", values[i])

/*
 * Straightforward answer with division.
 */
int *mpy_array(int *array, int nb_elem)
{
    int *mpy = NULL;
    int p = 1;

    mpy = (int*) malloc(sizeof(int) * nb_elem);
    if (!mpy)
        exit(EXIT_FAILURE);

    for (int i = 0; i < nb_elem; i++)
        p *= array[i];

    for (int i = 0; i < nb_elem; i++)
        mpy[i] = p / array[i];

    return mpy;
}

/*
 * Without division.
 */
int *mpy_array_v2(int *array, int nb_elem)
{
    int *mpy_order = NULL;
    int *mpy_reverse = NULL;
    int *result = NULL;
    int p1 = 1, p2 = 1;

    mpy_order = (int*) malloc(sizeof(int) * nb_elem);
    mpy_reverse = (int*) malloc(sizeof(int) * nb_elem);
    result = (int*) malloc(sizeof(int) * nb_elem);

    for (int i = 0; i < nb_elem; i++)
    {
        // successive multiplication in normal order
        mpy_order[i] = array[i] * p1;
        p1 *= array[i];

        // successive multiplication in reverse order
        mpy_reverse[i] = array[nb_elem-1-i] * p2;
        p2 *= array[nb_elem-1-i];
    }

    for (int i = 0; i < nb_elem; i++)
    {
        if (i == 0)
            result[i] = mpy_reverse[nb_elem-2];
        else if (i == nb_elem-1)
            // the last element of mpy_reverse is the multiplication of all the
            // component of the array, we don't need it, so -2
            result[i] = mpy_order[nb_elem-2];
        else
            result[i] = mpy_order[i-1] * mpy_reverse[nb_elem-2-i];
    }

    free(mpy_order);
    free(mpy_reverse);

    return result;
}

int main(void)
{
    // expected result : 120 60 40 30 24
    // expected result : 240 840 560 420 336 840
    int values_1[5] = {1, 2, 3, 4, 5};
    int values_2[6] = {7, 2, 3, 4, 5, 2};
    int *result = NULL;

    // with division
    result = mpy_array(values_1, 5);
    PRINT_ARRAY(result, 5);
    putchar('\n');
    free(result);

    result = mpy_array(values_2, 6);
    PRINT_ARRAY(result, 6);
    putchar('\n');
    free(result);

    // without division
    putchar('\n');
    result = mpy_array_v2(values_1, 5);
    PRINT_ARRAY(result, 5);
    putchar('\n');
    free(result);

    result = mpy_array_v2(values_2, 6);
    PRINT_ARRAY(result, 6);
    putchar('\n');
    free(result);

    return 0;
}
