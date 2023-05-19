#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    string letters[] = {"ab", "cd", "ef", "gh", "ff", "dd"};

    string s = get_string("Enter num: ");

    for (int i = 0; i < 6; i++)
    {
        if (strcmp(letters[i], s) == 0)
        {
            printf("Found string\n");
            return 0;
        }
    }
    printf("Not found\n");
    return 1;
}