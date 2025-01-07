#include "stdio.h"
#include "stdlib.h"

#define MAX_KEYS 3


struct BPlusTreeNode {
  int keys[MAX_KEYS];
  struct BPlusTreeNode* children[MAX_KEYS + 1];
  int is_leaf;
  int num_key;
  struct BPlusTreeNode* next;
};

int main(int argc, char *argv[]) {
  struct BPlusTreeNode node;

  for (int i = 0; i < MAX_KEYS + 1; i++) {
    node.children[i] = NULL;
  }

  for (int i = 0; i < MAX_KEYS + 1; i++) {
    printf("Child %d pointer: %p\n", i, (void*)node.children[i]);
  }



  return 0;
}





