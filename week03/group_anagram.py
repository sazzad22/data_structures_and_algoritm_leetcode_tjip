# TC : O(N*MlogM) M = number of Char in Stirng , N = length of strs list
# SC : O(N)


from collections import defaultdict

def return_of_default_dict():
    return []

class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_str_to_matched_str_list_dict : defaultdict = defaultdict(return_of_default_dict)

        for string in strs:
            identifier_str = ''.join(sorted(string))
            sorted_str_to_matched_str_list_dict[identifier_str].append(string)

        return list(sorted_str_to_matched_str_list_dict.values())