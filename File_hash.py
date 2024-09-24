import hashlib, os

def get_file_by_partial_name(partial_name):
    
    matched_files = [file for file in os.listdir() if file.startswith(partial_name)]
    
    if len(matched_files) == 0:
        print(f"No files found starting with '{partial_name}'")
        return None
    elif len(matched_files) == 1:
        return matched_files[0]
    else:
        print(f"Multiple files found starting with '{partial_name}':")
        for i, file in enumerate(matched_files, 1):
            print(f"{i}: {file}")
        choice = int(input("Please select a file by number: ")) - 1
        return matched_files[choice]

def fileHash(file):
    if os.path.isfile(file):
        print(f"\n{file}")
        print(f"MD5 Checksum:    {hashlib.md5(open(f'{file}', 'rb').read()).hexdigest()}")
        print(f"SHA1 Checksum:   {hashlib.sha1(open(f'{file}', 'rb').read()).hexdigest()}")
        print(f"SHA256 Checksum: {hashlib.sha256(open(f'{file}', 'rb').read()).hexdigest()}\n")
    else:
        print(f"The file '{file}' couldn't be found. Please check the spelling.")

if __name__ == "__main__":
    partial_file_name = input("Please enter the file name (or part of it): ")
    file_name = get_file_by_partial_name(partial_file_name)
    if file_name:
        fileHash(file_name)
