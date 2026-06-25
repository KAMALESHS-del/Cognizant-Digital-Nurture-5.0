def stockSpan(price):

    stack = []      # Stores indices
    span = []       # Stores answers

    for i in range(len(price)):

        while stack and price[stack[-1]] <= price[i]:
            stack.pop()

        if not stack:
            span.append(i + 1)
        else:
            span.append(i - stack[-1])

        stack.append(i)

    return span


price = [100, 80, 60, 70, 60, 75, 85]

print(stockSpan(price))