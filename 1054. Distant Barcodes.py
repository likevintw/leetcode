

class Solution:
    '''
    # own best
    # 580 ms, 61.37% ,16.2 MB, 70.00%
    '''

    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        table = {}
        max_n = 0
        max_c = 0
        for i in barcodes:
            if i in table.keys():
                n = table[i]+1
                table.update({i: n})
                if n > max_n:
                    max_n = n
                    max_c = i
            else:
                table.update({i: 1})
        buffer = [max_c]*max_n
        for i in table.keys():
            if i == max_c:
                continue
            else:
                buffer += [i]*table[i]
        for i in range(0, len(barcodes), 2):
            barcodes[i] = buffer.pop(0)
        for i in range(1, len(barcodes), 2):
            barcodes[i] = buffer.pop(0)
        return barcodes

# reference:
# Runtime: O(n log n), where n is the number of unique elements.
# Memory: O(n). We store unique elements in the map and set.
# 190 ms, 22.54% ,45.6 MB, 9.47%


class Solution {
    public:
        vector < int > rearrangeBarcodes(vector < int > & b, int pos=0) {
            unordered_map < int, int > m;
            set < pair < int, int >> s;
            for (auto n: b) + +m[n];
            for (auto it=begin(m); it != end(m); ++it) s.insert({it -> second, it -> first});
            for (auto it=s.rbegin(); it != s.rend(); ++it) {
                for (auto cnt=0; cnt < it -> first; ++cnt, pos += 2) {
                    if (pos >= b.size()) pos = 1;
                    b[pos] = it -> second;}
            }
            return b; }
}

# reference:
# C++成績, 75 ms, faster than 95.90% of C++ online submissions for Distant Barcodes.
# Memory Usage: 35.9 MB, less than 98.14%


class Solution {
    public:
    vector < int > rearrangeBarcodes(vector < int > & barcodes) {
        short m[10001] = {};
        short max_cnt = 0, max_n = 0, pos = 0;
        for (auto n: barcodes) {
            max_cnt = max(max_cnt, ++m[n]);
            max_n = max_cnt == m[n] ? n: max_n;}
        for (auto i=0; i <= 10000; ++i) {
            auto n = i == 0 ? max_n: i;
            while (m[n]-- > 0) {
                barcodes[pos] = n;
                pos = pos + 2 < barcodes.size() ? pos + 2: 1;}
        }
        return barcodes; }
};


# reference 772 ms, 24.10% ,16.2 MB, 70.00%


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        # If size <= 2 no need to change order
        size = len(barcodes)
        if size <= 2:
            return barcodes

        # Make sorted array order by # of the value desc.
        # e.g. [1,2,2,3,3,3] -> [3,3,3,2,2,1,1]
        # because # of 3 is top and # of 1 is bottom
        c = collections.Counter(barcodes)
        sorted_by_cnt = []
        for k, cnt in c.most_common():
            sorted_by_cnt.extend([k] * cnt)

        new_barcodes = [0] * size

        j = 0  # use index

        # new_barcodes [3, *, 3, *, 3, *]
        for i in range(0, size, 2):
            new_barcodes[i] = sorted_by_cnt[j]
            j += 1

        # new_barcodes [3, 2, 3, 2, 3, *]
        # new_barcodes [3, 2, 3, 2, 3, 1]
        for i in range(1, size, 2):
            new_barcodes[i] = sorted_by_cnt[j]
            j += 1

        return new_barcodes
