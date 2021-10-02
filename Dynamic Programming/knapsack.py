
class Item:
    def __init__(self, name, weight, profit):
        self.name = name
        self.weight = weight
        self.profit = profit
    
    def __repr__(self):
        return f"Item({self.name}, w='{self.weight}', p='{self.profit}')"
        

def knapsack(items, capacity):
    n = len(items)
    if n == 0:
        return 0
    
    dp = [[0 for j in range(capacity + 1)] for i in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if i == 0 or j == 0:
                pass
            elif items[i - 1].weight <= j: 
                dp[i][j] = max(
                    items[i - 1].profit + dp[i - 1][j - items[i - 1].weight], 
                    dp[i - 1][j] 
                )
            else:
                dp[i][j] = dp[i - 1][j]
    
    for i in range(n + 1):
        print(dp[i])
        
    print("Maximum profit", dp[n][capacity])
    


if __name__ == '__main__':
    items = [
        Item('a', 1, 10), 
        Item('b', 2, 12), 
        Item('c', 4, 28)    
    ]
    
    capacity = 6
    
    knapsack(items, capacity)