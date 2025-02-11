/**
 * // This is the Master's API interface.
 * // You should not implement it, or speculate about its implementation
 * class Master {
 *   public:
 *     int guess(string word);
 * };
 */
class Solution {
public:
    int distance(string w1, string w2) {
        if (w1.size() != w2.size()) return -2;

        int matches = 0;

        for (int i = 0; i < w1.size(); i++) {
            if (w1[i] == w2[i]) {
                matches++;
            }
        }

        return matches;
    }

    void findSecretWord(vector<string>& words, Master& master) {
        unordered_set<string> wordSet(words.begin(), words.end());

        while (!wordSet.empty()) {
            string first = *wordSet.begin();

            int guessed = master.guess(first);

            for (auto it = wordSet.begin(); it != wordSet.end();) {
                if (distance(*it, first) != guessed)
                    it = wordSet.erase(it);
                else
                    it++;
            }

            wordSet.erase(first);
        }
    }
};
