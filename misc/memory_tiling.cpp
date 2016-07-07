/* The problem goes as follows:
 Lets say we have a 4x4 matrix which is arranged as follows and needs to be transformed
 1  2  3  4             1   2   5   6
 5  6  7  8     =>      3   4   7   8
 9  10 11 12            9   10  13  14
 13 14 15 16            11  12  15  16
*/

#include <iostream>

using namespace std;

int** allocate_memory(int sizex, int sizey) {
    int **matrix = new int*[sizey];
    for (int i = 0; i < sizey; ++i)
        matrix[i] = new int[sizex];
        
    return matrix;
}

void fill_memory(int** memory, int sizex, int sizey) {
    for (int y = 0; y < sizey; ++y)
        for (int x = 0; x < sizex; ++x)
            memory[y][x] = y * sizex + x;
}

void print_memory(int** memory, int sizex, int sizey) {
    for (int y = 0; y < sizey; ++y) {
        for (int x = 0; x < sizex; ++x)
            cout << memory[y][x] << " ";
        cout << endl;
    }
}

int** transform_memory(
    int **memory,
    int surfaceWidth,
    int surfaceHeight,
    int tileWidth,
    int tileHeight) {
    
    int** new_mem = allocate_memory(surfaceWidth, surfaceHeight);
    
    for (int linearY = 0; linearY < surfaceHeight; ++linearY) {
        for (int linearX = 0; linearX < surfaceWidth; ++linearX) {
            
            int linearOffset = linearX + (linearY * surfaceWidth);
            
            int tileSize = tileWidth * tileHeight;
            
            int widthInTiles = surfaceWidth / tileWidth;
            
            int tileNo = linearOffset / tileSize;
            int locationInTile = linearOffset % tileSize;
            
            int tileOriginY = tileNo / 4;
            int tileOriginX = tileNo % 4;
            
            int tileLinearX = tileOriginX * tileWidth + locationInTile % tileWidth;
            int tileLinearY = tileOriginY * tileWidth + locationInTile / tileHeight;
            
            new_mem[tileLinearY][tileLinearX] = memory[linearY][linearX];
        }
    }
    
    return new_mem;
}

int main() {
    int sizex = 8, sizey = 8, tileWidth = 2, tileHeight = 2;
    int **memory = allocate_memory(sizex, sizey);
    fill_memory(memory, sizex, sizey);
    print_memory(memory, sizex, sizey);
    int **new_mem = transform_memory(memory, sizex, sizey, tileWidth, tileHeight);
    cout << "--------------------------------------------------------" << endl;
    print_memory(new_mem, sizex, sizey);
    return 1;
}