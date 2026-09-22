class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1 # By def, every stock will have a span of 1

        # As long as the stack exists and top most price is <= current price
        while self.stack and self.stack[-1][0] <= price:
            # We keep updating the current span and popping as we don't really need smaller prices
            span += self.stack[-1][1]
            self.stack.pop()
        
        # Append the current price and span
        self.stack.append([price, span])

        # Return the current span
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)