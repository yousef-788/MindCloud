#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int n;
    cin >> n;

    int arr[n][n];
    int first = 0;
    int second = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            do
            {
                cin >> arr[i][j];
            } while (arr[i][j] < -100 || arr[i][j] > 100);
        }
    }

    for (int i = 0; i < n; i++)
        first += arr[i][i];

    for (int i = 0; i < n; i++)
    {
        second += arr[i][n - 1 - i];
    }

    int sub = abs(first - second);
    cout << sub << endl;
    return 0;
}