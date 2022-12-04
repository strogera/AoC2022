#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>

#define BSIZE 125
#define MEMSETINTSIZE (BSIZE * 4)
#define PRIO(C) (((C) < 97) ? ((C)-38) : ((C)-96))

int main()
{
    TCHAR *fileName = TEXT("input2.txt");
    HANDLE hFile, hMap;
    LPVOID filePtr;
    LARGE_INTEGER fileSize;

    hFile = CreateFile(fileName, GENERIC_READ, 0, NULL, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, 0);
    GetFileSizeEx(hFile, &fileSize);
    hMap = CreateFileMapping(hFile, NULL, PAGE_READONLY, 0, 0, NULL);
    filePtr = MapViewOfFile(hMap, FILE_MAP_READ, 0, 0, 0);

    char *ptr = (char *)filePtr;
    boolean found[BSIZE] = {0};
    int found2[BSIZE] = {0};
    int sum = 0, i = 0, j = 0, lineStart = 0, z, sum2 = 0;
    for (; i < fileSize.QuadPart; i++)
    {
        if (ptr[i] != '\n')
        {
            found[ptr[i]] = 1;
            continue;
        }
        for (z = 65; z <= 122; z++)
        {
            found2[z] += found[z];
            if (found2[z] == 3)
            {
                sum2 += PRIO(z);
                memset(found2, 0, MEMSETINTSIZE);
                break;
            }
        }
        for (j = lineStart; j < (i + lineStart) >> 1; j++)
        {
            found[ptr[j]] = 0;
        }
        for (; j < i; j++)
        {
            if (found[ptr[j]] == 0)
            {
                sum += PRIO(ptr[j]);
                break;
            }
        }
        memset(found, 0, BSIZE);
        lineStart = i + 1;
    }
    printf("%d\n", sum);
    printf("%d\n", sum2);

    UnmapViewOfFile(filePtr);
    CloseHandle(hMap);
    CloseHandle(hFile);
}