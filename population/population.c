#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int start_size;
    do
    {
        start_size = get_int("Enter start size of population: ");
    }
    while (start_size < 9);
    // TODO: Prompt for end size
    int end_size;
    do
    {
        end_size = get_int("Enter end size of population: ");
    }
    while (end_size < start_size);

    if (start_size == end_size)
    {
        printf("Years: 0\n");
    }
    else
    {

    // TODO: Calculate number of years until we reach threshold
    int count = 0;
    int per_year;
    do
    {
        per_year = (start_size + start_size / 3 - start_size / 4) - start_size;
        start_size += per_year;
        count ++;
    }
    while (start_size < end_size);

    // TODO: Print number of years
    printf("Years: %i\n", count);
    }
}
