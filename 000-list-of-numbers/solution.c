#include <stdio.h>
#include <stdlib.h>

void find_sum_terms(int k, int *values, int size)
{
    int tmp = 0;
    char *seen = NULL;

    // we can't have a number bigger than k
    seen = (char*)malloc(sizeof(int) * k);
    if (!seen)
        exit(EXIT_FAILURE);

    for (int i = 0; i < size; i++)
    {
        tmp = k - values[i];
        if (seen[tmp] == 1)
        {
            printf("[+] Found two numbers that add up to %d : %d + %d\n",
                k,
                values[i],
                (unsigned int) (&seen[tmp] - seen)
            );
            break;
        }
        else if (i == size-1)
            puts("[-] No solution found.");

        seen[values[i]] = 1;
    }

    free(seen);
}

int main(void)
{
    int values_1[4] = {10, 15, 3, 7};
    int values_2[5] = {1, 2, 3, 13, 78};
    int values_3[1] = {10};
    int values_4[5] = {2, 3, 2, 1, 9};
    int k_1 = 17;
    int k_2 = 15;
    int k_3 = 9;
    int k_4 = 6;

    find_sum_terms(k_1, values_1, sizeof(values_1) / sizeof(int));
    find_sum_terms(k_2, values_2, sizeof(values_2) / sizeof(int));
    find_sum_terms(k_3, values_3, sizeof(values_3) / sizeof(int));
    find_sum_terms(k_4, values_4, sizeof(values_4) / sizeof(int));

	return 0;
}
