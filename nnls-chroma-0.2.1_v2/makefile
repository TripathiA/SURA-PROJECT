
PLUGIN_LIBRARY_NAME = nnls-chroma

PLUGIN_CODE_OBJECTS = chromamethods.o NNLSBase.o NNLSChroma.o Chordino.o Tuning.o plugins.o nnls.o viterbi.o

VAMP_SDK_DIR = ../vamp-plugin-sdk

CC=gcc
CXX=g++

OPTFLAGS = -O2 -ffast-math

CFLAGS = $(OPTFLAGS) -I$(VAMP_SDK_DIR) -Wall 
CXXFLAGS = $(OPTFLAGS) -I$(VAMP_SDK_DIR) -I../boost_1_44_0 -Wall

PLUGIN_EXT = .dll
PLUGIN = $(PLUGIN_LIBRARY_NAME)$(PLUGIN_EXT)

LDFLAGS = -shared -fno-exceptions -static-libgcc -Wl,-soname=$(PLUGIN) $(VAMP_SDK_DIR)/libvamp-sdk.a -Wl,--version-script=vamp-plugin.map 


$(PLUGIN): $(PLUGIN_CODE_OBJECTS)
	   $(CXX) -o $@ $^ $(LDFLAGS)

clean:
	del *.o

