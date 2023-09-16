import json
import random

# Function to generate fictitious service provider data
def generate_service_provider():
    services = ["Delivery", "Cleaning", "Plumbing", "Electrical", "Landscaping", "Catering", "Car Repair", "Graphic Design", "Tutoring"]

    provider = {
        "name": f"Fictitious {random.choice(services)} Service",
        "location": random.choice(["New York", "Los Angeles", "Chicago", "Miami"]),
        "services_offered": random.sample(services, random.randint(1, len(services))),
        "ratings": round(random.uniform(1, 5), 2),
        "reviews": random.randint(0, 100)
    }

    return provider

# Number of fictitious service providers to generate
num_providers = 10

# Generate and store data in a list
data = [generate_service_provider() for _ in range(num_providers)]

# Define the output JSON file path
output_file = "service_providers.json"

# Write the data to the JSON file
with open(output_file, "w") as file:
    json.dump(data, file, indent=4)

print(f"{num_providers} fictitious service providers data generated and saved to '{output_file}'.")
