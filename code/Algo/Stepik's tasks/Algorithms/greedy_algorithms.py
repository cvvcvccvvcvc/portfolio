#   greedy algorithm are approximation algorithms for problems, that have a complex solutions (in time)
#   approximation alg's judjed by: 1.speed, 2.how close to optimal solution

states_needed = set(["mt", "wa", "or", "id", "nv", 'ut', 'ca', 'az'])    # set is like a list, but it can't have(!!!) duplicates     set() deletes duplicates when converts(!!!)
stations = {}                                # key = stations, values = states, that it covers
stations['kone'] = set(["id", "nv", "ut"])
stations['ktwo'] = set(["wa", "id", "mt"])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])
final_stations = set()
def greedy_finding_smallest_array_of_stations(states_needed, stations, final_stations):
    while len(states_needed) != 0:
        best_station = None                                   # covers more states then others
        states_covered = set()                                # states that cover this station (only not covered before)
        for station, states_for_station in stations.items():       # loop over every station to find the best   items returns [(key1, value1), (key2, value2)]   key-station, value-states в set
            covered = states_needed & states_for_station          # what states cover this station     set of uncovered states that this station covers!
            if len(covered) > len(states_covered):                 #  is this st. better than current  best st.
                best_station = station                               # changing
                states_covered = covered
        final_stations.add(best_station)
        states_needed = states_needed - states_covered
        print(states_needed)

greedy_finding_smallest_array_of_stations(states_needed, stations, final_stations)
print(final_stations)