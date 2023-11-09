import hashlib

# Function to calculate MD5 hash


def calculate_md5(data):
    md5_hash = hashlib.md5()
    md5_hash.update(data.encode('utf-8'))
    return md5_hash.hexdigest()


# Original data
original_data = "Hello,world!"

# Calculate MD5 hash of the original data
md5_digest = calculate_md5(original_data)

# Simulate data transmission and storage
# In a real scenario, this is where data might be transmitted and stored

# Verify data integrity
received_data = "Hello,world!"  # Simulated received data
received_md5_digest = calculate_md5(received_data)

if md5_digest == received_md5_digest:
    print("Data integrity verified: The data has not been tampered with.")
else:
    print("Data integrity check failed: The data has been tampered with.")
print("Original MD5 Digest:", md5_digest)
print("Received MD5 Digest:", received_md5_digest)
