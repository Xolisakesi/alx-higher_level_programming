#include "lists.h"
#include <stdlib.h>
/**
* reverse_listint - Reverses a singly linked list.
* @head: Pointer to a pointer to the head of the list.
*
* Description: This function reverses the given linked list in-place.
*/
void reverse_listint(listint_t **head)
{
listint_t *prev = NULL;
listint_t *current = *head;
listint_t *next = NULL;

while (current != NULL) {
next = current->next;
current->next = prev;
prev = current;
current = next;
}

*head = prev;
}

/**
* is_palindrome - Checks if a linked list is a palindrome.
* @head: Pointer to a pointer to the head of the list.
*
* Return: 1 if the list is a palindrome, 0 otherwise.
*/
int is_palindrome(listint_t **head) 
{
if (*head == NULL || (*head)->next == NULL) 
{
return (1);
}

listint_t *slow = *head;
listint_t *fast = *head;

while (fast != NULL && fast->next != NULL) {
slow = slow->next;
fast = fast->next->next;
}
listint_t *second_half = slow;
reverse_listint(&second_half);

while (second_half != NULL) 
{
if ((*head)->n != second_half->n) {
return (0); /* Not a palindrome.*/
}
*head = (*head)->next;
second_half = second_half->next;
}
return (1);
}
