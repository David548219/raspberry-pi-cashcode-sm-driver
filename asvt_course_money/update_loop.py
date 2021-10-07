from asyncio import sleep

import RPi.GPIO as gpio


async def update_loop(callback, *, verbose=False):
    # Initialising counter
    pulse_count = 0

    def pulse(channel):
        nonlocal pulse_count
        pulse_count += 1

    # GPIO setup
    gpio.setmode(gpio.BCM)
    gpio.setup(2, gpio.IN)
    gpio.add_event_detect(2, gpio.RISING, callback=pulse)

    # Update loop
    while True:
        await sleep(0.06)
        if pulse_count == 0:
            continue
        callback(pulse_count)
        if verbose:
            print(f"PULSE {pulse_count}")
        pulse_count = 0
