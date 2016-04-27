#include <iostream>
#include <algorithm>
#include <tuple>
#include <iterator>

using namespace std;

int main() {
    auto triple = std::make_tuple(1, 2, 3);
    int x, y, z;
    std::tie(x, y, z) = triple;
    
    std::cout << std::get<0>(triple) << " ";
    std::cout << std::get<1>(triple) << " ";
    std::cout << std::get<2>(triple) << " ";
    
    std::cout << std::endl;
    
    std::cout << x << " " << y << " " << z << std::endl;
    
    auto mylist = std::vector<int>{1, 2, 3, 4, 5, 6, 7};

    std::vector<int> pow2list = std::vector<int>{};
    std::vector<int> myList = std::vector<int>{};
    std::copy_if(mylist.begin(), mylist.end(), std::back_inserter(pow2list), [](int x){ return x % 2 == 0; });
    std::copy(pow2list.begin(), pow2list.end(), std::ostream_iterator<int>(std::cout, " "));
}