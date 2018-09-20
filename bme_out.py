import machine, time, bme280
i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(18))
bme = bme280.BME280(i2c=i2c,address=0x76)
while True:
  print("BME280 values:")
  temp,pa,hum = bme.values
  print(temp)
  print(pa)
  print(hum)
  time.sleep_ms(2000)