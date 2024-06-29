#include<iostream>
#include<vector>
#include<thread>

void thread_function(){
    std::cout << "Thread function running!!!" << std::endl;
}


int main1(){
    // for (int i = 0; i < 5; i++)
    //     std::thread my_thread(thread_function);

    std::thread my_thread(thread_function);

    std::cout << "thread ID: " << my_thread.get_id() << "\n hardware concurrency: " << my_thread.hardware_concurrency() << std::endl;

    my_thread.join();

    return 0;

}

int main(){

    std::vector<std::thread> threads(5);
    std::thread my_thread;
    int i = 0;

    for (i = 0; i < 5; i++){
        threads[i] = std::thread(thread_function);
        std::cout <<"address of " << i << "th element is:" << &threads[i] << std::endl;
    }

    std::cout << "address of threads vector" << &threads << std::endl;


    for (i = 0; i < 5; i++)
        std::cout << "thread ID: " << threads[i].get_id() << "\nhardware concurrency: " << threads[i].hardware_concurrency() << std::endl;

    for (i = 0; i < 5; i++)
        threads[i].join();

    return 0;

}


