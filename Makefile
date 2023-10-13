# extremely barebones - idk if i even wanna use C for this
CFLAGS += $(shell pkg-config --cflags json-c)
LDFLAGS += $(shell pkg-config --libs json-c)

main:
	gcc src/screen/*.c