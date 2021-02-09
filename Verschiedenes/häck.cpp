#include <windows.h>

int main(void) {
    int x,y, counter;
    x = 5;
    y = 5;
    while(true) {
        counter = 0;
        while (counter < 150) {
          // bisschen die Maus bewegen...
          x += 5;
          y += 5;
          SetCursorPos(x,y);
          Sleep(50);
          counter ++;
        }
        // Cursor an ursprüngliche Position...
        x = 5;
        y = 5;
        SetCursorPos(x,y);
        Sleep(10000);
    }
    return 0;
}
