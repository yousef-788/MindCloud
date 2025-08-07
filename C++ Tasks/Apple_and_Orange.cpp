#include <iostream>
using namespace std;

int main()
{
    int s, t, a, b, m, n;
    do
    {
        do
        {
            cin >> s >> t;
        } while (s < 1 || s > 100000 || t < 1 || t > 100000 || s >= t);
        
        do
        {
            cin >> a >> b;
        } while (a < 1 || a > 100000 || b < 1 || b > 100000 || a >= b);

        do
        {
            cin >> m >> n;
        } while (m < 1 || m > 100000 || n < 1 || n > 100000);
        
    } while (!(a < s && s < t && t < b));

    int arr1[m];
    int arr2[n];

    int appleCount = 0;
    int orangeCount = 0;

    for (int i = 0; i < m; i++)
    {
        do
        {
            cin >> arr1[i];
        } while (arr1[i] < -100000 || arr1[i] > 100000);
    }

    for (int i = 0; i < n; i++)
    {
        do
        {
            cin >> arr2[i];
        } while (arr2[i] < -100000 || arr2[i] > 100000);
    }

    for (int i = 0; i < m; i++)
    {
        int position = a + arr1[i];
        if (position >= s && position <= t)
        {
            appleCount++;
        }
    }

    for (int i = 0; i < n; i++)
    {
        int position = b + arr2[i];
        if (position >= s && position <= t)
        {
            orangeCount++;
        }
    }

    cout << appleCount << endl;
    cout << orangeCount << endl;

    return 0;
}