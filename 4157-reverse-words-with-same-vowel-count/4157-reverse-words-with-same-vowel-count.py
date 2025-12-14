class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        f =lambda x: sum(x.count(c) for c in "aeiou")

        return " ".join([words[0]] + [w if f(w) !=f(words[0]) else w[::-1] for w in words[1:]])

        