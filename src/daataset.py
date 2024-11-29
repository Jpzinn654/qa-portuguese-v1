from datasets import load_dataset

# Load the dataset from Hugging Face
dataset = load_dataset("ju-resplande/qa-pt")

# Inspect the dataset
print(dataset['train'][0])

# Select the first 500,000 rows
sampled_dataset = dataset["train"].select(range(500000))

# Verify the size
print(f"Number of rows: {len(sampled_dataset)}")

# Save it locally in CSV format
sampled_dataset.to_csv("qa-portuguese-v1.csv")

# Or save it in JSON format
sampled_dataset.to_json("qa-portuguese-v1.json")

