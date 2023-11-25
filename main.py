
def generate_combinations(length, start, end, prefix=None):
    if length == 0: return [prefix]
    if prefix is None: prefix = []

    combinations = []
    for i in range(start, end + 1):
        new_prefix = prefix + [i]
        combinations.extend(generate_combinations(length - 1, start, end, new_prefix))

    return combinations



def P(n: int, summanden: int, validSummanden: list[int], ignoreOrder: bool = False) -> list[list[int]]:
    allCombinations = generate_combinations(summanden, validSummanden[0], validSummanden[-1])
    validCombinations: list[list[int]] = []

    for combination in allCombinations:
        if sum(combination) == n:
            if all(item in validSummanden for item in combination):
                if ignoreOrder:
                    combination.sort()
                    if combination in validCombinations:
                        continue

                validCombinations.append(combination)


    return validCombinations


results = P(21, 6, list(range(1, 6+1)), ignoreOrder=True)
print(len(results))
