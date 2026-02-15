class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        foods = sorted(set(food for _,_,food in orders))
        tables = sorted(set(table for _,table, _ in orders), key = lambda x: int(x))
        transfood = {}
        for i, n in enumerate(foods):
            transfood[n]=i
        transtable={}
        for i, n in enumerate(tables):
            transtable[n]=i
        res=[[0]*len(foods) for _ in range(len(tables))]
        for _, table, food in orders:
            res[transtable[table]][transfood[food]]+=1
        return [["Table"]+foods]+[[a] + list(map(str,b)) for a, b in zip(tables, res)]
        

