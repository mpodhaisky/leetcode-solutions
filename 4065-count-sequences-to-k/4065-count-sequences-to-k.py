class Solution:
    def countSequences(self, nums: List[int], k: int) -> int:
        counts = Counter(nums)
        
        v5_k = 0
        while k > 0 and k % 5 == 0:
            v5_k += 1
            k //= 5
            
        def get_ways(total_n, target_exp):
            res = 0
            for i in range(total_n + 1):
                rem = total_n - i
                if (rem + target_exp) % 2 == 0:
                    x = (rem + target_exp) // 2
                    if 0 <= x <= rem:
                        res = res + comb(total_n, i) * comb(rem, x)
            return res

        ways_5 = get_ways(counts[5], v5_k)
        if ways_5 == 0: return 0

        v2_k, v3_k = 0, 0
        for p in [2, 3]:
            while k > 0 and k % p == 0:
                if p == 2: v2_k += 1
                else: v3_k += 1
                k //= p
        if k != 1: return 0

        dp = {(0, 0): 1}
        
        impacts = {2: (1, 0), 3: (0, 1), 4: (2, 0), 6: (1, 1)}
        
        for val in [2, 3, 4, 6]:
            if counts[val] == 0: continue
            dv2, dv3 = impacts[val]
            new_dp = defaultdict(int)
            
            possible_nets = {}
            for net in range(-counts[val], counts[val] + 1):
                w = get_ways(counts[val], net)
                if w: possible_nets[net] = w
            
            for (e2, e3), current_ways in dp.items():
                for net, ways_to_get_net in possible_nets.items():
                    new_e2 = e2 + (net * dv2)
                    new_e3 = e3 + (net * dv3)
                    new_dp[(new_e2, new_e3)] = new_dp[(new_e2, new_e3)] + current_ways * ways_to_get_net
            dp = new_dp

        return dp.get((v2_k, v3_k), 0) * ways_5 * pow(3, counts[1])