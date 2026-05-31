import argparse

from src.fifo import Fifo
from src.sstf import Sstf
from src.scan import Scan
from src.c_scan import CScan


class Simulator:
    def __init__(self, initial_position, initial_direction, disk_size, request_queue):
        self.initial_position = initial_position
        self.initial_direction = initial_direction
        self.disk_size = disk_size
        self.request_queue = request_queue

        # create classes and set attributes for each disk scheduling algorithm here
        self.fifo = Fifo(initial_position, initial_direction, disk_size, request_queue)
        self.sstf = Sstf(initial_position, initial_direction, disk_size, request_queue)
        self.scan = Scan(initial_position, initial_direction, disk_size, request_queue)
        self.cscan = CScan(
            initial_position, initial_direction, disk_size, request_queue
        )

    def run(self):

        self.fifo.run()
        self.sstf.run()

        # True for SCAN with look, False for SCAN without look
        self.scan.run(True)
        self.scan.run(False)

        # True for C-SCAN with look, False for C-SCAN without look
        self.cscan.run(True)
        self.cscan.run(False)


def main():

    arg_parser = argparse.ArgumentParser(description="OS Disk Scheduling Algorithms")

    arg_parser.add_argument(
        "-p",
        "--position",
        type=int,
        help="Initial position of the disk head",
        required=True,
        default=0,
    )

    arg_parser.add_argument(
        "-d",
        "--direction",
        type=str,
        help="Initial direction of the disk head (inc or dec)",
        required=True,
        default="inc",
    )

    arg_parser.add_argument(
        "-s",
        "--size",
        type=int,
        help="Size of the disk (number of cylinders)",
        required=True,
        default=199,
    )

    arg_parser.add_argument(
        "-q",
        "--queue",
        type=int,
        nargs="+",
        help="Queue of disk requests (cylinder numbers)",
        required=True,
    )

    parser = arg_parser.parse_args()

    initial_position = parser.position
    initial_direction = parser.direction
    disk_size = parser.size
    request_queue = parser.queue

    simulator = Simulator(
        initial_position=initial_position,
        initial_direction=initial_direction,
        disk_size=disk_size,
        request_queue=request_queue,
    )

    simulator.run()


if __name__ == "__main__":
    main()
