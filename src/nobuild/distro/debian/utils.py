import hashlib

def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()
    
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    
    return sha256_hash.hexdigest()

def dump_filename(text: str, **kwargs):
    return text.replace("${name}", kwargs["name"]).replace("${version}", kwargs["version"]).replace("${arch}", kwargs["arch"])