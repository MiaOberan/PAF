#include <iostream>
#include <cmath>
using namespace std;

void jednadzba_pravca(double x1, double y1, double x2, double y2);
void jednadzba_pravca(double x1, double y1, double x2, double y2)
{
    double k;
    k=(y2-y1)/(x2-x1);
    cout<<"Jednazdba pravca je: y-"<<y1<<"="<<k<<"(x-"<<x1<<")"<<endl;
}
int main()
{
    jednadzba_pravca(4.0,5.0,7.0,6.0);
    return 0;
}
