import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

ler=SimpleMFRC522()

print("bota de novo")

while True:
	id,texto=ler.read()
	print("ID: {}\ntexto: {}".format(id,texto))
	sleep(3)

