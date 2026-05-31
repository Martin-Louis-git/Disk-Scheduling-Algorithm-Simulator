import argparse
import matplotlib.pyplot as plt

from src.fcfs import Fcfs
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
        self.fcfs = Fcfs(initial_position, initial_direction, disk_size, request_queue)
        self.sstf = Sstf(initial_position, initial_direction, disk_size, request_queue)
        self.scan = Scan(initial_position, initial_direction, disk_size, request_queue)
        self.cscan = CScan(
            initial_position, initial_direction, disk_size, request_queue
        )

    def run(self):

        fcfs_result = self.fcfs.run()
        # sstf_service_array, sstf_total_seek_distance = self.sstf.run()

        # True for SCAN with look, False for SCAN without look

        scan_service_array_no_look, scan_total_seek_distance_no_look = self.scan.run(
            False
        )
        scan_service_array_with_look, scan_total_seek_distance_with_look = (
            self.scan.run(True)
        )

        # True for C-SCAN with look, False for C-SCAN without look

        # cscan_service_array_no_look, cscan_total_seek_distance_no_look = self.cscan.run(
        #     False
        # )
        # cscan_service_array_with_look, cscan_total_seek_distance_with_look = (
        #     self.cscan.run(True)
        # )

        self.__plot_movement(
            {
                "FCFS": fcfs_result["service_order"],
                # "SSTF", self.initial_position, sstf_service_array,
                "SCAN (No Look)": scan_service_array_no_look,
                "SCAN (With Look)": scan_service_array_with_look,
                # "C-SCAN (No Look)", self.initial_position, cscan_service_array_no_look,
                # "C-SCAN (With Look)", self.initial_position, cscan_service_array_with_look,
            },
            self.initial_position,
        )

        self.__plot_seek_comparison(
            {
                "FCFS": fcfs_result["total_seek_distance"],
                "SCAN (No Look)": scan_total_seek_distance_no_look,
                "SCAN (With Look)": scan_total_seek_distance_with_look,
            }
        )

    def __plot_movement(self, all_results, initial_position):
        plt.figure()

        for algorithm_name, served_order in all_results.items():
            positions = [initial_position] + served_order
            steps = list(range(len(positions)))

            plt.plot(steps, positions, marker="o", label=algorithm_name)

        plt.title("Disk Arm Movement Over Time")
        plt.xlabel("Step")
        plt.ylabel("Cylinder Position")
        plt.grid(True)
        plt.legend()

        plt.show()

    def __plot_seek_comparison(self, results):
        algorithms = list(results.keys())
        seeks = list(results.values())

        plt.figure()
        plt.bar(algorithms, seeks)
        plt.title("Total Seek Distance Comparison")
        plt.xlabel("Algorithm")
        plt.ylabel("Total Seek Distance")


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
