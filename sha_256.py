import hashlib

# Function to calculate the SHA-256 hash of a message


def calculate_sha256_hash(message):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(message.encode('utf-8'))
    return sha256_hash.hexdigest()

# Function to verify the authenticity of data


def verify_data_integrity(original_message, provided_hash):
    # Calculate the SHA-256 hash of the original message
    calculated_hash = calculate_sha256_hash(original_message)

    # Compare the calculated hash with the provided hash
    if calculated_hash == provided_hash:
        print("Data is authentic. Hash matches.")
    else:
        print("Data has been tampered with. Hash does not match.")


# Define the original message
original_message = "This is a sample message for SHA-256 hashing"

# Calculate and display the SHA-256 hash of the original message
calculated_hash = calculate_sha256_hash(original_message)
print("Calculated Hash:", calculated_hash)

# Simulate data transfer or storage
# In a real scenario, this is where you'd save or transmit the original message and the hash.

# Verify the authenticity of the data
# In a real scenario, you'd retrieve the original message and the provided hash from storage or transmission.
provided_hash = calculated_hash  # Simulating the provided hash for verification
received_data = "This is a sample message for SHA-256 hashing."
verify_data_integrity(received_data, provided_hash)
