#include <iostream>
using namespace std;

int main()
{
    char alpha = 65;
    int n = 5;

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            cout << alpha << " ";
            alpha++;
        }
        cout << endl;
    }
}