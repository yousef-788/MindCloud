#include <iostream>
using namespace std;

int main()
{
    int t;
    do
    {
        cin >> t;
    } while (t < 1 || t > 100);

    while (t--)
    {
        int n;
        do
        {
            cin >> n;
        } while (n < 2 || n > 1000000);
        cout << n / 2 << endl;
    }
    return 0;
}