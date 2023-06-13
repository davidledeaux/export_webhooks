This will output a CSV file that contains all metadata for configured Rally webhooks, including last fired date, last status, etc.  This can help with making determinations about webhook status and administration decisions.

# Installation
Install requests:

`pip install requests`

# Configuration
Set API key in line 8

# Execution
Run the script:

`python export_webhooks.py`

Output will be webhooks.csv

# Misc
This script is provided without warranty or support.
