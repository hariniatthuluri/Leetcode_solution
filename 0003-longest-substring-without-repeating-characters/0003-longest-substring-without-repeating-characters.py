class Solution(object):
    def lengthOfLongestSubstring(self, s):
        m_len=0
        for i in range(len(s)):       
            h=set()

            for j in range(i,len(s)):
                if s[j] in h:
                    break

                h.add(s[j])
            m_len=(max(m_len,len(h)))
        return m_len