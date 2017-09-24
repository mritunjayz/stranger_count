#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    double t,c,d,i,f;
    scanf("%lf",&t);
    c=1;d=3;
    for(i=1;i<=t;i++){
        if(t>=c&&t<=d){
            break;
        }
        c=d+1;
        d=d*2+3;
    }
   t=t-c;
    f=c+2-t;
   printf("%.0lf",f);
    return 0;
}
