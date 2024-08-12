'''
Objective: The aim of this assignment is to enhance your skills in using Python sets for data analysis tasks. You will apply various set operations to handle real-world data scenarios, focusing on their practical application and efficiency.

Task 1: Duplicate Entries Cleanup 
You are given a list of customer IDs, some of which are duplicated. Write a Python script to remove duplicates and display the unique customer IDs.

Example Code:

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
Expected Outcome: A set of unique customer IDs, ensuring no duplicates. For instance, `{'C001', 'C002', 'C003', 'C004'}`. ---
'''
customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
# this collection type conversion removes duplicates because sets automatically remove duplicates
unique_ids = set(customer_ids)
print(unique_ids)

#alternatively, this removes any element that had a duplicate, not just the duplicate
fully_unique_ids = unique_ids
for id in customer_ids:
    if customer_ids.count(id) > 1:
        fully_unique_ids.discard(id)
print(fully_unique_ids)


