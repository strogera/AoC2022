#include <stdio.h>
#include <stdint.h>
#include <string.h>

#define L1 4u
#define L2 14u

inline uint32_t countOnes(uint32_t x)
{
    x = x - ((x >> 1) & 0x55555555);
    x = (x & 0x33333333) + ((x >> 2) & 0x33333333);
    x = (x + (x >> 4)) & 0x0F0F0F0F;
    x = x + (x >> 8);
    x = x + (x >> 16);
    return x & 0x0000003F;
}

int main()
{
    FILE *f = fopen("bigboy.txt", "r");
    char cur[L1];
    memset(&cur, getc(f), sizeof(char) * L1);
    char cur2[L2];
    int i = 1;
    uint32_t x = 0u;
    while (countOnes(x) != L1)
    {
        x = 0u;
        cur[i++ % L1] = getc(f);
        for (int j = 0; j < L1; ++j)
        {
            x |= 1u << cur[j] % 32;
        }
    }
    printf("%d\n", i);
    for (int j = i; (i - j) < L1; --j)
    {
        cur2[j % L2] = cur[i - j];
    }
    while (countOnes(x) != L2)
    {
        x = 0u;
        cur2[i++ % L2] = getc(f);

        for (int j = 0; j < L2; j++)
        {
            x |= 1u << cur2[j] % 32;
        }
    }
    printf("%d\n", i);
    fclose(f);
}