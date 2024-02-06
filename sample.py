# country_capital = {
#   "Germany": 1, 
#   "Canada": 1, 
#   "England": 1
# }
# country_capitals = {
#   "Germany": 1, 
#   "Italy": 1, 
#   "England": 1
# }

# co = country_capital | country_capitals
# print(set(country_capital))


# full_dict = {k:country_capital.get(k,0) + country_capitals.get(k,0) 
#              for k in set(country_capital | country_capitals) 

# }
# print(full_dict)
# create_a_sample = {k:k for k in range(1,10)}
# print(create_a_sample)

a = 0 // 10
print(a)