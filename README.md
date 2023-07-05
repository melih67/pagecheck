# Website Monitoring Tool

This is a simple Python script that monitors a specified URL for changes in its content. It uses the `requests` library to fetch the webpage, `BeautifulSoup` for parsing the HTML, and `hashlib` for generating an MD5 hash of the webpage's content.

## How it Works

1. The script starts by defining three constants:
   - `TOKEN`: Your Telegram bot token.
   - `CHAT_ID`: The chat ID of the Telegram user or group where you want to receive notifications.
   - `URL`: The URL of the website you want to monitor.

2. The `get_page_content()` function sends an HTTP GET request to the specified URL and retrieves the HTML content of the webpage. It uses `BeautifulSoup` to parse the HTML and returns it as a string.

3. The `send_telegram_message()` function sends a message to the specified Telegram chat using the Telegram Bot API. It constructs a URL with the provided `TOKEN`, `CHAT_ID`, and the `message` parameter. The function returns the response in JSON format.

4. The `monitor_website()` function is the main monitoring loop. It initializes an empty string `old_hash` to store the previous MD5 hash of the webpage's content. The function enters an infinite loop where it repeatedly fetches the webpage's content, generates the MD5 hash of the current content, and compares it with the previous hash.

   - If the hashes differ, it means the webpage's content has changed. The function prints a message on the console and sends a customizable message to the specified Telegram chat using the `send_telegram_message()` function. The `message` parameter can be modified to suit your notification needs.

   - If the hashes are the same, the function does nothing.

   - The function waits for 5 seconds before checking the webpage again. You can adjust this delay according to your preference.

5. The script ends by calling the `monitor_website()` function, initiating the monitoring process.

## Getting Started

To use this monitoring tool:

1. Clone the repository and navigate to the project directory.

2. Install the required Python dependencies by running the following command:
  pip install -r requirements.txt


3. Open the script file in a text editor and modify the following constants according to your requirements:
- `TOKEN`: Replace with your Telegram bot token. You can create a new bot and obtain the token from the [BotFather](https://core.telegram.org/bots#botfather).
- `CHAT_ID`: Replace with the chat ID of the Telegram user or group where you want to receive notifications. You can obtain the chat ID by starting a chat with your bot and accessing the following URL: `https://api.telegram.org/bot{TOKEN}/getUpdates`.
- `URL`: Replace with the URL of the website you want to monitor.

4. Save the modifications to the script file.

5. Run the script using the following command:
python script.py


The script will start monitoring the specified webpage and provide console output and Telegram notifications whenever a change is detected.

## Notes

- Ensure that you have a stable internet connection while running the script to avoid any network-related issues.

- Make sure to comply with the terms of service and usage policies of the websites you are monitoring. Some websites may have restrictions on automated access or scraping.

- This script provides a basic example of website monitoring. Depending on your specific requirements, you may need to modify the script to handle more complex scenarios or integrate additional functionality.

- For more information on using the Telegram Bot API, refer to the [official documentation](https://core.telegram.org/bots/api).

