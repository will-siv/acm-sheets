#ifndef __SCREEN_H__
#define __SCREEN_H__

#include <stdio.h>
#include <string.h>
#include <json-c/json.h>

#define CHAR_WIDTH 106
#define CHAR_HEIGHT 46

#define POS(X,Y) CHAR_WIDTH*Y + X

char buff[CHAR_WIDTH * CHAR_HEIGHT];

/* vertical lines at char 26, 53, 79 */
/* names at char 4, 57 */
/* maximum classes char width is 110 */

/* rewrites all characters in buffer to screen */
void refresh_screen() {
  int i, j;
  for (i = 0; i < CHAR_HEIGHT; i++) {
    for (j = 0; j < CHAR_WIDTH; j++) {
      putchar(buff[i*CHAR_WIDTH + j]);
    }
    putchar('\n');
  }
}

void clear_screen() {
  int i, j;
  for (i = 0; i < CHAR_HEIGHT; i++) {
    for (j = 0; j < CHAR_WIDTH; j++) {
      buff[i*CHAR_WIDTH + j] = ' ';
    }
  }
  printf("\033[H");
}

void paste(int x, int y, const char *str) {
  strcpy(buff + POS(x,y), str);
}

void linebreak(int n) {
  int i;
  char linebuff[CHAR_WIDTH];

  for (i = 0; i < CHAR_WIDTH - 1; i++) {
    linebuff[i] = '=';
  }

  strcpy(buff + CHAR_WIDTH*n, linebuff);
}

void vert_line(int x, int y, const char *str) {
  for (; y < CHAR_HEIGHT; y++) {
    paste(x, y, str);
  }
}

void template_cover() {
  vert_line(26, 7, "|");
  vert_line(53, 4, "|");
  vert_line(79, 7, "|");

  linebreak(3);
  linebreak(6);

  paste(38, 2, "YWCC Tutoring, Powered by ACM");
  paste(7, 4, "Join the ACM Discord! njit.gg/acm");
  paste(61, 4, "Join the YWCC Discord! njit.gg/ywcc");
  paste(5, 5, "Something wrong? Ask in #tutoring-questions");
  paste(57, 5, "Talk about individual CS/IT/IS/YWCC classes");
}

void update_name_class(json_object *root) {
  int temp_n = json_object_array_length(root);
  json_object *temp, *name, *class;
  template_cover();
  for (int i = 0; i < temp_n; i++) {
    temp = json_object_array_get_idx(root, i);
    name = json_object_object_get(temp, "name");
    class = json_object_object_get(temp, "classes");

  }
}

void update_name_time(json_object *root) {
  template_cover();
int temp_n = json_object_array_length(root);
  json_object *temp, *name, *secs;
  template_cover();
  for (int i = 0; i < temp_n; i++) {
    temp = json_object_array_get_idx(root, i);
    name = json_object_object_get(temp, "name");
    secs = json_object_object_get(temp, "sections");
    
  }
}

void update_class_date_time(json_object *root) {

}

void update_name_class_time_day(json_object *root) {

}

#endif