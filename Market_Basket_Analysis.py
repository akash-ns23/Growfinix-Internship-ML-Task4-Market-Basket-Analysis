import pandas as pd
from itertools import combinations

# -------------------------------
# Step 1: Sample Transactions
# -------------------------------
transactions = [
    ['Bread', 'Milk'],
    ['Bread', 'Diaper', 'Beer', 'Eggs'],
    ['Milk', 'Diaper', 'Beer', 'Coke'],
    ['Bread', 'Milk', 'Diaper', 'Beer'],
    ['Bread', 'Milk', 'Diaper', 'Coke'],
    ['Milk', 'Diaper', 'Beer'],
    ['Bread', 'Milk', 'Eggs'],
    ['Bread', 'Eggs'],
    ['Milk', 'Eggs'],
    ['Bread', 'Milk', 'Diaper']
]

# -------------------------------
# Step 2: Get all unique items
# -------------------------------
items = sorted(set(item for transaction in transactions for item in transaction))

# -------------------------------
# Step 3: Function to calculate support
# -------------------------------
def support(itemset):
    count = 0
    for t in transactions:
        if set(itemset).issubset(set(t)):
            count += 1
    return count / len(transactions)

# -------------------------------
# Step 4: Find frequent itemsets
# -------------------------------
min_support = 0.3
frequent_itemsets = {}

for r in range(1, 3):  # pairs only for simplicity
    for combo in combinations(items, r):
        sup = support(combo)
        if sup >= min_support:
            frequent_itemsets[combo] = sup

# -------------------------------
# Step 5: Display Frequent Itemsets
# -------------------------------
print("FREQUENT ITEMSETS:")
for itemset, sup in frequent_itemsets.items():
    print(itemset, "-> Support:", round(sup, 2))

# -------------------------------
# Step 6: Generate Simple Rules
# -------------------------------
print("\nASSOCIATION RULES:")

for itemset in frequent_itemsets:
    if len(itemset) > 1:
        for i in range(len(itemset)):
            antecedent = tuple([itemset[i]])
            consequent = tuple([x for x in itemset if x != itemset[i]])

            conf = support(itemset) / support(antecedent)

            print(antecedent, "->", consequent, "| Confidence:", round(conf, 2))

print("\nTask Completed Successfully!")
