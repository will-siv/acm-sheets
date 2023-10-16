/*
MAIN.C
controller function - stores important values and calls appropriate functions based on order of control
*/

#include <json-c/json.h>
#include <unistd.h>
#include <stdio.h>

#include "screen.h"

int main(int argc, char **argv) {
  json_object *root;
  if (argc != 2) {
    perror("Usage: ./program {json}");
  }
  root = json_object_from_file(argv[1]);
  printf("Starting Tutoring Display....\n");
  sleep(3);
  printf("\033[H\033[J");


  while (1) {
    clear_screen();
    update_name_class(root);
    refresh_screen();
    sleep(30);
    update_name_time(root);
    refresh_screen();
    sleep(30);
  }
}