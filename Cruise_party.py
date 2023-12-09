''' A party has been organized on cruise. The party is organized for a limited time(T).
    The number of guests entering (E[i]) and leaving (L[i]) the party at every hour is
    represented as elements of the array. The task is to find the maximum number of
    guests present on the cruise at any given instance within T hours.'''

def maximum_guests_within_time(T, E, L):
    events = []
    current_guests = E[0] - L[0]
    events.append(current_guests)

    for i in range(1, T):
        current_guests += E[i] - L[i]
        events.append(current_guests)

    return max(events)

if __name__=='__main__':
    entries = [10, 5, 15, 20]
    exits = [5, 10, 5, 10]
    T = len(entries)

    result = maximum_guests_within_time(T, entries, exits)
    print(result)