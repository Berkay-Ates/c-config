// complex_example.h

#ifndef COMPLEX_EXAMPLE_H
#define COMPLEX_EXAMPLE_H

struct InnerMostStruct {
    // input parameters
    int innerInput1;
    float innerInput2;

    // output parameters
    double innerOutput1;
};

struct InnerStruct {
    // input parameters
    InnerMostStruct innerMost;
    int input1;

    // output parameters
    float output1;
};

struct OuterStruct {
    // input parameters
    InnerStruct innerStruct;
    int outerInput;

    // output parameters
    float outerOutput;
};

#endif // COMPLEX_EXAMPLE_H
