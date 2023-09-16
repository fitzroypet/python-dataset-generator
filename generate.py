import json
import random

# Function to generate fictitious service provider data
def generate_service_provider():
    categories = ["Cleaning", "Delivery", "Shopping"]

    provider = {
        "name": f"Fictitious {random.choice(categories)} Service",
        "location": random.choice(["New York", "Los Angeles", "Chicago", "Miami"]),
        "services_offered": {
            "Cleaning": ["House Cleaning", "Carpet Cleaning", "Window Cleaning"],
            "Delivery": ["Food Delivery", "Package Delivery", "Grocery Delivery"],
            "Shopping": ["Personal Shopping", "Grocery Shopping", "Clothing Shopping"]
        }.get(random.choice(categories)),
        "ratings": round(random.uniform(1, 5), 2),
        "reviews": random.randint(0, 100)
    }

    return provider

# Number of fictitious service providers to generate
num_providers = 100

# Generate and store data in a list
data = [generate_service_provider() for _ in range(num_providers)]

# Define the output JSON file path
output_file = "service_providers.json"

# Write the data to the JSON file
with open(output_file, "w") as file:
    json.dump(data, file, indent=4)

print(f"{num_providers} fictitious service providers data generated and saved to '{output_file}'.")
