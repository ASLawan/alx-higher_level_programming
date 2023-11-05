#include "lists.h"
/**
* is_palindrome - checks if list is a palindrome
* @head: pointer start of list
* Return: 1 on success and 0 otherwise
*/
int is_palindrome(listint_t **head)
{
listint_t *reversed_head = NULL;
listint_t *current = *head;
listint_t *next = NULL;

while (current != NULL)
{
next = current->next;
current->next = reversed_head;
reversed_head = current;
current = next;
}

listint_t *current1 = *head;
listint_t *current2 = reversed_head;
while (current1 != NULL && current2 != NULL)
{
if (current1->n != current2->n)
{
return (0);
}
current1 = current1->next;
current2 = current2->next;
}

return (1);
}
