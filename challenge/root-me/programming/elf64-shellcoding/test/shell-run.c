#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/mman.h>
#include <fcntl.h>

#define SHELLCODE_SIZE 120

#define DO_PRINT(...) do { printf(__VA_ARGS__); fflush(stdout); } while(0)

int main(int argc, char * argv []) {
	int len, fd;
	void (*shellcode)(void);
	char code [SHELLCODE_SIZE];

	DO_PRINT("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n");
	DO_PRINT("~~~ Shellcode eXecutor 1.0 ~~~\n");
	DO_PRINT("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n");

	if (argc < 2) {
		DO_PRINT("[-] Usage: %s <file>\n", argv[0]);
		return EXIT_FAILURE;
	}

	DO_PRINT("[+] Openinig file %s)\n", argv[1]);
	fd = open(argv[1], O_RDONLY);

	shellcode = mmap(NULL, 0x1000, PROT_READ | PROT_WRITE | PROT_EXEC, MAP_PRIVATE | MAP_ANON, fd, 0);

	if(shellcode == MAP_FAILED) {
		perror("[-] mmap ");
		exit(EXIT_FAILURE);
	}

	len = read(fd, shellcode, SHELLCODE_SIZE);
	close(fd);

	write(STDOUT_FILENO, shellcode, len);


	DO_PRINT("[+] Executing shellcode of length %d...\n", len);
	shellcode();
	DO_PRINT("[+] Shellcode executed !\n");

	return EXIT_SUCCESS;
}

