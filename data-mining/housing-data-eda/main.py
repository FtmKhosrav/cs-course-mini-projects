import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from pandas.plotting import scatter_matrix
from google.colab import files

# Upload dataset
uploaded = files.upload()

# Load data
data = pd.read_csv("housing.csv")

# Train-test split
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

data_copy = train_data.copy()

# Extract features
longitude = data_copy["longitude"]
latitude = data_copy["latitude"]
population = data_copy["population"]
median_house_value = data_copy["median_house_value"]

# Scatter plot: location
plt.figure(figsize=(7, 10))
plt.scatter(longitude, latitude, alpha=0.2)
plt.title("Longitude vs Latitude")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()

# Scatter plot: population size
plt.figure(figsize=(7, 10))
plt.scatter(longitude, latitude, s=population / 30, alpha=0.3)
plt.title("Geographical Distribution with Population")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()

# Scatter plot: house value coloring
plt.figure(figsize=(7, 10))
plt.scatter(
    longitude,
    latitude,
    s=population / 30,
    c=median_house_value,
    cmap="jet",
    alpha=0.3
)
plt.title("House Value Distribution")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.colorbar(label="Median House Value")
plt.show()

# Correlation matrix
corr_matrix = data.corr(numeric_only=True)
print(corr_matrix["median_house_value"].sort_values(ascending=False))

# Top features
features = corr_matrix["median_house_value"].abs().sort_values(ascending=False).head(5).index

# Scatter matrix
scatter_matrix(data[features], figsize=(15, 10))
plt.show()

# Income vs House value
data.plot(
    kind="scatter",
    x="median_income",
    y="median_house_value",
    alpha=0.4,
    figsize=(10, 7)
)

plt.title("Median Income vs House Value")
plt.show()
