#include <iostream>
#include <algorithm>
#include <vector>

int main() {
    std::vector<int> arr =  {1, 2, 3, 4, 5, 6, 7};
    auto g = *(std::max_element(arr.begin(), arr.begin() + 3));
    std::cout << g << std::endl;
}