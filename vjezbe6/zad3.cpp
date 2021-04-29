#include <iostream>
#include <math.h>

using namespace std;

const int n = 7;
int lista[n] = {1,3,2,4,6};

void polje(unsigned a, unsigned b) {
    for(int i = 0; i < n; i++) {
        if (lista[i] >= a && lista[i] <= b) {
            cout << lista[i] << " ";
        }
        else {
            continue;
        } } 
        cout << endl;
        }   

int main() {

    list<int> lista;
    int a = 1;
    int b = 7;
    lista.push_back(a);
    lista.push_back(2);
    lista.push_back(4);
    lista.push_back(3);
    lista.push_back(6);
    lista.push_back(b);

    cout << "\nPrvotna lista je : ";
    polje(lista);

    cout << "\nLista poslije mijenjanjaa redoslijeda clanova: ";
    lista.reverse();
    polje(lista);

    cout << "\nLista nakon zamjene clanova: ";
    std::swap(a, b);
    polje(lista);

    cout << "\nLista nakon sortiranja: ";
    lista.sort();
    polje(lista);

    return 0;
