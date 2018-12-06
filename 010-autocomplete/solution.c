/*
 * Implement an autocomplete system. That is, given a query string s and a set
 * of all possible query strings, return all strings in the set that have s as a
 * prefix.
 *
 * For example, given the query string de and the set of strings [dog, deer, deal],
 * return [deer, deal].
 * 
 * Hint: Try preprocessing the dictionary into a more efficient data structure to
 * speed up queries.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SIZE    26
#define TRUE    1
#define FALSE   0

typedef struct Trie {
    struct Trie* nodes[SIZE];
    char is_leaf;
} Trie;

Trie* init_node()
{
    Trie* new_node = NULL;

    new_node = malloc(sizeof(Trie));
    if (!new_node)
        exit(EXIT_FAILURE);

    for (int i = 0; i < SIZE; i++)
        new_node->nodes[i] = NULL;

    return new_node;
}

void insert_node(Trie* root, char* word)
{
    Trie *t = NULL;
    int len = 0, index = 0;

    if (!root || !word)
        return;

    len = strlen(word);
    t = root;

    for (int depth = 0; depth < len; depth++)
    {
        index = word[depth] - 'a';
        
        if (t->nodes[index] == NULL)
            t->nodes[index] = init_node();

        t = t->nodes[index];
    }

    t->is_leaf = TRUE;
}

void print_node(Trie* root, char* word, int depth)
{
    // last char of the word in this branch, print it
    if (root->is_leaf)
    {
        word[depth] = '\0';
        printf("%s\n", word);
    }

    // append characters of the sub-trie to 'word'
    for (int i = 0; i < SIZE; i++)
    {
        if (root->nodes[i])
        {
            word[depth] = i + 'a';
            print_node(root->nodes[i], word, depth+1);
        }
    }
}

/*
 * Print all words in of the trie that have the same prefix.
 */
void autocomplete(Trie* root, char* subword)
{
    Trie *t = NULL;
    char word[SIZE] = { '\0' };
    int index = 0, depth = 0, len = 0;

    if (!root || !subword)
        return;

    len = strlen(subword);
    t = root;

    for (int i = 0; i < len; i++)
    {
        index = subword[i] - 'a';
        
        if (t->nodes[index] == NULL)
            break;

        t = t->nodes[index];
    }

    // memorize the prefix
    memcpy(word, subword, len);

    print_node(t, word, depth + len);
}

int main(void)
{
    Trie *root = NULL;
    char word[SIZE] = { '\0' };
    int depth = 0;

    char *word_list[6] = { "bob", "spunge", "balloon", "ballers", "chip", "aerospace" };
    char *subword = "ba";

    root = init_node();
    for (int i = 0; i < 6; i++)
        insert_node(root, word_list[i]);

    puts("[+] ba* in :");
    print_node(root, word, depth);

    puts("--------------------");
    autocomplete(root, subword);

    return 0;
}
