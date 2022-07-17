#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <float.h>

int main(int argc, char** argv) {
    printf("CHAR_BIT    :   %d\n", CHAR_BIT);
    printf("CHAR_MAX    :   %d\n", CHAR_MAX);
    printf("CHAR_MIN    :   %d\n", CHAR_MIN);
    printf("INT_MAX     :   %d\n", INT_MAX);
    printf("INT_MIN     :   %d\n", INT_MIN);
    printf("LONG_MAX    :   %ld\n", (long) LONG_MAX);
    printf("LONG_MIN    :   %ld\n", (long) LONG_MIN);
    printf("SCHAR_MAX   :   %d\n", SCHAR_MAX);
    printf("SCHAR_MIN   :   %d\n", SCHAR_MIN);
    printf("SHRT_MAX    :   %d\n", SHRT_MAX);
    printf("SHRT_MIN    :   %d\n", SHRT_MIN);
    printf("UCHAR_MAX   :   %d\n", UCHAR_MAX);
    printf("UINT_MAX    :   %u\n", (unsigned int) UINT_MAX);
    printf("ULONG_MAX   :   %lu\n", (unsigned long) ULONG_MAX);
    printf("USHRT_MAX   :   %d\n", (unsigned short) USHRT_MAX);
    printf("\n");
    printf("Storage size for float : %d \n", sizeof(float));
    printf("FLT_MAX                : %g\n", (float) FLT_MAX);
    printf("FLT_MIN                : %g\n", (float) FLT_MIN);
    printf("-FLT_MAX               : %g\n", (float) -FLT_MAX);
    printf("-FLT_MIN               : %g\n", (float) -FLT_MIN);
    printf("DBL_MAX                : %g\n", (double) DBL_MAX);
    printf("DBL_MIN                : %g\n", (double) DBL_MIN);
    printf("-DBL_MAX               : %g\n", (double) -DBL_MAX);
    printf("Precision value        : %d\n", FLT_DIG );

    int test;
    printf("TEST %d\n", test);

  

    float test2 = 12.234234999;
    printf("1 : %f | 2 : %g\n", test2, test2);

    int maVariable = 42;
    printf("Voici la valeur de ma variable : %d\n", maVariable);

    int monInt = 42;
    float monFloat = 42.424242;
    char monChar = 'c';

    printf("monInt : %d\nmonFloat : %f\nmonChar : %c\n", monInt, monFloat, monChar);

    int premierNbr = 20;
    int deuxiemeNbr = 22;

    printf("Somme du premier et du deuxième nombre : %d", premierNbr + deuxiemeNbr);

    return 0;
}