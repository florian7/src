CC = gcc
CFLAGS  = -Wall -m64
LDFLAGS = 

RM = rm -f

all: ch10 p-sandbox fixperms


ch10:  ch10.o
	$(CC) $(CFLAGS) -o $@ $<

p-sandbox:  p-sandbox.o
	$(CC) $(CFLAGS) -o $@ $<

%.o:%.c
	$(CC) $(CFLAGS) -c $<

fixperms:
	chown root:root ch10* p-sandbox*
clean:
	$(RM) ch10 p-sandbox *.o *~

