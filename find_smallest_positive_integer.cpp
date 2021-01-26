#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> &A) {
    // write your code in C++14 (g++ 6.2.0)
    sort(A.begin(), A.end());

    if (A.back() < 1 || A.front() > 1) {
        return 1;
    }

    auto _nextInt = A.front();
    for (size_t i = 0; i < A.size() -1 ; i++) {

        if (A[i] == A[i+1])
            continue;

        _nextInt++;
        if (_nextInt < 1) {
            i--;
            continue;
        }
        else if (_nextInt == A[i+1]) {
            continue;
        }
        else {
            return  _nextInt;
        }

    }

    return A.back()+1;
}

/* Write a function:

class Solution { public int solution(int[] A); }

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000]. */

