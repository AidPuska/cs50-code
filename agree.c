#include <stdio.h>
#include <cs50.h>

int main (void)
{
    char answer = get_char("Do you agree? y or n? ");

    if (answer == 'y' || answer == 'Y')
    {
        printf("Ok you agreed \n");
    }
    else if (answer == 'n' || answer == 'N')
    {
        printf("You declined \n");
    }
}