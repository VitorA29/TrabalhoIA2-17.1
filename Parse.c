#include <string.h>
#include <stdlib.h>
#include <stdio.h>

int main(void){
	FILE *fin=fopen("NELL.08m.666.SSFeedback.csv", "rt"), *fout;
	if(!fin)exit(1);
	fout=fopen("parse.txt", "wt");
	if(!fout){
		fclose(fin);
		exit(1);
	}
	int col=1, aspas=0, index=0, size=1;
	char ch;
	char *str1, *str2, *str3;
	str1=NULL;
	str2=NULL;
	str3=NULL;
	while(((ch=fgetc(fin))!=EOF) && ch!='\n');
	while(((ch=fgetc(fin))!=EOF)){
		if(ch=='\n'){
			fprintf(fout, "(%d,%d,%d);(%s,%s,%s)\n", 
				strlen(str1), strlen(str2), strlen(str3),
				str1, str2, str3);
			col=1;
			size=1;
			free(str1);
			free(str2);
			free(str3);
			str1=NULL;
			str2=NULL;
			str3=NULL;
			continue;
		}
		if(ch=='"'){
			aspas=!aspas;
			continue;
		}
		if(ch=='\t'){
			col++;
			size=1;
			continue;
		}
		switch(col){
			case 1:
				size++;
				str1=(char*)realloc(str1, size*sizeof(char));
				str1[size-2]=ch;
				str1[size-1]='\0';
				break;
			case 2:
				size++;
				str2=(char*)realloc(str2, size*sizeof(char));
				str2[size-2]=ch;
				str2[size-1]='\0';
				break;
			case 4:
				size++;
				str3=(char*)realloc(str3, size*sizeof(char));
				str3[size-2]=ch;
				str3[size-1]='\0';
				break;
			default:
				break;
		}
	}
	if(str1)free(str1);
	if(str2)free(str2);
	if(str3)free(str3);
	fclose(fin);
	fclose(fout);
	return 0;
}
