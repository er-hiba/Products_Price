from Product import Product
from Elementary import Elementary
from Composite import Composite
from Composition import Composition


# Creating Elementary products
elementary_1 = Elementary("Product 1", "E001", 10.0)
elementary_2 = Elementary("Product 2", "E002", 15.0)
elementary_3 = Elementary("Product 3", "E003", 12.0)

# Creating Compositions for the Composite instances
compo_1 = Composition(elementary_1, 3)
compo_2 = Composition(elementary_2, 5)

# Creating Composite products
constituents = [compo_1, compo_2]
composite_1 = Composite("Product 4", "C001", 20, constituents)

# Displaying information about the created products
print("Elementary Products:")
print(elementary_1)
print(elementary_2)
print(elementary_3)

print("\nComposite Product:")
print(composite_1)
