#include "lists.h"
void reverse_list(listint_t **head);
int compare_lists(listint_t *h1, listint_t *h2);
int is_padlindrome(listint_t **head);
/**
 * reverse_list - reverses a linked list
 * @head: start of list
 * Return: nothing
 */
void reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;

		current = next;
	}
	*head = prev;
}

/**
 * compare_lists - compares two linked lists
 * @h1: start of list one
 * @h2: start of list two
 * Return: 1 on success, 0 otherwise
 */
int compare_lists(listint_t *h1, listint_t *h2)
{
	int l1 = 0, l2 = 0;
	listint_t *current1 = h1;
	listint_t *current2 = h2;

	while (current1 != NULL)
	{
		l1++;
		current1 = current1->next;
	}
	while (current2 != NULL)
	{
		l2++;
		current2 = current2->next;
	}
	if (l1 != l2)
	{
		return (0);
	}
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
/**
 * is_palindrome - checks if list is palindrome
 * @head: start of list
 * Return: 0 on success, 1 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev = *head;
	listint_t *second_half, *middle = NULL;
	int result = 0;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev = slow;
			slow = slow->next;
		}
		if (fast != NULL)
		{
			middle = slow;
			slow = slow->next;
		}
		second_half = slow;
		prev->next = NULL;
		reverse_list(&second_half);
		result = compare_lists(*head, second_half);
		reverse_list(&second_half);
		if (middle != NULL)
		{
			prev->next = middle;
			middle->next = second_half;
		}
		else
		{
			prev->next = second_half;
		}
	}
	return (result);
}
