import hashlib
import sys

def crack_hash(hash_to_crack, hash_type, wordlist_path):
    try:
        with open(wordlist_path, 'r', encoding='utf-8') as f:
            for word in f:
                word = word.strip()
                if not word:
                    continue
                hashed_word = ""
                if hash_type == 'md5':
                    hashed_word = hashlib.md5(word.encode()).hexdigest()
                elif hash_type == 'sha1':
                    hashed_word = hashlib.sha1(word.encode()).hexdigest()
                elif hash_type == 'sha256':
                    hashed_word = hashlib.sha256(word.encode()).hexdigest()
                elif hash_type == 'sha224':
                    hashed_word = hashlib.sha224(word.encode()).hexdigest()
                elif hash_type == 'sha384':
                    hashed_word = hashlib.sha384(word.encode()).hexdigest()
                elif hash_type == 'sha512':
                    hashed_word = hashlib.sha512(word.encode()).hexdigest()
                elif hash_type == 'blake2b':
                    hashed_word = hashlib.blake2b(word.encode()).hexdigest()
                elif hash_type == 'blake2s':
                    hashed_word = hashlib.blake2s(word.encode()).hexdigest()
                elif hash_type == 'sha3_224':
                    hashed_word = hashlib.sha3_224(word.encode()).hexdigest()
                elif hash_type == 'sha3_256':
                    hashed_word = hashlib.sha3_256(word.encode()).hexdigest()
                elif hash_type == 'sha3_384':
                    hashed_word = hashlib.sha3_384(word.encode()).hexdigest()
                elif hash_type == 'sha3_512':
                    hashed_word = hashlib.sha3_512(word.encode()).hexdigest()
                else:
                    print(f"[!] Unsupported hash type: {hash_type}")
                    return

                if hashed_word == hash_to_crack.lower():
                    print(f"[+] Hash cracked! The plaintext is: '{word}'")
                    return
        print("[-] Sorry, password not found in wordlist.")
    except FileNotFoundError:
        print(f"[!] Wordlist file '{wordlist_path}' not found.")
    except Exception as e:
        print(f"[!] An error occurred: {e}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python hash_cracker.py <hash> <hash_type> <wordlist>")
        print("Example: python hash_cracker.py 5d41402abc4b2a76b9719d911017c592 md5 wordlist.txt")
        print("Supported hash types: md5, sha1, sha256, sha224, sha384, sha512, blake2b, blake2s, sha3_224, sha3_256, sha3_384, sha3_512")
        return

    hash_to_crack = sys.argv[1]
    hash_type = sys.argv[2].lower()
    wordlist_path = sys.argv[3]

    print(f"[*] Starting to crack hash: {hash_to_crack} (Type: {hash_type})")
    crack_hash(hash_to_crack, hash_type, wordlist_path)

if __name__ == "__main__":
    main()