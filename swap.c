#include <cs50.h>
#include <stdio.h>

void swap(int *a, int *b);

int main(void)
{
    int x = get_int("x: ");
    int y = get_int("y: ");

    printf("Before swap: x: %i and y: %i\n", x, y);
    swap(&x, &y);
    printf("After swap: x: %i and y: %i\n", x, y);
}

void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}