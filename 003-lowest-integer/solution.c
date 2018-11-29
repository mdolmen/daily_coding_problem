#include <stdio.h>
#include <stdlib.h>

#define PRINT_ARRAY(values, nb) \
    for (int i = 0; i < nb; i++) printf("%d ", values[i])

int lowest_integer(int *array, int nb_elem)
{
    int lowest = 1;

    if (!array)
        exit(EXIT_FAILURE);

    // sort the array
    for (int i = 0; i < nb_elem-1; i++)
    {
        for (int j = 0; j < nb_elem-1; j++)
        {
            if (array[j] > array[j+1])
            {
                // XOR swap
                array[j] ^= array[j+1];
                array[j+1] ^= array[j];
                array[j] ^= array[j+1];
            }
        }
    }

    // search for the lowest not present integer
    for (int i = 0; i < nb_elem; i++)
    {
        if (array[i] <= 0)
            continue;

        if (array[i] >= lowest+1)
            break;

        lowest++;
    }

    return lowest;
}

int main(void)
{
    int array_1[6] = {3, 5, 4, -1, 1, 7};
    int array_2[3] = {0, 2, 1};
    int result = 0;

    result = lowest_integer(array_1, 6);
    printf("[+] Sorted array : ");
    PRINT_ARRAY(array_1, 6);
    printf("\n[+] Result : %d\n", result);

    result = lowest_integer(array_2, 3);
    printf("\n[+] Sorted array : ");
    PRINT_ARRAY(array_2, 3);
    printf("\n[+] Result : %d\n", result);

    return 0;
}
