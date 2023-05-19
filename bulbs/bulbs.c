#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);
void reverse_array(int arr[], int size);

int main(void)
{
    // TODO
    string text = get_string("Message: ");

    int bin[strlen(text) * 8];

    int count = 0;

    for (int i = 0, len = strlen(text); i < len; i++)
    {
        //printf("Starting");
        int rest = text[i];
        for (int j = 0; j < 8; j++)
        {
            bin[count] = rest % 2;
            if (count > 0)
            {
                reverse_array(bin, count);
            }
            print_bulb(bin[count]);
            rest = round(rest / 2);
            count++;
        }
        for (int low = 0, high = count - 1; low < high; low++, high--)
        {
            int temp = arr[low];
            arr[low] = arr[high];
            arr[high] = temp;
        }
        printf("\n");
    }
}

void reverse_array(int arr[], int n)
{
    for (int low = 0, high = n - 1; low < high; low++, high--)
    {
        int temp = arr[low];
        arr[low] = arr[high];
        arr[high] = temp;
    }
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
