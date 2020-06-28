'''Given a string S that only contains "I" (increase) or "D" 
(decrease), let N = S.length.

Return any permutation A of [0, 1, ..., N] such that for all 
i = 0, ..., N-1:

If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]'''

'''Input: "IDID"
Output: [0,4,1,3,2]'''

def diStringMatch(S):
        inc = 0
        dec = len(S)
        ans = []
        for s in S:
            if s == 'I':
                ans.append(inc)
                inc +=1
            elif s == 'D':
                ans.append(dec)
                dec -=1
                
        if S[-1] == "D":
            ans.append(dec)
        else:
            ans.append(inc)
        return ans
