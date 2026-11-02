# Maps in C++ and Python

## What is a map?

A map stores data as **key → value** pairs.

- Every key is unique.
- Values can repeat.
- A value is found quickly by its key.

A telephone directory is a map: the name is the key and the phone number is the value.

```text
Ali   → 85
Sara  → 92
Ahmed → 78
```

More examples:

```text
Pakistan → Islamabad        101 → Ali
Germany  → Berlin           102 → Sara
Japan    → Tokyo            103 → Ahmed
```

## Maps in C++ (`std::map`)

`std::map` is in the `<map>` header and keeps its keys **sorted**.

```cpp
#include <iostream>
#include <map>
using namespace std;

int main() {
    map<string, int> marks;
    marks["Ali"] = 85;
    marks["Sara"] = 92;
    marks["Ahmed"] = 78;

    cout << "Ali's marks: " << marks["Ali"] << endl;

    for (auto p : marks) {
        cout << p.first << " -> " << p.second << endl;
    }
    return 0;
}
```

Output (keys in alphabetical order):

```text
Ali's marks: 85
Ahmed -> 78
Ali -> 85
Sara -> 92
```

## Maps in Python (`dict`)

Python's built-in dictionary is its map. Since Python 3.7 it keeps keys in **insertion order**.

```python
marks = {"Ali": 85, "Sara": 92, "Ahmed": 78}

print("Ali's marks:", marks["Ali"])

for name, score in marks.items():
    print(name, "->", score)
```

Output:

```text
Ali's marks: 85
Ali -> 85
Sara -> 92
Ahmed -> 78
```

## Comparison

| Feature | C++ `map` | Python `dict` |
|---|---|---|
| Import needed | `#include <map>` | no, built-in |
| Unique keys | yes | yes |
| Repeated values | yes | yes |
| Order | sorted by key | insertion order |
| Access by key | `marks["Ali"]` | `marks["Ali"]` |
| Loop | `for (auto x : marks)` | `for k, v in marks.items()` |

A C++ `map` and a Python `dict` are the same idea. The main difference is order: `map` is sorted, while `dict` keeps insertion order and is closer to C++ `unordered_map`, which is a hash table.

## The `auto` keyword (C++)

`auto` lets the compiler work out the type of a variable.

```cpp
map<string, int> marks = {{"Ali", 85}, {"Sara", 92}};

// Full type written out
for (map<string, int>::iterator it = marks.begin(); it != marks.end(); it++)
    cout << it->first << " -> " << it->second << endl;

// Same loop with auto (type is pair<const string, int>)
for (auto p : marks)
    cout << p.first << " -> " << p.second << endl;
```

## `pair` (C++)

A `pair` (header `<utility>`) holds two values together. Each element of a `map` is a pair of key and value.

```cpp
#include <utility>
pair<string, int> p = {"Ali", 85};
cout << p.first;    // Ali  (the key)
cout << p.second;   // 85   (the value)
```

## The Python loop

```python
for name, score in marks.items():
    print(name, "->", score)
```

- `marks.items()` returns every key–value pair as a tuple, for example `("Ali", 85)`.
- `name, score` unpacks each tuple: `name` gets the key and `score` gets the value.
- The loop runs once for every entry in the dictionary.
