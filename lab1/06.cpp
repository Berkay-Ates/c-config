#include<iostream>


int main(){
    float R, Area, Circumference;
    std::cout << "\t\tC++ program to calculate Area and Circumference of circle." <<std::endl;

    std::cout << "Please enter the Radius of Circle: ";
    std::cin >> R;

    if (R>0){
        Area = 3.14 * R * R;
        Circumference = 2 * 3.14 * R;
        std::cout << "Ares of Circle is " << Area << ";" << std::endl;
        std::cout << "Circumference of Circle is " << Circumference << ";" << std::endl;   
    }
    else {
       std::cout<<"Negative numbers cannot be applied !!!" << std::endl;
    }

    system("pause");
    return 0;

}