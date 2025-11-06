#include <iostream>
using namespace std;
int main() {
    int limit;
    std::cout << "Enter a limit: ";
    std::cin >> limit;

    int sum_of_multiples = 0;
    for (int i = 0; i < limit; ++i) {
        if (i % 3 == 0 || i % 5 == 0) {
            sum_of_multiples += i;
        }
    }
    std::cout << "Sum of multiples of 3 or 5 below " << limit << " is: " << sum_of_multiples << std::endl;
    return 0;
}