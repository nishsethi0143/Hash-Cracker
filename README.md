# Hash Cracker

A simple Python hash cracker that attempts to recover the plaintext from an MD5, SHA1, or SHA256 hash using a wordlist (dictionary attack).

## Features
- Supports MD5, SHA1, and SHA256 hashes.
- Takes a hash and a wordlist file as input.
- Prints the cracked plaintext if found.

## Usage

1. Clone the repository or download the files.

2. Prepare a wordlist file (`wordlist.txt`) with candidate passwords, one per line.

3. Run the script with:

```bash
python hash_cracker.py <hash> <hash_type> <wordlist>
```

Example:

```bash
python hash_cracker.py 5d41402abc4b2a76b9719d911017c592 md5 wordlist.txt
```

This tries to crack the MD5 hash of "hello".

## Requirements

- Python 3.x

## Notes

- This is a simple educational tool and not optimized for large-scale cracking.
- Use responsibly and ethically.

---

Feel free to contribute or improve the wordlist!
