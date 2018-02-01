#include "stdio.h"
#include "string.h"
#include "stdlib.h"

void compute_prefix(char* P, int* next){
	int m = strlen(P);
	int i;
	int k = 0;
	for (i = 1; i < m; i = i + 1) {
		while (k > 0 && P[k] != P[i]) {
			k = next[k - 1];
		}
		if (P[k] == P[i]) {
			k = k + 1;
		}
		next[i] = k;
	}
}
void kmp_matcher(char* T, char* P){
	int n = strlen(T);
	int m = strlen(P);
	int i;
	int next[1000];
	for (i = 0; i < 1000; i = i + 1) {
		next[i] = 0;
	}
	compute_prefix(P, next);
	int q = 0;
	int flag = 0;
	int result[1000] = {0};
	for (i = 0; i < n; i += 1) {
		while (q > 0 && P[q] != T[i]) {
			q = next[q - 1];
		}
		if (P[q] == T[i]) {
			q = q + 1;
			if (q == m) {
				result[flag] = i - m + 1;
				q = next[q - 1];
				flag += 1;
			}
		}
	}
	if (flag == 0) {
		printf("False");
	}
	else {
		for (i = 0; i < flag - 1; i = i + 1){
			printf("%d,", result[i]);
		}
		printf("%d", result[i]);
	}
	printf("\n");
}
int main() {
	char T[1000];
	char P[1000];
	gets(T);
	gets(P);
	kmp_matcher(T, P);
	return 0;
}
