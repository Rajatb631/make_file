#include<iostream.h>
#include<stdlib.h>
#include<fstream.h>
int main(){
	fstream fil;
	fil.open("data.txt", ios::out);
	for(int i=0; i<50;i++){

		fil<<i+1<<","<<rand()%100<<","<<rand()%15;
	}
	fil.close();
	return 0;

}
