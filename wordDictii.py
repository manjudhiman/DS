class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        
        wordDict = set(wordDict)
        
        def helper(start, i, curr):
            
            if i == len(s):
                if len(''.join(curr)) == len(s):
                    res.append(' '.join(curr))
                return
                
            '''
            to skip the letter
            '''
            helper(start, i+1, curr)
            
            '''
            to include
            '''
            if s[start:i+1] in wordDict:
                curr.append(s[start:i+1])
                helper(i+1,i+1,curr)
                curr.pop()
            
        
            
        helper(0,0,[])
        
        return res
        
        
