#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define COLUMNS 3
#define ROWS 3
#define WIN 3

    char field [ROWS][COLUMNS] = {
        {' ',' ',' '},
        {' ',' ',' '},
        {' ',' ',' '}
    };

    int fieldElements = 0; // How many 'x' and 'o' does field contain?

void printField() {
    int i,j;
    for (i = 0; i < ROWS; i++) {
        for (j = 0; j < COLUMNS; j++){
            printf("|");
            printf("%c", field[i][j]);
        }
        printf("|\n");
        printf("-------\n");
    }
    printf("***********************\n");
}

void playerMove(char playerSign) {
    bool validPosition = false;
    int column, row;
    do {
        printf("Spalte: ");
        scanf("%d", &column);
        printf("Reihe: ", &row);
        scanf("%d", &row);
        // computer starts counting with 0
        column--;
        row--;
        if (field[row][column] == ' '){ // field is empty
            validPosition = true;
        } else {
            printf("Position bereits belegt oder nicht-existent!Trottel...\n");
        }
    } while (!validPosition);
    
    field[row][column] = playerSign;
    fieldElements++;
}

void checkCounters(int counterX, int counterO) {
    if (counterX == WIN) {
        printf("Spieler X hat gewonnen!");
        exit(0);
        }
    if (counterO == WIN) {
        printf("Spieler O hat gewonnen!");
        exit(0);
    }
}

void checkIfGameOver(){
    /***********check rows***********/
    int i, j, counterO, counterX;
    counterO = counterX = 0;
    for (i = 0; i < ROWS; i++) {
        for (j = 0; j < COLUMNS; j++) {
            if (field[i][j] == 'x'){
                counterX++;
            }
            if (field[i][j] == 'o') {
                counterO++;
            }
        }
        checkCounters(counterX, counterO);
        counterX = counterO = 0;
    }
    /**********check columns**********/
    for (i = 0; i < COLUMNS; i++) {
        for (j = 0; j < ROWS; j++) {
            if (field[j][i] == 'x') {
                counterX++;
            }
            if (field[j][i] == 'o') {
                counterO++;
            }
        }
        checkCounters(counterX, counterO);
        counterX = counterO = 0;
    }
    /**********diagonal 1**********/ 
    for (i = 0; i < ROWS; i++) {
        if (field[i][i] == 'x') {
            counterX ++;
        }
        if (field[i][i] == 'o') {
            counterO ++;
        }
    }
    checkCounters(counterX, counterO);
    counterX = counterO = 0;
    /**********diagonal 2**********/ 
    i = ROWS - 1;
    j = 0;
    while (i >= 0 && j < COLUMNS) {
        if (field [i][j] == 'x') {
            counterX++;
        }
        if (field[i][j] == 'o') {
            counterO++;
        }
        i--;
        j++;
    }
    checkCounters(counterX, counterO);
    // field is full...
    if (fieldElements == (ROWS * COLUMNS)) {
        printf("UNENTSCHIEDEN");
        exit(0);
    }
}

int main() {
    printField();
    char turn = 'x';
    int round = 1;
    while(true) {
        printf("**RUNDE %d**\n", round);
        printf("Spieler %c ist an der Reihe!\n", turn);
        playerMove(turn);
        // switch turn
        if (turn == 'x'){
            turn = 'o';
        } else {
            turn = 'x';
        }
        printField();
        checkIfGameOver();
        round++;
    }
}