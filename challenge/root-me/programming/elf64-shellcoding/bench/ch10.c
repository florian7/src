#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/mman.h>

#define SHELLCODE_SIZE 50

#define DO_PRINT(...) do { printf(__VA_ARGS__); fflush(stdout); } while(0)


int main(void) {
  int len;
  void (*shellcode)(void);

  DO_PRINT("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n");
  DO_PRINT("~~~ Shellcode eXecutor 1.0 ~~~\n");
  DO_PRINT("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n");

  DO_PRINT("[+] Give me a shellcode ! (Max len : %d bytes) :)\n", SHELLCODE_SIZE);

  shellcode = mmap(NULL, 0x1000, PROT_READ | PROT_WRITE | PROT_EXEC, MAP_PRIVATE | MAP_ANON, -1, 0);

  if(shellcode == MAP_FAILED) {
    perror("[-] mmap ");
    exit(EXIT_FAILURE);
  }

  len = read(0, shellcode, SHELLCODE_SIZE);

  DO_PRINT("[+] Executing shellcode of length %d...\n", len);
  shellcode();
  DO_PRINT("[+] Shellcode executed !\n");

  return EXIT_SUCCESS;
}

