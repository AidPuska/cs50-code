#include <stdio.h>
#include <cs50.h>
#include <string.h>

typedef struct
{
    string name;
    string num;
}
person;

int main(void)
{
    person people[2];

    people[0].name = "Aid";
    people[1].name = "Ais";

    people[0].num = "12345";
    people[1].num = "54321";

    string name = get_string("Enter your name: ");

    for (int i = 0; i < 2; i++)
    {
        if (strcmp(people[i].name, name) == 0)
        {
            printf("Found, %s", people[i].num);
            return 0;
        }
    }
    printf("Not found");
    return 1;
}