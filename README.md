# Self-Bot Discord Utility

A self-bot built with Python and Discord.py to perform various automated tasks, including message deletion, history management, and more.

## Features

- **Say Command**: Make the bot repeat a message in the same channel.
- **Purge Command**: Delete a specified number of your bot's own messages.
- **History Command**: Fetch and display recent message history in the current channel.
- **User Message History**: Fetch message history from a specific user.
- **Keyword Search**: Search for messages from a user that contain a specific keyword.
- **Snipe**: Retrieve the last deleted message.
- **Spam**: Repeat a message multiple times.
- **Exit**: Shut down the bot.

## Prerequisites

Before running the bot, you will need:

- Python 3.8+
- `discord.py` (Discord API wrapper)
- A Discord token (for the bot to authenticate)
- Owner's Discord user ID

### Python Libraries

Ensure you have the required Python libraries installed. You can install them using the following command:

```bash
pip install discord.py
pip install openai  # Optional, depending on usage
```

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/PedYekt/Python-Discord-self-bot.git
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the Bot:**

    - Open the `main.py` file.
    - Add your Discord bot token in the `TOKEN` variable.
    - Add your user ID in the `OWNER_ID` variable.

4. **Run the Bot:**
   ```bash
   python main.py
   ```

## Bot Commands

| Command | Description |
| ------- | ----------- |
| `~say [message]` | Make the bot repeat a message. |
| `~purge [number]` | Delete up to the specified number of your bot's messages. |
| `~history [limit]` | Fetch the last `[limit]` number of messages in the channel. |
| `~user_his [user_id] [limit]` | Fetch up to `[limit]` messages from a specific user in the channel. |
| `~user_search [user_id] [keyword] [limit]` | Fetch up to `[limit]` messages from a specific user containing the specified keyword. |
| `~snipe` | Retrieve the last deleted message. |
| `~spam [message] [count]` | Spam the specified message a number of times. |
| `~exit` | Shut down the bot. |

## Example Usage

- Send a message:
  ```bash
  ~say Hello, World!
  ```

- Purge 10 messages:
  ```bash
  ~purge 10
  ```

- Get the last 50 messages in the channel:
  ```bash
  ~history 50
  ```

- Retrieve the last 5 messages from a user with ID `1234567890`:
  ```bash
  ~user_his 1234567890 5
  ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Feel free to submit a pull request or open an issue for any suggestions or bug reports.

---

### Disclaimer
This project is a self-bot, which interacts with Discord via your own account. **Self-bots** violate Discord's terms of service and may lead to your account being disabled or banned. Use at your own risk.
