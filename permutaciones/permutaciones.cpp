#include <bits/stdc++.h>
using namespace std;
char lista[]={'X','Y','Z'};
char lista2[20];
int length;
bool listaBool[20];

void permutacionesRec(int pos) {
	if (length==pos) {
		puts(lista2);
	}
	else {
		for (int i = 0; i < length; i++) {
			if(!listaBool[i]){
				listaBool[i]=true;
				lista2[pos]=lista[i];
				permutacionesRec(pos+1);
				listaBool[i]=false;
			}
		}
	}
}
int main()
{
	length=strlen(lista);
	permutacionesRec(0);
	return 0;
}