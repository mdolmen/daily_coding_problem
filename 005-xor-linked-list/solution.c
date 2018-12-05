/*
 * An XOR linked list is a more memory efficient doubly linked list. Instead of
 * each node holding next and prev fields, it holds a field named both, which is
 * an XOR of the next node and the previous node. Implement an XOR linked list;
 * it has an add(element) which adds the element to the end, and a get(index)
 * which returns the node at index.

 * If using a language that has no pointers (such as Python), you can assume you
 * have access to get_pointer and dereference_pointer functions that converts
 * between nodes and memory addresses.
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

// node of an XOR doubly linked list
typedef struct Node {
    int value;
    struct Node *pnx; // Previous Next XOR
} Node;

void add(Node *list, Node *new)
{
    Node *previous = NULL;
    Node *current = list;
    Node *next = NULL;

    // get to the last item
    while ( (next = (Node *) ((uintptr_t)current->pnx ^ (uintptr_t)previous)) != NULL)
    {
        previous = current;
        current = next;
    }

    new->pnx = current;
    current->pnx = (Node *) ((uintptr_t)previous ^ (uintptr_t)new);
}

Node *get(Node *head, int index)
{
    Node *previous = NULL;
    Node *current = head;
    Node *next = NULL;
    int i = 0;

    if (index < 0)
        return NULL;

    // get to the last item
    while (current != NULL)
    {
        next = (Node *) ((uintptr_t)current->pnx ^ (uintptr_t)previous);

        if (i == index)
            return current;

        previous = current;
        current = next;

        i++;
    }

    return NULL;
}

void print_list(Node *head)
{
    Node *previous = NULL;
    Node *current = head;
    Node *next = NULL;

    while (current != NULL)
    {
        next = (Node *) ((uintptr_t)current->pnx ^ (uintptr_t)previous);
        printf("value: %d\n", current->value);
        previous = current;
        current = next;
    }
}

int main(void)
{
    Node head, n2, n3, n4;
    Node *n5 = NULL;

    head.value = 10;
    head.pnx = NULL;

    n2.value = 20;
    n2.pnx = NULL;
    add(&head, &n2);
    
    n3.value = 30;
    n3.pnx = NULL;
    add(&head, &n3);

    n4.value = 40;
    n4.pnx = NULL;
    add(&head, &n4);

    print_list(&head);

    n5 = get(&head, 1);
    printf("list[1].value = %d\n", n5->value);

    return 0;
}
