class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morsealphabet = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                         "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        morselist = []
        for i in words:
            temp = list(i)
            morseword = ""
            for j in temp:
                tempnum = ord(j)
                tempnum -= 97
                morsetemp = morsealphabet[tempnum]
                morseword += morsetemp
            morselist.append(morseword)

        uniquelist = []
        for x in morselist:
            if x not in uniquelist:
                uniquelist.append(x)

        return len(uniquelist)