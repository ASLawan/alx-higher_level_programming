#include "lists.h"
/**
* insert_node - inserts new_node to a linked list
* @head: pointer to beginning of list
* @number: index to insert node
* Return: linked list
*/
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new_node = malloc(sizeof(listint_t));
if (new_node == NULL)
{
return (NULL);
}
new_node->n = number;
if (*head == NULL || (*head)->n >= number)
{
new_node->next = *head;
*head = new_node;
}
else
{
listint_t *temp = *head;
while (temp->next != NULL && temp->next->n < number)
{
temp = temp->next;
}
new_node->next = temp->next;
temp->next = new_node;
}
return (new_node);
}
