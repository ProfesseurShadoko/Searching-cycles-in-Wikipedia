from wiki_map import WikiMap

map = WikiMap()
map.add_philo()

for i in range(100):
    map.append_rd()
    if i%10==0:
        print(map)
        print(map.__repr__())

print("\nFINAL RESULTS :")
print(map)

print()

print(repr(map))
        