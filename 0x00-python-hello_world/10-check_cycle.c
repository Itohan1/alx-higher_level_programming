#include "lists.h"

/**
 * check_cycle - checks for list cycle
 * @list: parameter
 * Return: 1 or 0
 */

int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *second = list;

	while (first != NULL && second != NULL && second->next != NULL)
	{
		first = first->next;
		second = second->next->next;

		if (first == second)
		{
			return (1);
		}

	}
	return (0);
}
