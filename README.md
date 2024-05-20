#!/bin/bash

# Keylogger Python Script

cat << EOF > README.md
# Keylogger Python Script

This Python script implements a basic keylogger using the \`pynput\` library to monitor and log keystrokes.

## Features

- Records keystrokes in real-time.
- Logs keystrokes to a file (\`keylog.txt\`).
- Stops logging when the \`esc\` key is pressed.

## Prerequisites

- Python 3.x installed on your system.
- Install the \`pynput\` library using pip:
  \`\`\`
  pip install pynput
  \`\`\`

## Usage

1. Clone or download this repository to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the \`keylogger.py\` file.
4. Run the keylogger script:
   \`\`\`
   python keylogger.py
   \`\`\`
5. Press keys on your keyboard to log keystrokes.
6. Press the \`esc\` key to stop logging and exit the script.

## Configuration

- By default, the log file (\`keylog.txt\`) is created in the same directory as the script. You can modify the \`log_file\` variable in the script to change the log file path.

## Disclaimer

- This script is provided for educational purposes only. Be responsible and use it ethically and legally. Do not use this script for malicious purposes.

## License

This project is licensed under the [MIT License](LICENSE).
EOF

echo "README.md file created successfully."
