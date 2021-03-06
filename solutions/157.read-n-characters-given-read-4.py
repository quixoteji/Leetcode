#
# @lc app=leetcode id=157 lang=python3
#
# [157] Read N Characters Given Read4
#

# @lc code=start
"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        readBytes = 0
        while (readBytes < n):
            tmpBuf = [' '] * 4
            tmpBytes = read4(tmpBuf)
            # print ("tmpBytes = ", tmpBytes)
            # print ("tmpBuf = ", tmpBuf)

            for idx in range(tmpBytes):
                if (readBytes < n):
                    buf[readBytes] = tmpBuf[idx]
                    readBytes += 1
            # print ("readBytes = ", readBytes)
            # print ("buf = ", buf)

            if (tmpBytes < 4):
                print("1 break")
                break

        # print ("after while buf = ", buf)
        return readBytes
        
# @lc code=end

