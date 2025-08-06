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
    cin >> n;
    int arr[100];
    for (int i = 0; i < n; i++)
    {

        cin >> arr[i];
    }

    cocktail(arr, n);
    return 0;
}