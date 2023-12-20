from Product import Product
from Elementary import Elementary
from Composite import Composite
from Composition import Composition


# Creating Elementary products
elementary_1 = Elementary("Product 1", "E001", 10.0)
elementary_2 = Elementary("Product 2", "E002", 15.0)
elementary_3 = Elementary("Product 3", "E003", 12.0)

# Creating Composite products with Elementary products as constituents
constituents_1 = [elementary_1, elementary_2]
constituents_2 = [elementary_1, elementary_3]

composite_1 = Composite("Composite Product 1", "C001", 20, constituents_1)
composite_2 = Composite("Composite Product 2", "C002", 20, constituents_2)

# Creating Compositions for the Composite instances
composition_1_for_composite_1 = Composition(composite_1, 3)
composition_2_for_composite_2 = Composition(composite_2, 5)

# Displaying information about the created products and compositions
print("Elementary Products:")
print(elementary_1)
print(elementary_2)
print(elementary_3)

print("\nCompositions for Composite Products:")
print(composition_1_for_composite_1)
print(composition_2_for_composite_2)

# Comparisons between compositions
print("\nComparisons:")
print(f"Composition 1 == Composition 2: {composition_1_for_composite_1 == composition_2_for_composite_2}")  # Should be False

# Comparisons between composite products
print(f"Composite 1 == Composite 2: {composite_1 == composite_2}")  # Should be False
