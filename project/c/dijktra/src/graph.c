#include <stdio.h>
#include <stdlib.h>
#include "graph.h"


struct vertex {
	size_t label_length;
	char * label;
	size_t neighbours_nb;
	edge * neighbours;
};

struct edge {
	size_t weight;
	vertex * vertices [2];
};

struct graph {
	size_t vertices_nb;
	vertex * vertices;
	size_t edges_nb;
	edge * edges;
};

static int parse_relation(graph * graph, size_t length, char * string)
{
	size_t i = 0;
	if (string[i])
}

int graph_create_from_string(graph * graph, size_t length, char * string)
{
	int ret;
	size_t i;

	for (i = 0; i < length; i++) {

		ret = parse_relation(graph, length - i, string + i);
		if (ret != 0)
			return ret;

		i += ret;

		if (i < length && string[i] != ',') {
			printf("Expected ',' at offset %d\n", i);
			return -1;
		}

		i++;
	} 
} 

