from asyncio import new_event_loop

from asvt_course_money.update_loop import update_loop


def example_callback(pulse_value):
    print(pulse_value)


if __name__ == "__main__":
    loop = new_event_loop()
    loop.create_task(update_loop(example_callback, verbose=True))
    loop.run_forever()
