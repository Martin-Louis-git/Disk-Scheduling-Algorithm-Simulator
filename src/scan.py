class Scan:
    def __init__(
        self, initial_position, initial_direction, disk_size, request_queue, logger=None
    ):
        self.initial_position = initial_position
        self.initial_direction = initial_direction
        self.disk_size = disk_size
        self.request_queue = request_queue
        self.logger = logger

    def run(self, look: bool):

        current_position = self.initial_position
        direction = self.initial_direction
        disk_size = self.disk_size
        request_queue = self.request_queue.copy()
        total_steps = 0
        order_of_service = []

        while request_queue:
            max_request = max(request_queue) if look else disk_size - 1
            min_request = min(request_queue) if look else 0

            if direction == "inc":
                # find the next request in the increasing direction
                next_request = min(
                    (r for r in request_queue if r >= current_position),
                    default=None,
                )

                if next_request is None:
                    if not look:
                        total_steps += abs(current_position - max_request)
                        current_position = max_request
                    direction = "dec"
                    continue

                total_steps += abs(current_position - next_request)
                current_position = next_request
                request_queue.remove(next_request)
                order_of_service.append(next_request)

            else:
                # find the next request in the decreasing direction
                next_request = max(
                    (r for r in request_queue if r <= current_position),
                    default=None,
                )

                if next_request is None:
                    if not look:
                        total_steps += abs(current_position - min_request)
                        current_position = min_request
                    direction = "inc"
                    continue

                total_steps += abs(current_position - next_request)
                current_position = next_request
                request_queue.remove(next_request)
                order_of_service.append(next_request)

        if self.logger:
            self.logger.info(
                f"SCAN {'with look' if look else 'without look'}: Total steps = {total_steps}"
            )
            self.logger.info(f"Order of service: {order_of_service}")

        return order_of_service, total_steps
