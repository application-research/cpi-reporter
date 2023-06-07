#!/bin/bash

# Check if the GITEA_API_KEY environment variable is set
if [[ -z "${GITEA_API_KEY}" ]]; then
  echo "Error: GITEA_API_KEY environment variable is not set."
  exit 1
fi

# Check if /storage/ has the file .mounted in it
if [[ ! -e /storage/.mounted ]]; then
  echo "Error: /storage/.mounted file does not exist."
  exit 1
fi

# If the above checks pass, run reporter.py and pipe the results into /storage/report.json in one atomic write
if python3 reporter.py | jq . > /storage/report_temp.json && mv /storage/report_temp.json /storage/report.json; then
  echo "Success: reporter.py output has been successfully written to /storage/report.json."
  exit 0
else
  echo "Error: Failed to write reporter.py output to /storage/report.json."
  exit 1
fi
