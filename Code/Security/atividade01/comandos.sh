sudo apt-get update
sudo apt-get upgrade

sudo apt-get install python3-scapy bridge-utils tcpdump

#abra 3 terminais

sudo ip netns add Alice
sudo ip netns add Bob
sudo ip netns add Attacker


sudo ip link add br0 type bridge
sudo ip link set br0 up

sudo ip link add veth1 type veth peer name veth1-br
sudo ip link add veth2 type veth peer name veth2-br
sudo ip link add veth3 type veth peer name veth3-br

sudo ip link set veth1 netns Alice
sudo ip link set veth2 netns Bob
sudo ip link set veth3 netns Attacker

sudo ip link set veth1-br master br0
sudo ip link set veth2-br master br0
sudo ip link set veth3-br master br0

sudo ip link set veth1-br up
sudo ip link set veth2-br up
sudo ip link set veth3-br up

sudo brctl setageing br0 0

sudo ip netns exec Alice ip addr add 192.168.1.1/24 dev veth1
sudo ip netns exec Alice ip link set veth1 up

sudo ip netns exec Bob ip addr add 192.168.1.2/24 dev veth2
sudo ip netns exec Bob ip link set veth2 up

sudo ip netns exec Attacker ip addr add 192.168.1.3/24 dev veth3
sudo ip netns exec Attacker ip link set veth3 up