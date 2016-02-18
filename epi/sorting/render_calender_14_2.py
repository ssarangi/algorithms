def render_calender(events):
    overlapping = []
    events = sorted(events, key=lambda x: x[0])

    for i, event in enumerate(events):
        for nevent in range(i+1, len(events)):
            if event[1] > events[nevent][0]:
                overlapping.append((event, events[nevent]))

    return overlapping

def main():
    events = [(1, 5), (6, 10), (11, 13), (14, 15), (2, 7), (8, 9), (12, 15), (4, 5), (9, 17)]
    print(render_calender(events))

if __name__ == "__main__":
    main()