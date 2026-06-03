import argparse
import logging
import matplotlib.pyplot as plt

from src.fcfs import Fcfs
from src.sstf import Sstf
from src.scan import Scan
from src.c_scan import CScan
from src.lstf import Lstf
from src.teleport import Teleport


class Simulator:
    def __init__(self, initial_position, initial_direction, disk_size, request_queue):
        self.initial_position = initial_position
        self.initial_direction = initial_direction
        self.disk_size = disk_size
        self.request_queue = request_queue

        logging.basicConfig(
            level=logging.WARNING,
            format="%(levelname)s | %(name)s | %(message)s",
        )

        logging.getLogger("matplotlib").propagate = False

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        # create classes and set attributes for each disk scheduling algorithm and logger here
        self.fcfs = Fcfs(
            initial_position,
            initial_direction,
            disk_size,
            request_queue,
            logger=self.logger,
        )
        self.sstf = Sstf(
            initial_position,
            initial_direction,
            disk_size,
            request_queue,
            logger=self.logger,
        )
        self.scan = Scan(
            initial_position,
            initial_direction,
            disk_size,
            request_queue,
            logger=self.logger,
        )
        self.cscan = CScan(
            initial_position,
            initial_direction,
            disk_size,
            request_queue,
            logger=self.logger,
        )
        self.lstf = Lstf(
            initial_position,
            initial_direction,
            disk_size,
            request_queue,
            logger=self.logger,
        )
        self.teleport = Teleport(
            initial_position,
            initial_direction,
            disk_size,
            request_queue,
            logger=self.logger,
        )

    def run(self):
        self.logger.info(
            f"Starting simulation | head: {self.initial_position} | direction: {self.initial_direction} | disk size: {self.disk_size}"
        )
        self.logger.debug(f"Request queue: {self.request_queue}")

        fcfs_service_array, fcfs_total_seek_distance = self.fcfs.run()

        sstf_service_array, sstf_total_seek_distance = self.sstf.run()

        scan_service_array_no_look, scan_total_seek_distance_no_look = self.scan.run(
            False
        )

        scan_service_array_with_look, scan_total_seek_distance_with_look = (
            self.scan.run(True)
        )

        cscan_service_array_no_look, cscan_total_seek_distance_no_look = self.cscan.run(
            False
        )

        cscan_service_array_with_look, cscan_total_seek_distance_with_look = (
            self.cscan.run(True)
        )

        lstf_service_array, lstf_total_seek_distance = self.lstf.run()

        teleport_service_array, teleport_total_steps = self.teleport.run()

        self.__plot_movement({"FCFS": fcfs_service_array}, self.initial_position)
        self.__plot_movement({"SSTF": sstf_service_array}, self.initial_position)
        self.__plot_movement(
            {"SCAN (No Look)": scan_service_array_no_look}, self.initial_position
        )
        self.__plot_movement(
            {"SCAN (With Look)": scan_service_array_with_look}, self.initial_position
        )
        self.__plot_movement(
            {"C-SCAN (No Look)": cscan_service_array_no_look}, self.initial_position
        )
        self.__plot_movement(
            {"C-SCAN (With Look)": cscan_service_array_with_look}, self.initial_position
        )
        self.__plot_movement({"LSTF": lstf_service_array}, self.initial_position)
        self.__plot_movement(
            {"Teleport": teleport_service_array}, self.initial_position
        )

        self.__plot_seek_comparison(
            {
                "FCFS": fcfs_total_seek_distance,
                "SSTF": sstf_total_seek_distance,
                "SCAN (No Look)": scan_total_seek_distance_no_look,
                "SCAN (With Look)": scan_total_seek_distance_with_look,
                "C-SCAN (No Look)": cscan_total_seek_distance_no_look,
                "C-SCAN (With Look)": cscan_total_seek_distance_with_look,
                "LSTF": lstf_total_seek_distance,
                "Teleport": teleport_total_steps,
            }
        )

    def __plot_movement(self, result, initial_position):
        plt.figure()

        algorithm_name, served_order = list(result.keys())[0], list(result.values())[0]
        positions = [initial_position] + served_order
        steps = list(range(len(positions)))
        if str(algorithm_name) == "Teleport":
            plt.scatter(steps, positions, marker="o", label=algorithm_name)
        else:
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
        default=200,
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
