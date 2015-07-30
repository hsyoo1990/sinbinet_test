# 가스센서(MQ-7)를  이용한 SPI 통신

### SPI Setting
라즈베리파이는 기본적으로 SPI 통신이 활성화 되어 있지 않아, 설정 파일을 수정하여 두 기능을 블랙 리스트로 부터 제거  
```sh
$ sudo nano /etc/modeprobe.d/raspi-blacklist.conf
```
 - **#blacklist spi-bcm2708**
 - **'#'으로 SPI를 블랙리스트에서 코멘트아웃하여 제거**


### SPI 드라이브 로드
    $ gpio load spi

### Sample Code ( C )
```sh
$ sudo nano spi-test.c
```
```java
#include <stdio.h> 
#include <string.h>
#include <errno.h>
#include <wiringPi.h>
#include <wiringPiSPI.h>

#define CS_MCP3208  6        // BCM_GPIO 25
#define SPI_CHANNEL 0
#define SPI_SPEED   1000000  // 1MHz


int read_mcp3208_adc(unsigned char adcChannel)
{
  unsigned char buff[3];
  int adcValue = 0;

  buff[0] = 0x06 | ((adcChannel & 0x07) >> 2);
  buff[1] = ((adcChannel & 0x07) << 6);
  buff[2] = 0x00;

  digitalWrite(CS_MCP3208, 0);  // Low : CS Active

  wiringPiSPIDataRW(SPI_CHANNEL, buff, 3);

  buff[1] = 0x0F & buff[1];
  adcValue = ( buff[1] << 8) | buff[2];

  digitalWrite(CS_MCP3208, 1);  // High : CS Inactive

  return adcValue;
}


int main (void)
{
  int adcChannel = 0;
  int adcValue   = 0;

  if(wiringPiSetup() == -1)
  {
    fprintf (stdout, "Unable to start wiringPi: %s\n", strerror(errno));
    return 1 ;
  }

  if(wiringPiSPISetup(SPI_CHANNEL, SPI_SPEED) == -1)
  {
    fprintf (stdout, "wiringPiSPISetup Failed: %s\n", strerror(errno));
    return 1 ;
  }

  pinMode(CS_MCP3208, OUTPUT);

  while(1)
  {
    adcValue = read_mcp3208_adc(adcChannel);
    printf("adc0 Value = %u\n", adcValue);
  }

  return 0;
}    
```

### 컴파일 
    $ gcc -o spi-test spi-test.c -lwiringPi
    
### 프로그램 실행
    $ sudo ./spi-test
