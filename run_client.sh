
SERVER_IP=$(docker inspect -f '{{.NetworkSettings.Networks.net_client.IPAddress}}' server_inst)

if [ -z "$SERVER_IP" ]; then
    echo "Error: Could not find Server IP."
    exit 1
fi

docker run --rm \
  --name client_inst \
  --network net_client \
  -v $(pwd)/client_persistent_storage:/client_storage \
  my_client_img $SERVER_IP 8080

echo "Transfer complete!"