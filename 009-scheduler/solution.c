/*
 * Implement a job scheduler which takes in a function f and an integer n, and
 * calls f after n milliseconds.
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <time.h>
#include <pthread.h>

typedef struct Task {
    void (*fct)();
    int delay;
    struct Task *pnx;
} Task;

Task t0;

void add(Task *list, Task *new)
{
    Task *previous = NULL;
    Task *current = list;
    Task *next = NULL;

    // get to the last item
    while ( (next = (Task *) ((uintptr_t)current->pnx ^ (uintptr_t)previous)) != NULL)
    {
        previous = current;
        current = next;
    }

    new->pnx = current;
    current->pnx = (Task *) ((uintptr_t)previous ^ (uintptr_t)new);
}

void polling()
{
    Task *previous = NULL, *next = NULL;
    Task *current = &t0;
    struct timespec timer0, timer1;
    int counter = 0; // milliseconds ellapsed

    timer0.tv_sec = 0;
    timer0.tv_nsec = 1000000;

    while (1)
    {
        if ( nanosleep(&timer0, &timer1) < 0 )
            exit(EXIT_FAILURE);
        counter++;

        // TODO : need a fix : doesn't go through all of the list
        // browse tasks and launch it if its time
        while ( (next = (Task *) ((uintptr_t)current->pnx ^ (uintptr_t)previous)) != NULL)
        {
            printf("next = %p\n", *next);
            printf("delay = %d - counter  = %d\n", current->delay, counter);
            if (counter > current->delay && current->delay != 0)
            {
                current->fct();
                // quick and dirty solution : should remove the element of the
                // list
                current->delay = 0;
            }

            previous = current;
            current = next;
        }

    }
}

void scheduler()
{
    pthread_t thp_id = 0;

    pthread_create(&thp_id, NULL, polling, NULL);
    pthread_join(thp_id, NULL);
}

void job0() { puts("Doing job 0.."); }
void job1() { puts("Doing Job 1.."); }
void job2() { puts("Doing Job 2.."); }
void job3() { puts("Doing Job 3.."); }

int main(void)
{
    Task t1, t2, t3;
    
    t0.fct = job0;
    t0.delay = 30;
    t0.pnx = NULL;
    
    t1.fct = job1;
    t1.delay = 5;
    t1.pnx = NULL;
    
    t2.fct = job2;
    t2.delay = 60;
    t2.pnx = NULL;
    
    t3.fct = job3;
    t3.delay = 80;
    t3.pnx = NULL;

    add(&t0, &t1);
    add(&t0, &t2);
    add(&t0, &t3);

    scheduler();

    return 0;
}
