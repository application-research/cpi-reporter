FROM alpine:latest

# Install bash, jq, python3
RUN apk add --no-cache bash jq python3 py3-pip

ADD requirements.txt /scripts/requirements.txt

# Install required modules
RUN pip3 install -r /scripts/requirements.txt

# Create a directory for our script files
RUN mkdir -p /scripts

# Add the reporter.py and reporter.sh files to the /scripts directory
ADD reporter.py /scripts/reporter.py
ADD reporter.sh /scripts/reporter.sh

# Set permissions to make the script executable
RUN chmod +x /scripts/reporter.sh

# Set the working directory to /scripts
WORKDIR /scripts

# Set the entrypoint to be our bash script
ENTRYPOINT ["/scripts/reporter.sh"]
