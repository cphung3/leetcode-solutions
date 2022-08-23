class Solution:
    def defangIPaddr(self, address: str) -> str:
        split = address.split('.')
        return '[.]'.join(split)
