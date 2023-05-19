#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    // check is number between 1-8
    do
    {
        // get user input
        n = get_int("Enter num between 1-8: ");
    }
    while (n < 1 || n > 8);
    // print blocks
    for (int i = 0; i < n; i++)
    {
        // Loop to add spaces
        for (int k = n - i; k > 1; k--)
        {
            printf(" ");
        }
        // Loop to add hashes
        for (int j = 0; j <= i; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}