def longestCommonSuffixStr(query_str, trie):
    node = trie
    len = 0
    for i in range(len(query_str)):
        if query_str[i] not in node.children:
            break
        node = node.children[query_str[i]]
        len += 1
    return len



class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False
        self.frequency = 0

    def insert(self, string):
        if not string:
            return
        if string[0] not in self.children:
            self.children[string[0]] = TrieNode()
        self.children[string[0]].insert(string[1:])
        self.frequency += 1

def main():
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(input()[::-1]) # reverse the string to find the longest common suffix
    trie = TrieNode()
    for i in range(n):
        trie.insert(arr[i])

    q = int(input())
    for _ in range(q):
        query_str = input()[::-1]
        longestLen = longestCommonSuffixStr(query_str, trie)
        substr = query_str[:longestLen]
        maxLen = 0
        ind = -1
        for i in range(n):
            if arr[i].endswith(substr):
                maxLen = max(maxLen, len(arr[i]))
                ind = i
        print(arr[ind][::-1])


if __name__ == '__main__':
    main()