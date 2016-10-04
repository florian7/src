ifdef VERBOSE
	Q =
	E = @true 
else
	Q = @
	E = @echo 
endif


CFILES := $(shell find src -mindepth 1 -maxdepth 4 -name "*.c")
CXXFILES := $(shell find src -mindepth 1 -maxdepth 4 -name "*.cpp")

INFILES := $(CFILES) $(CXXFILES)

OBJFILES := $(CXXFILES:src/%.cpp=%) $(CFILES:src/%.c=%)
DEPFILES := $(CXXFILES:src/%.cpp=%) $(CFILES:src/%.c=%)
OFILES := $(OBJFILES:%=obj/%.o)

BINFILE = simple-kernel


COMMONFLAGS = -Wall -Wextra -pedantic
LDFLAGS = -lm -lpthread -lX11

DEBUG=yes
ifdef DEBUG
	COMMONFLAGS := $(COMMONFLAGS) -g
endif

CFLAGS = $(COMMONFLAGS) --std=c99
CXXFLAGS = $(COMMONFLAGS) --std=c++0x


CC = gcc
CXX = g++


.PHONY: clean all depend
.SUFFIXES:


all: $(BINFILE)

obj/%.o: src/%.c
	$(E)C-compiling $<
	$(Q)if [ ! -d `dirname $@` ]; then mkdir -p `dirname $@`; fi
	$(Q)$(CC) -o $@ -c $< $(CFLAGS)

obj/%.o: src/%.cpp
	$(E)C++-compiling $<
	$(Q)if [ ! -d `dirname $@` ]; then mkdir -p `dirname $@`; fi
	$(Q)$(CXX) -o $@ -c $< $(CXXFLAGS)

$(BINFILE): $(OFILES)
	$(E)Linking $@
	$(Q)$(CXX) -o $@ $(OFILES) $(LDFLAGS)

clean:
	$(E)Removing files
	$(Q)rm -f $(BINFILE) obj/* Makefile.dep
