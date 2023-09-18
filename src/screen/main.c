/*
MAIN.C
controller function - stores important values and calls appropriate functions based on order of control
*/

#include <json-c/json.h>
#include <unistd.h>

#include "screen.h"

int main() {
  printf("Starting Tutoring Display....\n");
  usleep(3);

  while (1) {
    update_name_class();
    sleep(30);
    update_name_time();
    sleep(30);
  }
}