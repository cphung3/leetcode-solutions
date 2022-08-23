


def threeSum(nums):

    # look at first idx, keep the same
    # look at next idx, keep the same
    # look at third idx, iterate through that

    sums = {}
    ans = []
    for i, num_i in enumerate(nums):
        for j, num_j in enumerate(nums):
            if i == j: continue
            tup = tuple(sorted((num_i, num_j)))
            result = num_i + num_j
            if tup not in sums: 
                sums[tup] = result
            for k, num_k in enumerate(nums):
                if len(set((i, j, k))) < 3: continue
                if tuple(sorted((num_i, num_j, num_k))) in sums:
                    continue
                tup = tuple(sorted((num_i, num_j)))
                if tup in sums: 
                    add = sums[tup]
                else:
                    add = num_i + num_j
                total = add + num_k
                if total == 0:
                    res = [num_i, num_j, num_k]
                    ans.append(res)
                tupThree = tuple(sorted((num_i, num_j, num_k)))
                sums[tupThree] = total

    return ans



def find3Numbers(nums): 
    ans = set([])
    A, arr_size, total = nums, len(nums), 0
    for i in range(0, arr_size-1): 
        # Find pair in subarray A[i + 1..n-1]  
        # with total equal to total - A[i] 
        s = set([]) 
        curr_total = total - A[i] 
        for j in range(i + 1, arr_size): 
            if j == i: continue
            res = tuple(sorted([A[i], A[j], curr_total-A[j]]))
            if res in ans: continue
            if (curr_total - A[j]) in s: 
                if res not in ans:
                    ans.add(res)
                # print("Triplet is", A[i], ", ", A[j], ", ", curr_total-A[j]) 
            s.add(A[j]) 
    return [list(tup) for tup in ans]

def find3Numbers(nums): 

    ans = set([])
    A, arr_size, total = nums, len(nums), 0
    # Sort the elements  
    A.sort() 
  
    # Now fix the first element  
    # one by one and find the 
    # other two elements  
    for i in range(0, arr_size-2): 
        # To find the other two elements, 
        # start two index variables from 
        # two corners of the array and 
        # move them toward each other 
          
        # index of the first element 
        # in the remaining elements 
        l = i + 1 
        if A[i] > total:
            break
          
        # index of the last element 
        r = arr_size-1 
        if (A[i] == A[l] == A[r]) and tuple(sorted([A[i], A[l], A[r]])) in ans:
            continue
        while (l < r): 
            res = tuple(sorted([A[i], A[l], A[r]]))
            print(i, l, r)
            # if res in ans:
            #     continue
            if( A[i] + A[l] + A[r] == total): 
                if res not in ans:
                    ans.add(res)
                l += 1
            elif (A[i] + A[l] + A[r] < total): 
                l += 1
            else: # A[i] + A[l] + A[r] > total 
                r -= 1
  
    # If we reach here, then 
    # no triplet was found 
    return [list(tup) for tup in ans]


print(find3Numbers([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))