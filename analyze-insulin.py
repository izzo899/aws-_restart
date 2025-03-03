# Read the cleaned sequence from the file
with open("preproinsulin-seq-clean.txt", "r") as file:  # Replace with your actual filename
    cleaned_data = file.read().strip()  # Remove any extra whitespace or newlines

# Define sequence ranges and expected lengths
ranges = {
    "lsinsulin-seq-clean.txt": (0, 24, 24),  # Amino acids 1–24
    "binsulin-seq-clean.txt": (24, 54, 30),  # Amino acids 25–54
    "cinsulin-seq-clean.txt": (54, 89, 35),  # Amino acids 55–89
    "ainsulin-seq-clean.txt": (89, 110, 21), # Amino acids 90–110
}

# Process each range and save to respective file
for filename, (start, end, expected_length) in ranges.items():
    segment = cleaned_data[start:end]  # Extract required sequence

    # Verify length
    if len(segment) == expected_length:
        print(f"{filename}: ✅ Correct length ({expected_length} characters).")
    else:
        print(f"{filename}: ❌ Incorrect length ({len(segment)} characters, expected {expected_length}).")
        # Save to file
    with open(filename, "w") as output_file:
        output_file.write(segment)