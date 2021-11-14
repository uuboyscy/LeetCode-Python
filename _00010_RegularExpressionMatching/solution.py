class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pWordList = list(p)
        pList = list()
        pLength = p.__len__()
        sIdx = 0
        sLength = s.__len__()
        ## 'a' -> ['a']; 'a*' -> ['a*']; '.*' -> ['.*']; 'c*a*b' -> ['c*', 'a*', 'b']
        for n, w in enumerate(pWordList):
            if (n != pLength - 1) and (w != '*'):
                if pWordList[n + 1] == '*':
                    pList.append(w + pWordList[n + 1])
                else:
                    pList.append(pWordList[n])
            elif (n == pLength - 1) and (w != '*'):
                pList.append(w)
        pLength = pList.__len__()
        print(p, '->', pList)

        for eachP in pList:
            print('[Now pattern]:', eachP)
            if eachP.__len__() == 1:
                if eachP == s[sIdx] or eachP == '.':
                    print('\t[Now word1]:', s[sIdx])
                    sIdx += 1
                else:
                    print('\t[Now word2]:', s[sIdx])
                    return False
            else:
                precWord = eachP[0]
                leadingWordNowForS = s[sIdx]
                if (leadingWordNowForS == precWord) or (precWord == '.'):
                    while True:
                        if sIdx + 1 < sLength and leadingWordNowForS == s[sIdx + 1]:
                            print('\t[Now word3]:', s[sIdx])
                            sIdx += 1
                            leadingWordNowForS = s[sIdx]
                        elif sIdx == sLength - 1 and leadingWordNowForS == precWord:
                            print('\t[Now word4]:', s[sIdx])
                            break
                        else:
                            print('\t[Now word5]:', s[sIdx])
                            break

        if sIdx != sLength:
            return False

        return True

if __name__ == '__main__':
    sol = Solution()

    s = "aa"
    p = "a"
    print('s = %s\np = %s\n'%(s, p), sol.isMatch(s, p))
    print('======')

    s = "aa"
    p = "a*"
    print('s = %s\np = %s\n'%(s, p), sol.isMatch(s, p))
    print('======')

    s = "ab"
    p = ".*"
    print('s = %s\np = %s\n'%(s, p), sol.isMatch(s, p))
    print('======')

    s = "aab"
    p = "c*a*b"
    print('s = %s\np = %s\n'%(s, p), sol.isMatch(s, p))
    print('======')

    s = "abc"
    p = "abc"
    print('s = %s\np = %s\n'%(s, p), sol.isMatch(s, p))
    print('======')

    s = "aaa"
    p = "..."
    print('s = %s\np = %s\n'%(s, p), sol.isMatch(s, p))
    print('======')

