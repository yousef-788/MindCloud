#include <iostream>
using namespace std;

int main() {
    int s, t, a, b, m, n;
    cin >> s >> t;
    cin >> a >> b;
    cin >> m >> n;

    int arr1[m];
    int arr2[n];

    int appleCount = 0;
    int orangeCount = 0;

    for (int i = 0; i < m; i++) {
        cin >> arr1[i];
    }

    for (int i = 0; i < n; i++) {
        cin >> arr2[i];
    }

    for (int i = 0; i < m; i++) {
        int position = a + arr1[i];
        if (position >= s && position <= t) {
            appleCount++;
        }
    }

    for (int i = 0; i < n; i++) {
        int position = b + arr2[i];
        if (position >= s && position <= t) {
            orangeCount++;
        }
    }

    cout << appleCount << endl;
    cout << orangeCount << endl;

    return 0;
}