#include "lists.h"
/**
* is_palindrome - checks if list is a palindrome
* @head: pointer start of list
* Return: 1 on success and 0 otherwise
*/
int is_palindrome(listint_t **head)
{
	listint_t *start = *head;
	listint_t *temp = *head;
	int i, j, middle, length = 0;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
	while (temp)
	{
		length += 1;
		temp = temp->next;
	}
	middle = length / 2;
	int nodes[length];

	for (i = 0; start; i++)
	{
		nodes[i] = start->n;
		start = start->next;
	}
	j = length - 1;
	for (i = 0; i < middle; i++, j--)
	{
		if (nodes[i] != nodes[j])
		{
			return (0);
		}
	}
	return (1);
}
