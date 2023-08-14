#include "lists.h"
/**
 * check_cycle - check if linked list is circular
 * @list: pointer to head of list
 * Return: 0 if not 1 if is circular
 */
int check_cycle(listint_t *list)
{
	listint_t *car;
	listint_t *donkey;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}
	donkey = list;
	car = list;
	while (car != NULL && car->next != NULL)
	{
		if (car == donkey)
		{
			return (1);
		}
		donkey = donkey->next;
		car = car->next->next;
	}
	return (0);
}
