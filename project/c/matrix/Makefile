ifdef VERBOSE
	Q =
	E = @true 
else
	Q = @
	E = @echo 
endif
	

CFILES := $(shell find src -mindepth 1 -maxdepth 4 -name "*.c")

INFILES := $(CFILES)

OBJFILES := $(CFILES:src/%.c=%)
DEPFILES := $(CFILES:src/%.c=%)
OFILES := $(OBJFILES:%=obj/%.o)

BINFILE = matrix


ifdef DEBUG
	COMMONFLAGS := $(COMMONFLAGS) -g
endif

CC = gcc

COMMONFLAGS = -Wall -Wextra -pedantic
LDFLAGS =

CFLAGS = $(COMMONFLAGS) --std=c99
DEPDIR = deps


all: $(BINFILE)

.PHONY: clean all depend
.SUFFIXES:

obj/%.o: src/%.c
	$(E)C-compiling $<
	$(Q)if [ ! -d `dirname $@` ]; then mkdir -p `dirname $@`; fi
	$(Q)$(CC) -o $@ -c $< $(CFLAGS)

Makefile.dep: $(CFILES)
	$(E)Depend
	$(Q)for i in $(^); do $(CC) $(CFLAGS) -MM "$${i}" -MT obj/`basename $${i%.*}`.o; done > $@

	
$(BINFILE): $(OFILES)
	$(E)Linking $@
	$(Q)$(CC) -o $@ $(OFILES) $(LDFLAGS)
clean:
	$(E)Removing files
	$(Q)rm -f $(BINFILE) obj/* Makefile.dep
