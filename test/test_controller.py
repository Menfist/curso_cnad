from src.model.controller import ManageData
from src.model.model import Data


def inset_random():
    import random

    db = ManageData()
    new_data = Data(
        sensor_1=float(str(random.random() * 100)[0:5]),
        sensor_2=float(str(random.random() * 100)[0:5]),
        btn_1=random.choice([1, 0]),
        btn_2=random.choice([1, 0]),
        led_1=random.choice([1, 0]),
        led_2=random.choice([1, 0]),
        modify_by=random.choice(["dashboard", "board"]),
    )

    db.insert_data(new_data)


def read_data():
    db = ManageData()

    data = db.get_last_data()
    print("last: ", data.id)
    print(
        f"data= sensor 1: {data.sensor_1}, sensor 2: {data.sensor_2}, btn1: {data.btn_1}, led 1: {data.led_1}, own: {data.modify_by}"
    )


if __name__ == "__main__":

    for i in range(4):
        inset_random()
