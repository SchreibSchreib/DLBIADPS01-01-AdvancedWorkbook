import time
from functools import wraps


def timer(function_to_measure):
    function_to_measure._is_running = False

    @wraps(function_to_measure)
    def measure_time(*args, **kwargs):
        if function_to_measure._is_running:
            return

        function_to_measure.is_running = True
        start_time = time.perf_counter()
        performed_task = function_to_measure(*args, **kwargs)
        end_time = time.perf_counter()
        print(
            f"{function_to_measure.__name__} dauerte {end_time - start_time:.6f} Sekunden"
        )
        function_to_measure.is_running = False
        return performed_task

    return measure_time
