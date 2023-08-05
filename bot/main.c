#include <stdio.h>
#include <ctype.h>
#include "pico/stdlib.h"

#include "wizchip_conf.h"
#include "socket.h"
#include "w5x00_spi.h"

typedef union _un_l2cval {
  uint32_t	lVal;
  uint8_t		cVal[4];
}un_l2cval;

un_l2cval remote_ip;
const uint LED_PIN = 25;

static wiz_NetInfo g_net_info =
    {
        .mac = {0x00, 0x08, 0xDC, 0x12, 0x34, 0x56}, // MAC address
        .ip = {192, 168, 86, 2},                     // IP address
        .sn = {255, 255, 255, 0},                    // Subnet Mask
        .gw = {192, 168, 86, 1},                     // Gateway
        .dns = {8, 8, 8, 8},                         // DNS server
        .dhcp = NETINFO_STATIC                       // DHCP enable/disable
};

void init_network();

int main() {
  init_network();
  gpio_init(LED_PIN);
  gpio_set_dir(LED_PIN, GPIO_OUT);
  
  // initialize TCP socket on port 36543
  int socketFD = socket(1, Sn_MR_TCP, 36543, 0x00);
  while (true) {
    int listenResult = listen(socketFD);
    if (connect(socketFD, remote_ip.cVal, 36543) == 1) {
      uint8_t buffer[1024];
      recv(socketFD, buffer, 1024);
      if (buffer[0] == 1) {
        gpio_put(LED_PIN, 1);
      }

      uint8_t message[1024];
      message[0] = 69;
      send(socketFD, message, 1024);

      close(socketFD);
    }
  }
}

// run various initialization functions
void init_network() {stdio_init_all();wizchip_spi_initialize();wizchip_cris_initialize();wizchip_reset();wizchip_initialize();wizchip_check();network_initialize(g_net_info);print_network_information(g_net_info);}