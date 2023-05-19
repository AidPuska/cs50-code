#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

// name functions before main function
int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    string text = get_string("Text: ");

    // call functions
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);

    // calculate grade
    float L = (float)letters / words * 100;
    float S = (float)sentences / words * 100;
    int index = round(0.0588 * L - 0.296 * S - 15.8);
    // check if is lower than 1 or bigger than 16
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index >= 1 && index <= 16)
    {
        printf("Grade %i\n", index);
    }
    else
    {
        printf("Grade 16+\n");
    }
}

int count_letters(string text)
{
    // count letters
    int letters = 0;
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        // check if it's a letter
        if (text[i] >= 'A' && text[i] <= 'Z')
        {
            letters++;
        }
        else if (text[i] >= 'a' && text[i] <= 'z')
        {
            letters++;
        }
    }
    return letters;
}

int count_words(string text)
{
    // counts words
    int words = 0;
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        // check if there is blank space
        if (text[i + 1] == ' ')
        {
            words++;
        }
        else
        {
            words += 0;
        }
    }
    return words + 1;
}

int count_sentences(string text)
{
    // count sentences
    int sentences = 0;
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        // check if there is end of sentence
        if (text[i + 1] == '.' || text[i + 1] == '!' || text[i + 1] == '?')
        {
            sentences++;
        }
        else
        {
            sentences += 0;
        }
    }
    return sentences;
}