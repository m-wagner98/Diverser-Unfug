#include <windows.h>

int main(void) {
    int x,y, counter;
    x = 5;
    y = 5;
    counter = 0;
    while(true) {
        SetCursorPos(x,y);
        x += 1;
        y += 1;
        if (counter == 50) { // reset (Zahl willkürlich)
          x = 5;
          y = 5;
          counter = 0;
        }
        Sleep(30000);
    }
    return 0;
}
