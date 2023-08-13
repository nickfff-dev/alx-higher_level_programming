#include "lists.h"

/**
* is_palindrome - checks if a singly linked list is a palindrome
* @head: pointer to pointer of head of the list
* Return: 0 if not a palindrome, 1 if a palindrome
*/
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *temp;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (is_palindrome);
	}
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		temp = slow;
		slow = slow->next;
		temp->next = prev;
		prev = temp;
	}
	if (fast != NULL)
	{
		slow = slow->next;
	}
	while (slow != NULL)
	{
		if (prev->n != slow->n)
		{
			is_palindrome = 0;
			break;
		}
		prev = prev->next;
		slow = slow->next;
	}
	return (is_palindrome);
}
