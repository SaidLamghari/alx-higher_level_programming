#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - Start of function that inserts a number
 *			into a sorted singly linked list.
 * @head: The pointer.
 * @number: The number.
 * Return: the address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_nd;
	listint_t *crrt;
	
	new_nd = malloc(sizeof(listint_t));
	
	if (new_nd == NULL)
	{
		return (NULL);
	
	}
	new_nd->n = number;
	
	new_nd->next = NULL;
	
	if (*head == NULL || number < (*head)->n)
	{
		new_nd->next = *head;
		*head = new_nd;
	}
	else
	{
		crrt = *head;
		while (crrt->next != NULL && crrt->next->n < number)
			crrt = crrt->next;
		new_nd->next = crrt->next;
		crrt->next = new_nd;
	}

	return (new_nd);
}
