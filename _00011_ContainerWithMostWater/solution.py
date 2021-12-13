'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.
'''

class Solution1:
    def maxArea(self, height: list) -> int:
        c = 0
        result = 0
        for idx1, h1 in enumerate(height[:-1]):
            for idx2, h2 in enumerate(height[idx1 + 1:]):
                x = idx2 + 1
                y = min([h1, h2])
                result = max([result, x * y])
                c += 1
        print('Total compute:', c)
        return result

class Solution2:
    def maxArea(self, height: list) -> int:
        c = 0
        result = 0
        heightIndexMap = dict() # {height: [idx1, idx2, idx3, ...], ...}, the height keys need to be ordered
        heightIndexMapList = list()
        for i, h in enumerate(height):
            if h == 0: continue
            if h in heightIndexMap:
                heightIndexMap[h].append(i)
            else:
                heightIndexMap[h] = [i]
            c += 1

        ## Sort each value ascending, adding it into heightIndexMapList as (height, idxMin, idxMax)
        for k, v in heightIndexMap.items():
            v.sort()
            heightIndexMapList.append((k, v[0], v[-1]))
            c += 1

        ## Sort heightIndexMapList by height descending
        heightIndexMapList.sort(key=lambda x: x[0], reverse=True)

        for i, hMain in enumerate(heightIndexMapList):
            if hMain[1] == hMain[2]: i += 1
            for hSub in heightIndexMapList[i:]:
                tmpResult = hSub[0] * max([hMain[2] - hSub[1], hSub[2] - hMain[1]])
                result = max([result, tmpResult])
                c += 1
        print('Total compute:', c)
        return result

class Solution3:
    def maxArea(self, height: list) -> int:
        c = 0
        leftIdx = 0
        rightIdx = height.__len__() - 1
        result = 0

        while leftIdx < rightIdx:
            hr = height[rightIdx]
            hl = height[leftIdx]
            if hr == 0:
                rightIdx -= 1
                continue
            if hl == 0:
                leftIdx += 1
                continue
            result = max([result, (rightIdx - leftIdx) * min([hr, hl])])
            if height[rightIdx] > height[leftIdx]:
                leftIdx += 1
            else:
                rightIdx -= 1
            c += 1

        print('Total compute:', c)
        return result

if __name__ == '__main__':
    import json
    # s = Solution2()
    # print(s.maxArea([1,8,6,2,5,4,8,3,7])) # 49
    # print(s.maxArea([1,1])) # 1
    # print(s.maxArea([4,3,2,1,4])) # 16
    # print(s.maxArea([1,2,1])) # 2
    # print(s.maxArea(json.load(open('sample.json', 'r')))) # 48431514
    # print(s.maxArea(json.load(open('sample2.json', 'r')))) # 49024602
    #
    # print('=====')
    #
    # s = Solution1()
    # print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
    # print(s.maxArea([1, 1]))  # 1
    # print(s.maxArea([4, 3, 2, 1, 4]))  # 16
    # print(s.maxArea([1, 2, 1]))  # 2
    # print(s.maxArea(json.load(open('sample.json', 'r'))))  # 48431514
    # print(s.maxArea(json.load(open('sample2.json', 'r'))))  # 49024602

    print('=====')

    s = Solution3()
    print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
    print(s.maxArea([1, 1]))  # 1
    print(s.maxArea([4, 3, 2, 1, 4]))  # 16
    print(s.maxArea([1, 2, 1]))  # 2
    print(s.maxArea(json.load(open('sample.json', 'r'))))  # 48431514
    print(s.maxArea(json.load(open('sample2.json', 'r'))))  # 49024602
