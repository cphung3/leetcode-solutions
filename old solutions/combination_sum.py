

def combinationSum(candidates, target: int):
    
    memo = {}
    ans = []

    def recurse(candidates, target, idx, accum, ans):
        print('accum: ', accum)
        result = candidates[idx] + sum(accum)
        accum.append(candidates[idx])
        if result > target:
            return
        elif result == target:
            return accum

        # for i, num in enumerate(candidates):
        add = recurse(candidates, target, idx, accum, ans)
        skip = recurse(candidates, target, idx + 1, accum,ans)

        if add:
            ans.append(add)
        if skip:
            ans.append(skip)
        return ans
    for i in range(len(candidates)):
        tried = recurse(candidates, target, i, [], ans)
        if tried:
            ans.append(tried)
        print('this,', tried)
    return ans


candidates = [2,3,6,7]
target = 7

print(combinationSum(candidates, target))

'''
// Print all members of ar[] that have given 
void findNumbers(vector<int>& ar, int sum, 
                 vector<vector<int> >& res, 
                 vector<int>& r, int i) 
{ 
    // If  current sum becomes negative 
    if (sum < 0) 
        return; 
  
    // if we get exact answer 
    if (sum == 0) 
    { 
        res.push_back(r); 
        return; 
    } 
  
    // Recur for all remaining elements that 
    // have value smaller than sum. 
    while (i < ar.size() && sum - ar[i] >= 0) 
    { 
  
        // Till every element in the array starting 
        // from i which can contribute to the sum 
        r.push_back(ar[i]); // add them to list 
  
        // recur for next numbers 
        findNumbers(ar, sum - ar[i], res, r, i); 
        i++; 
  
        // remove number from list (backtracking) 
        r.pop_back(); 
    } 
} 
  
// Returns all combinations of ar[] that have given 
// sum. 
vector<vector<int> > combinationSum(vector<int>& ar, 
                                            int sum) 
{ 
    // sort input array 
    sort(ar.begin(), ar.end()); 
  
    // remove duplicates 
    ar.erase(unique(ar.begin(), ar.end()), ar.end()); 
  
    vector<int> r; 
    vector<vector<int> > res; 
    findNumbers(ar, sum, res, r, 0); 
  
    return res; 
} 
'''


if total < 0:
    return

if total == 0:
    res.append(accum)
    return;

while (i < len(candidates) and total - candidates[i] >= 0):
    accum.append(candidates[i]); # add them to list
    findNumbers(candidates, total - candidates[i], res, r, i); 