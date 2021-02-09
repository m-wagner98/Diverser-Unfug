#include <windows.h>

int main(void) {
    int x,y;
    x = 10;
    y = 10;
    while(true) {
        SetCursorPos(x,y);
        x += 1;
        y += 1;
        Sleep(2000);
    }
    return 0;
}