#include <stdio.h>
#include <cs50.h>

int get_size(void);
void print_grid(int size);

int main(void)
{
    // get user input
    int n = get_size();

    // print grid of bricks
    print_grid(n);
}

int get_size(void)
{
    int n;
    do
    {
        n = get_int("Size: ");
    }
    while (n < 0);

    return n;
}

void print_grid(int size)
{
    for (int i = 0; i < size; i++)
    {
        for k 
        for (int j = 0; j < size; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}