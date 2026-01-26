
docker rm -f server_inst 2>/dev/null
docker network create net_server 2>/dev/null
docker network create net_client 2>/dev/null

docker run -d --name server_inst --network net_server \
  -v "$(pwd)/server_persistent_storage:/server_storage" \
  my_server_img 8080

docker network connect net_client server_inst

echo "Server is UP and connected to both networks."