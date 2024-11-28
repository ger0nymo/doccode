#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;
    std::vector<int> nums(n);
    for(int i = 0; i < n; ++i)
        std::cin >> nums[i];
    int sum = 0;
    for(int num : nums)
        sum += num;
    double average = static_cast<double>(sum) / n;
    std::cout << "Average: " << average << std::endl;
    return 0;
}
