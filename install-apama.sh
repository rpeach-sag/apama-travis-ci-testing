wget https://downloads.apamacommunity.com/apama/10.2.0.1/apama_10.2.0.1_amd64_linux.zip  -O /tmp/apama.zip
unzip /tmp/apama.zip -d /tmp/
expect -f ./scripts/install-apama-prompts.sh