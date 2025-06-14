# Metaclass that enforces class names to be in CamelCase (start with capital letter)
class NamingConventionMeta(type):
    def __new__(metacls, name, bases, namespace):
        if not name[0].isupper():
            raise ValueError(f"Class name '{name}' must start with an uppercase letter.")
        return super().__new__(metacls, name, bases, namespace)

# Valid class
class ValidName(metaclass=NamingConventionMeta):
    pass

# Invalid class — uncomment to test the enforcement
# class invalidName(metaclass=NamingConventionMeta):
#     pass
