# This is a Script for executable transfer between machines
# Used like this for encoding : python3 Transfer_tool.py -e backdoor.exe -o backdoor_encoded.b64
# Used like this for decoding : python3 Transfer_tool.py -d backdoor_encoded.b64 -o backdoor_decoded.exe
import base64
import argparse

def encode_file(input_file, output_file):
    try:
        with open(input_file, "rb") as f:
            encoded = base64.b64encode(f.read())
        with open(output_file, "wb") as f:
            f.write(encoded)
        print(f"[+] Encoded '{input_file}' to '{output_file}'")
    except Exception as e:
        print(f"[-] Encoding failed: {e}")

def decode_file(input_file, output_file):
    try:
        with open(input_file, "rb") as f:
            decoded = base64.b64decode(f.read())
        with open(output_file, "wb") as f:
            f.write(decoded)
        print(f"[+] Decoded '{input_file}' to '{output_file}'")
    except Exception as e:
        print(f"[-] Decoding failed: {e}")

def main():
    parser = argparse.ArgumentParser(description="Base64 Encode/Decode Tool for Executables")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-e", "--encode", metavar="FILE", help="Path to input executable to encode")
    group.add_argument("-d", "--decode", metavar="FILE", help="Path to base64-encoded file to decode")
    parser.add_argument("-o", "--output", metavar="OUTPUT", required=True, help="Output file name")

    args = parser.parse_args()

    if args.encode:
        encode_file(args.encode, args.output)
    elif args.decode:
        decode_file(args.decode, args.output)

if __name__ == "__main__":
    main()