#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

void sortMatrix(vector<vector<int>>& matrix) {
    int column, row, i, j, k;
    vector<int> arr;
    
    column = matrix.size();
    if (column == 0) return;
    
    row = matrix[0].size();
    arr.assign(column * row, 0);
    
    for (i = 0; i < column; ++i) {
        k = i * row;
        for (j = 0; j < row; ++j) {
            arr[k + j] = matrix[i][j];
        }
    }
    
    sort(arr.begin(), arr.end());
    
    for (j = 0; j < row; ++j) {
        k = j * column;
        for (i = 0; i < column; ++i) {
            matrix[i][j] = arr[k + i];
        }
    }
}

int main() {
    std::vector<std::vector<int>> matrix = {
        {3, 2, 1},
        {5, 4, 6},
        {9, 7, 11},
    };
    
    sortMatrix(matrix);
    
    for (auto row : matrix) {
        for (auto col: row) {
            std::cout << col << " ";
        }
        
        std::cout << std::endl;
    }
    
    return 0;
}