from copy import deepcopy


class Fcfs:
    def __init__(self, initial_position, initial_direction, disk_size, request_queue):
        self.initial_position = initial_position
        self.initial_direction = initial_direction
        self.disk_size = disk_size
        self.request_queue = request_queue

    def run(self):
        request_queue = deepcopy(self.request_queue)
        self._validate_input(request_queue)

        service_order = request_queue
        movement_path = [self.initial_position] + service_order
        total_seek_distance = self._calculate_total_seek_distance(movement_path)

        print("Running FCFS algorithm...")
        print(f"Service order: {service_order}")
        print(f"Movement path: {movement_path}")
        print(f"Total seek distance: {total_seek_distance}")

        return {
            "algorithm": "FCFS",
            "service_order": service_order,
            "movement_path": movement_path,
            "total_seek_distance": total_seek_distance,
        }

    def _validate_input(self, request_queue):
        if self.disk_size < 0:
            raise ValueError("Disk size must be non-negative.")

        if self.initial_direction not in ("inc", "dec"):
            raise ValueError("Initial direction must be 'inc' or 'dec'.")

        if not 0 <= self.initial_position <= self.disk_size:
            raise ValueError(
                f"Initial position must be between 0 and {self.disk_size}."
            )

        for request in request_queue:
            if not 0 <= request <= self.disk_size:
                raise ValueError(
                    f"Request {request} is outside the valid cylinder range "
                    f"0 to {self.disk_size}."
                )

    def _calculate_total_seek_distance(self, movement_path):
        total = 0

        for current_position, next_position in zip(movement_path, movement_path[1:]):
            total += abs(next_position - current_position)

        return total
