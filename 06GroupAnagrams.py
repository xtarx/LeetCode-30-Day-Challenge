from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramsIndices = dict()
        for index,word in enumerate(strs):
            sortedWord=''.join(sorted(word))
            if sortedWord in anagramsIndices:
                # append the new number to the existing array at this slot
                anagramsIndices[sortedWord].append( strs[index])
            else:
                # create a new array in this slot
                anagramsIndices[sortedWord] = [ strs[index]]

        return (anagramsIndices.values())


s1 = Solution();
print(s1.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
