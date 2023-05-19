#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

bool only_digits(string key);
bool only_digits(string key);
char rotate(char c, int n);

int main(int argc, string argv[])
{
    if (!argv[1])
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else if (argc > 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else if(!only_digits(argv[1]))
    {
        printf("Value must be between 0 and 9\n");
        return 1;
    }

    int key = atoi(argv[1]);
    string plain = get_string("plaintext: ");

    printf("ciphertext: ");
    for (int i = 0; i < strlen(plain); i++)
    {
        printf("%c", (char)rotate(plain[i], key));
    }
    printf("\n");
}

bool only_digits(string key)
{
    for (int i = 0; i < strlen(key); i++)
    {
        if (!isdigit(key[i]))
        {
            return false;
        }
    }
    return true;
}

char rotate(char c, int n)
{
    if (isalpha(c) && isupper(c))
    {
        if ((int) c == 90)
        {
            return (int) c - 26 + n;
        }
        else if ((int) c + n > 90)
        {
            return (int) c - 26 + n;
        }
        return (int) c + n;
    }
    else if (isalpha(c) && islower(c))
    {
        if ((int) c == 122)
        {
            return (int) c - 26 + n;
        }
        else if ((int) c + n > 122)
        {
            return (int) c - 26 + n;
        }
        return (int) c + n;
    }
    else
    {
        return c;
    }
}