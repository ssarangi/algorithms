#include <vector>
#include <string>
#include <limits>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        int num_words = words.size();
        // Now create a 2D array of the size of num words which will store the
        // costs.
        vector<vector<int>> costs;
        costs.resize(num_words);

        for (int i = 0; i < num_words; ++i) {
            costs[i].resize(num_words);
        }

        int inf = numeric_limits<int>::max();

        for (int i = 0; i < num_words; ++i) {
            for (int j = i; j < num_words; ++j) {
                int total_len_of_words = 0;
                for (int w = i; w <= j; ++w) {
                    total_len_of_words += words[w].length();
                }

                int num_spaces_left = (maxWidth - total_len_of_words - (j - i));
                num_spaces_left = num_spaces_left >= 0 ? num_spaces_left * num_spaces_left : inf;
                costs[i][j] = num_spaces_left;

                cout << "Cost: " << i << " " << j << " = " << costs[i][j] << std::endl;
            }
        }

        // Now use this information of costs for calculating the best possible
        // justification.

        int i = num_words - 1;
        std::vector<int> split_pts;
        std::vector<int> best_costs;

        split_pts.resize(num_words);
        best_costs.resize(num_words + 1);
        best_costs[num_words] = 0;

        while (i >= 0) {
            // Initialize the j to the complete end since we will start checking
            // from what point of i till the end we can use.
            int j = num_words - 1;
            int best_val = costs[i][j];
            int best_idx = j + 1;

            while (j >= i ) {
                if (costs[i][j] != inf && best_val > costs[i][j] + best_costs[j+1]) {
                    best_val = costs[i][j] + best_costs[j+1];
                    best_idx = j + 1;
                }

                j -= 1;
            }

            best_costs[i] = best_val;
            split_pts[i] = best_idx;
            i -= 1;
        }

        for (auto val : best_costs) {
            std::cout << "Best cost: " << val << std::endl;
        }

        for (auto idx : split_pts) {
            std::cout << "Best Idx: " << idx << std::endl;
        }

        vector<string> output;
        int start = 0;
        bool all_covered = false;
        std::string current_line;
        while (!all_covered) {
            current_line = "";
            int end = split_pts[start];
            for (int i = start; i < end; ++i)
                current_line += words[i] + " ";

            start = end;
            if (end >= num_words)
                all_covered = true;
            output.push_back(current_line);
        }

        return output;
    }
};

int main() {
    Solution soln;

    // std::vector<std::string> words {"This", "is", "an", "example", "of", "text", "justification."};
    vector<string> words {"tushar", "roy", "likes", "to", "code"};

    int maxWidth = 10;
    soln.fullJustify(words, maxWidth);
    return 0;
}
