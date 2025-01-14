import json

# Load the JSON data from the file
with open('/home/anjali/Bayut/Bayut/data.json', encoding='utf-8', errors='surrogatepass') as f:
    data = json.load(f)

# Process the data
formatted_data = []
for row in data:
    formatted_row = {
        'property_id': row['property_id'],
        'purpose': row['purpose'],
        'type': row['type'],
        'added_on': row['added_on'],
        'furnishing': row['furnishing'],
        'price': {
            'currency': row['price']['currency'],
            'amount': row['price']['amount']
        },
        'location': row['location'],
        'bed_bath_size': {
            'beds': row['bed_bath_size']['beds'],
            'baths': row['bed_bath_size']['baths'],
            'sqft': row['bed_bath_size']['sqft']
        },
        'permit_number': row['permit_number'],
        'agent_name': row['agent_name'],
        'primary_image_url': row['primary_image_url'],
        'breadcrumbs': row['breadcrumbs'],
        'amenities': row['amenities'],
        'description': row['description'],
        'property_image_urls': row['property_image_urls']
    }
    formatted_data.append(formatted_row)

# Write the formatted data to a new JSON file
with open('formatted_data.json', 'w', encoding='utf-8') as f:
    json.dump(formatted_data, f, indent=4, ensure_ascii=False)