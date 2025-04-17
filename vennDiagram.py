def vennDiagram():
    set1 = {"a", "b", "c", "d", "i", "j", "k", "l", "m"}
    set2 = {"d", "e", "f", "g", "h", "i", "j", "n", "o", "p"}
    set3 = {"q", "r", "s", "t", "i", "j", "n", "o", "p", "k", "l", "m"}

    return set1, set2, set3

set1, set2, set3 = vennDiagram()


print(set1.intersection(set2).intersection(set3))
line2 = sorted(set1 - set2 - set3)
print(line2)
allIntersection = set1.intersection(set2).intersection(set3)
intersect2and3 = set2.intersection(set3)
line3 = sorted(allIntersection.union(intersect2and3))
print(line3)
intersection1and2 = set1.intersection(set2)
line4 = intersection1and2 - allIntersection
print(line4)
intersection1and3 = set1.intersection(set3)
line5 = sorted(intersection1and3.union(intersect2and3) - allIntersection)
print(line5)
