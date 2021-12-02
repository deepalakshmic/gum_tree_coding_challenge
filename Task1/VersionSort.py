def version_sort(versions, is_reverse=True):
  versions.sort(key=lambda x: [ int(x) for x in x.split(".")], reverse=is_reverse)
  return versions

print(version_sort(["1.0.1", "2.14.15"]))
print(version_sort(["4.3.11", "4.5.6"]))
print(version_sort(["3.9.5", "4.3.11", "1.2.11", "8.1.2", "4.3.6", "4.5.6"]))
