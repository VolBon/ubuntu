#include "encrypt.h"

void encrypt(char *message)
{
char c;
while (*message) {
*message = *message ^ 30;
message++;
}

}

//encrypt.o: encrypt.c encrypt.h msg_hider.c
//	gcc -c encrypt.c msg_hider.c
//msg_hider.o: msg_hider.c
//	gcc -c msg_hider.c
//tree: encrypt.o msg_hider.o
//	gcc encrypt.o msg_hider.o -o tree