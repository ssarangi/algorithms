def power_set(els):
    if len(els) == 0:
        return []

    el0 = els[0]
    ps = power_set(els[1:])

    res = [el0]
    for i in ps:
        res.append([i])
        res.append([el0] + [i])

    if len(ps) == 0:
        res = [el0]

    return res

def main():
    els = ["A", "B", "C"]
    ps = power_set(els)
    print(ps)

if __name__ == "__main__":
    main()