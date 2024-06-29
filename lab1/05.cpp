#include<iostream>

int main(){

    int dividend,divisor,quotient,remainder;
    std::cout << "Enter divident: ";
    std::cin >> dividend;
    std::cout << "Enter divisor: ";
    std::cin >> divisor;
    quotient = dividend/divisor;
    remainder = dividend % divisor;

    std::cout << "Quotient = " << quotient << std::endl;
    std::cout << "Remainder = " << remainder << std::endl;
    system("pause");
    return 0;

}