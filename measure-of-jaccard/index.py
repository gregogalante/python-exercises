# Define two set of users preferred clothes stores
user1 = {"Target", "Banana Republic", "Old Navy"}
user2 = {"Banana Republic", "Gap", "Kohl's"}

def jaccard(set1, set2):
    stores_in_common = len(set1 & set2)
    stores_all_together = len(set1 | set2)
    return stores_in_common / float(stores_all_together)

print jaccard(user1, user2)
