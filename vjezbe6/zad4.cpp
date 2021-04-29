#include <iostream>

using namespace std;

int main()
{
    int a1, b1, c1, a2, b2, c2;
    cout << "Unesi drugu jednadzbu" << endl;
    cout << "Unesi vrijednost za a1" << endl;
    cin >> a1;
    cout << "Unesi vrijednost za b1" << endl;
    cin >> b1;
    cout << "Unesi vrijednost za c1" << endl;
    cin >> c1;
    cout << "Unesi drugu jednadzbu." << endl;
    cout << "Unesi vrijednost za a2" << endl;
    cin >> a2;
    cout << "Unesi vrijednost za b2" << endl;
    cin >> b2;
    cout << "Unesi vrijednost za c2" << endl;
    cin >> c2;
    cout << "Sustav:" << endl;
    cout << a1 << "x+" << b1 << "y=" << c1 << endl;
    cout << a2 << "x+" << b2 << "y=" << c2 << endl;

if ((a1 * b2) - (b1 * a2) == 0){
    cout << "nema rjesenja" << endl;
}
else{
    rjes_x = ((c1*b2) - (b1*c2))/((a1*b2)-(b1*a2));
    rjes_y = ((a1*c2) - (c1*a2)) / ((a1*b2) - (b1*a2));
    cout << "x=" << rjes_x << " y=" << rjes_y << endl;
}

    return 0;
}

#to je bio prvi pokusaj, ne ide bas ali neka ostane ovdje za primjer kada budem ucila


float sustav(float a1,float b1, float c1,float a2,float b2, float c2)
{
    float x; 
    x = (b1*c2-b2*c1)/(b1*a2-a1*b2);
    float y;
    y = (c1-a1*x)/b1;
   std::cout << "x je:" << x << "y je:" << y << std::endl;
    
}

int main()
{
    sustav(4,6,2,3,8,7);
     return 0;
