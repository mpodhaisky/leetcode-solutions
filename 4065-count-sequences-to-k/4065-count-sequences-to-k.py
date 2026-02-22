def get_ways(total_n, target_exp):
    res = 0
    for i in range(total_n + 1):
        rem = total_n - i
        if (rem + target_exp) % 2 == 0:
            x = (rem + target_exp) // 2
            if 0 <= x <= rem:
                res = res + comb(total_n, i) * comb(rem, x)
    return res

class Solution:
    def countSequences(self, nums: List[int], K: int) -> int:
        f = Counter(nums)
    
        count = [0, 0, 0]
        for i, p in enumerate([2, 3, 5]):
            while K % p == 0:
                K //= p
                count[i] += 1
        
        if K != 1: return 0            
        ways_5 = get_ways(f[5], count[-1])
        if ways_5 == 0: return 0

        dp = Counter({(0, 0): 1})
        
        impacts = {2: (1, 0), 3: (0, 1), 4: (2, 0), 6: (1, 1)}
        
        for val in [2, 3, 4, 6]:
            if not f[val] : continue
            dv2, dv3 = impacts[val]
            new_dp = Counter()
            
            possible_nets = {}
            for net in range(-f[val], f[val] + 1):
                w = get_ways(f[val], net)
                if w: possible_nets[net] = w
            
            for (e2, e3), current_ways in dp.items():
                for net, ways_to_get_net in possible_nets.items():
                    new_e2 = e2 + (net * dv2)
                    new_e3 = e3 + (net * dv3)
                    new_dp[(new_e2, new_e3)] = new_dp[(new_e2, new_e3)] + current_ways * ways_to_get_net
            dp = new_dp

        return dp[(count[0], count[1])] * ways_5 * pow(3, f[1])