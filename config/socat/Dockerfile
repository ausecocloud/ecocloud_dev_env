# A container running socat ....
# 
# Usage: ... run this container in the network space of a specific container, so that localhost:XX can be forwarded to container:YY

# docker run --name mysql-bridge-a-to-b --net=container:<containerAid> socat socat TCP-LISTEN:3306,fork TCP:BIP:3306

# docker build -t socat .

FROM alpine
RUN apk update && apk add socat
