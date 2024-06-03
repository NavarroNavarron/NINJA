from alive_progress import alive_bar, config_handler

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

config_handler.set_global(length=50)

# Example: Assuming we want to read multiple chunks for the demonstration
total_chunks = 10

try:
    with alive_bar(total_chunks, title="Reading data...") as bar:
        for i in range(total_chunks):
            # Adjust offset for each chunk
            chunk_offset = offset + i * chunk_size
            data = read_data_from_file(file_path, chunk_offset, chunk_size)
            print_data(data)
            hex_representation = " ".join(f"{byte:02x}" for byte in data)
            with open('output.txt', 'a') as file:  # Append to the file
                file.write(str(hex_representation) + "\n")
            bar()  # Update the progress bar
except Exception as e:
    print("Error:", e)
