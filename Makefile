CC=gcc
CLFAGS=-Wall

SRC_FILES=src

main:	
	$(CC) $(CLFAGS) -o /bin/schedule $(SRC_FILES)
test:
	@echo $(MAKE)
