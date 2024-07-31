import copy

class A:

    def __init__(self, b: str) -> None:
        self.b = b

    def __str__(self) -> str:
        return self.b
    
    def __repr__(self) -> str:
        return self.b


hallo = [A("test"), A("test2")]

print(hallo)

hallo1 = hallo.copy()
hallo2 = copy.copy(hallo)
hallo3 = copy.deepcopy(hallo)

hallo[0].b = "nix test"

print(f"hallo: {hallo}")
print(f"hallo1: {hallo1}")
print(f"hallo2: {hallo2}")
print(f"hallo3: {hallo3}")

hallo[0].test = "kldj"

print(hallo[0].test)