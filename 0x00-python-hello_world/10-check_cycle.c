#include "lists.h"

/**
 * check_cycle - Satart of function that
 *			Checks if a singly linked list has a cycle in it.
 * @list: The pointer.
 * Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *s, *f;


	if (list == NULL)
	{
		return (0);
	}

	s = list;

	f = list->next;



	while (f != NULL && f->next != NULL)
	{


		if (s == f)
		{
			return (1);

		}
		s = s->next;

		f = f->next->next;
	}

	return (0);
}
