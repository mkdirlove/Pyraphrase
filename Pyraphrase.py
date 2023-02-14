import json
import argparse
import requests

# Fancy banner
banner = """
╔═╗╦ ╦╦═╗╔═╗╔═╗╦ ╦╦═╗╔═╗╔═╗╔═╗
╠═╝╚╦╝╠╦╝╠═╣╠═╝╠═╣╠╦╝╠═╣╚═╗║╣
╩   ╩ ╩╚═╩ ╩╩  ╩ ╩╩╚═╩ ╩╚═╝╚═╝
"""

# Custom function to check if an argument is empty
def check_not_empty(value):
    if not value:
        raise argparse.ArgumentTypeError("Value cannot be empty.")
    return value

print(banner)
# Create the argument parser
parser = argparse.ArgumentParser(description='Pyraphrase - Paraphrase text using the Paraphrase Genius API')

# Add the arguments with the custom check
parser.add_argument('-t', '--text', type=check_not_empty, help='the text to paraphrase')
parser.add_argument('-f', '--file', type=argparse.FileType('r'), help='the input file to read text from')
parser.add_argument('-r', '--result_type', type=str, default='single', help='the type of result to return (single or multiple)')
parser.add_argument('-o', '--output', type=str, default=None, help='the output file to save the results to')

# Parse the arguments
args = parser.parse_args()

# Check if --text or --file was specified
if not args.text and not args.file:
    parser.print_help()
    parser.exit()

# Check that only one of --text and --file was specified
if args.text and args.file:
    parser.error("Only one of --text and --file can be specified.")

# Set up the input text from --text or --file
if args.text:
    input_text = args.text
else:
    input_text = args.file.read()

# Set up the request payload
payload = {
        "text": input_text,
        "result_type": args.result_type
}

# Set up the request headers
headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "PUT_YOUR_API_KEY_HERE",
        "X-RapidAPI-Host": "paraphrase-genius.p.rapidapi.com"
}

# Make the API request
response = requests.post("https://paraphrase-genius.p.rapidapi.com/dev/paraphrase/", json=payload, headers=headers)

# Convert the response to a JSON object
response_json = json.loads(response.text)

# Print or save the results in JSON format
if args.output:
        with open(args.output, 'w') as f:
                f.write(response_json["message"])
else:
        print(response_json["message"])
