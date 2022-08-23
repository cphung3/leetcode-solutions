class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B): return False


        Adict = {i: A[i] for i in range(len(A))}
        Bdict = {i: B[i] for i in range(len(B))}

        swaps = 0
        for i in range(len(A)):
            if Adict[i] != Bdict[i]:
                swaps += 1
                swapkey = self.search(Bdict[i], Adict, i)
                if swapkey is not None:
                    Adict[swapkey], Adict[i] = Adict[i], Adict[swapkey]
            else:
                swapkey = self.search(Bdict[i], Adict, i)
                if swapkey is not None:
                    swaps += 1
            break
        if A == B:
            if swaps == 0:
                return False
            elif len(set(A)) == len(set(B)):
                return True
        for i in range(len(A)):
            if Adict[i] != Bdict[i]:
                return False
        return True


    def search(self, dst, mapping, old):
        for key, item in mapping.items():
            if item == dst and key != old:
                return key
        return None
