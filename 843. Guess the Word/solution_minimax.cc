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
        for (int i = 0, match = 0; i < 10 and match < 6; i++) {
            unordered_map<string, int> wordCount;

            for (string w1 : words) {
                for (string w2 : words) {
                    if (distance(w1, w2) == 0) {
                        wordCount[w1]++;
                    }
                }
            }

            pair<string, int> minimax = { words[0], 10000 };

            for (string w : words) {
                if (wordCount[w] <= minimax.second) {
                    minimax = make_pair(w, wordCount[w]);
                }
            }

            int masterMatch = master.guess(minimax.first);

            vector<string> candidateWords = {};

            for (string w : words) {
                if (distance(w, minimax.first) == masterMatch) {
                    candidateWords.push_back(w);
                }
            }
            words = candidateWords;
        }
    }
};
