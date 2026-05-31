class CScan:
    def __init__(self, initial_position, initial_direction, disk_size, request_queue):
        self.initial_position = initial_position
        self.initial_direction = initial_direction
        self.disk_size = disk_size
        self.request_queue = request_queue.copy()


    def sort_requests(self):
        # Sort the request queue based on the initial direction of the disk head
        if self.initial_direction == "inc":
            self.request_queue = sorted(self.request_queue)
        else:
            self.request_queue = sorted(self.request_queue, reverse=True)

    def split_requests(self, look: bool):
        # Split the request queue
            if self.initial_direction == "inc":
                self.requests_greater_or_equal = [request for request in self.request_queue if request >= self.initial_position]
                if not look:
                    self.requests_greater_or_equal.append(self.disk_size - 1)
                    self.requests_greater_or_equal.append(0)
                self.requests_less_than = [request for request in self.request_queue if request < self.initial_position]
                self.request_queue = self.requests_greater_or_equal + self.requests_less_than
            else:
                self.requests_less_than_or_equal = [request for request in self.request_queue if request <= self.initial_position]
                if not look:
                    self.requests_less_than_or_equal.append(0)
                    self.requests_less_than_or_equal.append(self.disk_size - 1)
                self.requests_greater = [request for request in self.request_queue if request > self.initial_position]
                self.request_queue = self.requests_less_than_or_equal + self.requests_greater

    def calculate_total_head_movement(self):
        # Calculate the total head movement based on the order of requests processed
        total_head_movement = 0
        current_position = self.initial_position

        for request in self.request_queue:
            total_head_movement += abs(request - current_position)
            current_position = request

        return total_head_movement
                

    def run(self, look: bool):
        # Implement the C-SCAN algorithm here
        # If look is True, implement C-SCAN with look-ahead; otherwise, implement without look-ahead
        self.sort_requests()
        self.split_requests(look)
        total_movement = self.calculate_total_head_movement()

        return (self.request_queue, total_movement)


if __name__ == "__main__":
    cscan = CScan(3, "dec", 200, [1, 2, 3, 4])
    cscan.run(False)
