import numpy as np
import pandas as pd

series1 = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])

print(series1)

series2 = pd.Series(np.random.randn(5))

print(series2)

dictionary = {
    "a": 1,
    "b": 2,
    "c": 3
}

series_from_dictionary = pd.Series(dictionary)

print(series_from_dictionary)

series_from_dictionary_with_custom_index = pd.Series(dictionary, ["x", "y", "z"])

print(series_from_dictionary_with_custom_index)

series_from_scalar_value = pd.Series(5, index=["a", "b", "c", "d", "e"])

print(series_from_scalar_value)

# slicing
print("Slicing...")
print(series1.iloc[1:3])

print("Getting median...")
print(series1.median())
print(series1[series1 > series1.median()])

print("Getting selected items from the series...")
print(series1.iloc[[4, 2, 0]])

print(f"Data Type of the series is {series1.dtype}")

print(series1.to_numpy())

print(series1["a"])

series1["e"] = 2
print(series1)

print("e" in series1)
print("f" in series1)
print(series1.get("e"))

# Vector operations with series
print(series1 + series1)
print(series1 - series1)
print(np.exp(series1))

print(series1[:1] + series1[:1])

series_with_a_name = pd.Series(["a", "b", "c", "d", "e"], [0, 1, 2, 3, 4], name="characters")
print(series_with_a_name.name)

copy_of_series1 = series1.copy()
print(copy_of_series1)