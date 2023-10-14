/*
MAIN.C
controller function - stores important values and calls appropriate functions based on order of control
*/

#include <json-c/json.h>
#include <unistd.h>
#include <stdio.h>

#include "screen.h"

int main() {
  printf("Starting Tutoring Display....\n");
  sleep(3);
  printf("\033[H\033[J");

  while (1) {
    clear_screen();
    update_name_class();
    refresh_screen();
    sleep(30);
    update_name_time();
    refresh_screen();
    sleep(30);
  }
}