import embedding_model_test


cache_file="cache_theme.json"
cache = embedding_model_test.init(cache_file)



Theme = embedding_model_test.get_cache(cache_file) # get the list of buckets from cache
if Theme is None: # if the is no cache file
    start_theme = ["Love", "Sacrfice", "Sad", "Death", "Dark"]
    embedding_model_test.start_cache(start_theme) # add the starting elements to the cache so we have a base of buckets to start with
    Theme= embedding_model_test.get_cache(cache_file) # get the list of buckets from cache

print(Theme)
EMBEDDING_MODEL = "text-embedding-3-small"

max_distance = 0.4

word2 = input("input theme: ")
Dis_list = []

for theme in Theme:
    print("theme: ", theme)
    distance = embedding_model_test.nearest_word_E_D(theme, word2)
    Dis_list.append((theme, distance))

# Sort by distance
Dis_list.sort(key=lambda x: x[1])

# Find the closest 
closest_distance = Dis_list[0]
print(closest_distance)
closest_theme = Dis_list[0][0]
if closest_distance[1]>max_distance:
    print("make new bucket for :", word2)
    embedding_model_test.new_bucket(word2)
    print("Sucessfully made new bucket for :", word2)
else:
    print(f"The closest theme is: {closest_theme}")
    # we here need to add the theme to the list of closest themes