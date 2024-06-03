def read_data_from_file(file_path, offset, length=100):
    """
    Reads data from a file at a given offset.
    
    :param file_path: Path to the file.
    :param offset: Offset in bytes from the start of the file.
    :param length: Number of bytes to read.
    :return: The read data.
    """
    with open(file_path, 'rb') as file:
        file.seek(offset)
        data = file.read(length)
        return data

def print_data(data):
    """
    Print the data in a readable format.
    
    :param data: Data to be printed.
    """
    # Print hex representation
    hex_representation = " ".join(f"{byte:02x}" for byte in data)
    print(f"Hex: {hex_representation}")

    # Print integer values
    #print("Integers:", list(data))

    # Try to decode as ASCII (or another encoding if known)
    #try:
    #    decoded_data = data.decode('ascii', errors='ignore')
    #    print(f"ASCII: {decoded_data}")
    #except Exception as e:
    #    print(f"Error decoding data: {e}")

# Path to the .dat file
file_path = r'C:\Outlive\outlive.dat'
offset = 43644082
chunk_size = 200

# Read and display data at the given offset
data = read_data_from_file(file_path, offset, chunk_size)
print_data(data)
hex_representation = " ".join(f"{byte:02x}" for byte in data)

try:
    with open('output.txt', 'w') as file:
        file.write(str(hex_representation))
except Exception as e:
    print("Error:", e)