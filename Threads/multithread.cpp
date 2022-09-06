// CPP program to demonstrate multithreading
// using three different callables.
#include <iostream>
#include <thread>
using namespace std;


void foo(int x) {
    for (int i = 0; i < x; i++) {
        cout << "Thread usando ponteiro de função\n";
    }
}

class thread_obj {
public:
    void operator()(int x) {
        for (int i = 0; i < x; i++)
            cout << "Thread usando método invocado do objeto\n";
    }
};

int main() {
    cout << "Threads 1, 2 e 3 operando independentemente!" << endl;

    // ponteiro de função
    thread th1(foo, 3);

    // chamando um método de um objeto
    thread th2(thread_obj(), 3);

    // definindo expressão lambda
    auto f = [](int x) {
        for (int i = 0; i < x; i++)
            cout << "Thread usando expressão lambda\n";
    };

    // usando expressão lambda
    thread th3(f, 3);

    // esperando thread 1
    th1.join();
    // esperando thread 2
    th2.join();
    // esperando thread 3
    th3.join();

    return 0;
}