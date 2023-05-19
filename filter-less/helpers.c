#include "helpers.h"
#include <stdio.h>
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int avgc;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            avgc = (image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0;
            image[i][j].rgbtRed = image[i][j].rgbtBlue = image[i][j].rgbtGreen = round(avgc);
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    /* printf("%i\n", width);
    for (int i = 0; i < height; i++)
    {
        int n = 0;
        printf("n before: %i\n", n);
        for (int j = width; j > 0; j--)
        {
            image[i][n] = image[i][j];
            n++;
        }
        n = 0;
        printf("n after: %i\n", n);
    } */
    for (int i = 0; i < height; i++)
    {
        int num = 0;
        for (int j = width - 1; j >= 0; j--)
        {
            image[i][j] = image[i][num];
            num++;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
