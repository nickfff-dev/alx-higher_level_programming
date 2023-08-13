#include "lists.h"

/**
* insert_node - inserts node to a sorted linked list
* @head: pointer to head of list
* @number: value to insert
* Return: address of new node
*/
listint_t *insert_node(listint_t **head, int number)
{
listint_t *current;
listint_t *new;
listint_t *prev = NULL;

new = (listint_t *) malloc(sizeof(listint_t));
if (new == NULL)
{
return (NULL);
}
new->n = number;
new->next = NULL;
if (*head == NULL)
{
*head = new;
return (new);
}
else
current = *head;
{
while (current != NULL && number > current->n)
{
prev = current;
current = current->next;
}
if (prev == NULL)
{
new->next = *head;
*head = new;
}
else
{
new->next = current;
prev->next = new;
}
}
return (new);
}
