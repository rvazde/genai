import sys
import requests
import json
import dewiki
import re


def error_out(message):
    print(message)
    sys.exit(1)

def requestToApi(search_term):
    url = "https://pt.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "titles": search_term,
        "prop": "extracts",
        "explaintext": True,
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        error_message = f"HTTP error occurred: {http_err}"
    except requests.exceptions.ConnectionError as conn_err:
        error_message = f"Connection error occurred: {conn_err}"
    except requests.exceptions.Timeout as timeout_err:
        error_message = f"Timeout error occurred: {timeout_err}"
    except requests.exceptions.RequestException as req_err:
        error_message = f"An error occurred: {req_err}"
    except json.JSONDecodeError as json_err:
        error_message = f"JSON decode error: {json_err}"
    error_out(error_message)

def processPayload(payload):
    pages = payload.get("query", {}).get("pages", {})
    if not pages:
        error_out("Pages not found.")
    page_content = ""
    for page_id, page in pages.items():
        if "extract" in page:
            page_content = page["extract"]
            cleaned_content = dewiki.from_string(page_content)
            return cleaned_content
    error_out("Content not found on Wikipedia.")
    return page_content

def writeToFile(file_name, content):
    if not content:
        content = "Tente novamente."
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    if len(sys.argv) != 2:
        error_out("Usage: python request_wikipedia.py 'SEARCH_TERM (portuguese)'")

    input_string = sys.argv[1]
    file_name = re.sub(r'\s+', '_', input_string) + ".wiki"

    payload = requestToApi(input_string)
    cleaned_content = processPayload(payload)
    writeToFile(file_name, cleaned_content)

if __name__ == "__main__":
    main()