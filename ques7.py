class Solution:
    from itertools import product
    def letterCombinations(self, digits: str) -> List[str]:
        dataSet={"2":["a","b","c"],
        "3":["d","e","f"],
        "4":["g","h","i"],
        "5":["j","k","l"],
        "6":["m","n","o"],
        "7":["p","q","r","s"],
        "8":["t","u","v"],
        "9":["w","x","y","z"]}
        if not digits:
            return []
        chars=[dataSet[digit] for digit in digits]
        ans=["".join(comb) for comb in product(*chars)]
        return ans