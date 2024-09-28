import time

def print_bar(elapsed_time, percentage, arrow, current_iteration, total_iteration):
    eta = elapsed_time / (percentage / 100) - elapsed_time if percentage > 0 else 0
    print(f'\rETA: {eta:.2f}s [{percentage:3}%] [{arrow:<10}] {current_iteration}/{total_iteration} | elapsed time {elapsed_time:.2f}s', end='')
    
def get_arrow(percentage):
    filled_length = int(percentage // 10)
    return (filled_length * '=') + '>'

def ft_progress(a_list):
    init_time = time.time()
    current_iteration = 0
    total_iteration = len(a_list)
    for current_iteration, _ in enumerate(a_list, start=1):
        elapsed_time = time.time() - init_time
        percentage = int((current_iteration / total_iteration) * 100)
        arrow = get_arrow(percentage)
        print_bar(elapsed_time, percentage, arrow, current_iteration, total_iteration)
        yield current_iteration
        current_iteration += 1
