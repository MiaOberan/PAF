#include <iostream>
#include <cmath>
void  tocka_na_kruznici(int x1,int y1,int x2,int y2,int r)
{
    float udalj;
    udalj = pow((x1-x2),2) + pow((y1-y2),2);
    float d;
    d = sqrt(udalj);
    float epsilon = 0.01;
    if (d<r){
        std::cout << "Točka je unutar kružnice" << std::endl;
    }
    else if ( r-epsilon < d < r+epsilon){
        std::cout << "Točka je na kružnici" << std::endl;
    }
    else{
        std::cout << "Točka je van kružnice" << std::endl;
    }
}
int main(){
    tocka_na_kruznici(2,4,6,3,1);
    return 0;
}
