stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
x = {
    "banana": stock ["banana"] * prices["banana"],
    "apple":stock ["apple"] * prices["apple"],
    "orange": stock["orange"] * prices["orange"],
    "pear":stock["pear"] * prices["pear"]
    }
print(x)