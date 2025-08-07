#include <iostream>
using namespace std;

void cocktail(int *arr, int n)
{
    double sum = 0;
    for (int i = 0; i < n; i++)
    {
        sum += arr[i];
    }
    double percentage = sum / n;

    cout.precision(12);
    cout << fixed << percentage;
}

int main()
{
    int n;
    do
    {
        cin >> n;
    } while (n < 1 || n > 100);

    int arr[100];
    for (int i = 0; i < n; i++)
    {
        do
        {
            cin >> arr[i];
        } while (arr[i] < 0 || arr[i] > 100);
    }

    cocktail(arr, n);
    return 0;
}