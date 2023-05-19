#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>

int main(void)
{
    /* char *s = "###";
    printf("%s\n", s);
    printf("%s\n", s+1);
    printf("%s\n", s+2); */

    /* char *s = get_string("s: ");
    char *t = get_string("t: "); */

    char *a = get_string("Enter string: ");
    if (a == NULL)
    {
        return 1;
    }

    char *b = malloc(strlen(a) + 1);
    if (b == NULL)
    {
        return 1;
    }

    strcpy(b, a);

    if (strlen(b) > 1)
    {
        b[0] = toupper(b[0]);
    }


    printf("a: %s\n", a);
    printf("b: %s\n", b);

    free(b);
    
    return 0;
}