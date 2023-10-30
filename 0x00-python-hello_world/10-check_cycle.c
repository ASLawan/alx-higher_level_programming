#include "lists.h"
/**
 * check_cycle - checks if a linked list is cyclic
 * @list: linked list
 * Return: 0 on success and 1 otherwise
 */
int check_cycle(listint_t *list)
{
	int flag = 0;
	listint_t *fast = list;
	listint_t *slow = list;

	fast = fast->next->next;
	slow = slow->next;

	while (fast != NULL && slow != NULL)
	{
		if (fast == slow)
		{
			flag = 1;
			break;
		}
		fast = fast->next->next;
		slow = slow->next;
	}
	return (flag);
}
