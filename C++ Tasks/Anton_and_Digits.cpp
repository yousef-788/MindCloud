#include <iostream>
using namespace std;

void Anton(int *arr)
{
    int sum = 0;
    while (arr[0] != 0 && arr[2] != 0 && arr[3] != 0)
    {
        arr[0]--;
        arr[2]--;
        arr[3]--;
        sum += 256;
    }
    while (arr[0] != 0 && arr[1] != 0)
    {
        arr[0]--;
        arr[1]--;
        sum += 32;
    }
    cout << sum;
}

int main()
{
    int arr[4];
    for (int i = 0; i < 4; i++)
    {
        do
        {
            cin >> arr[i];
        } while (arr[i] < 0 || arr[i] > 5000000);
    }
    Anton(arr);
    return 0;
}