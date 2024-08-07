import os
import heapq
import time
import logging
import argparse


def read_file(filepath):
    """Read the contents of a file and return them as a list of lines."""
    with open(filepath) as f:
        return f.read().splitlines()


def write_sequence_to_file(filename, sequence):
    """Write a sequence of strings to a file, each on a new line."""
    with open(filename, 'w') as f:
        for item in sequence:
            f.write(item + '\n')


def greedy_additional(testlist, coveragelist, total_count, used, has_change, forward_index, inverted_index):
    """Perform greedy additional test case prioritization."""
    additional_order = []
    total_count_backup = total_count[:]
    pass_count = 0
    intermediate_timelist = []

    # Initialize the max-heap
    max_heap = [(-total_count[i], i) for i in range(len(total_count))]
    heapq.heapify(max_heap)

    while max_heap:
        maxvalue, maxindex = heapq.heappop(max_heap)
        maxvalue = -maxvalue  # Convert back to positive value

        if used[maxindex]:
            continue

        if maxvalue == 0:
            pass_count += 1
            thistime = time.time()
            intermediate_timelist.append(thistime)
            total_count = total_count_backup[:]
            has_change = [False] * len(has_change)
            max_heap = [(-total_count[i], i) for i in range(len(total_count))]
            heapq.heapify(max_heap)
            continue

        additional_order.append(testlist[maxindex])
        used[maxindex] = True
        for j in forward_index[maxindex]:
            if not has_change[j]:
                has_change[j] = True
                for k in inverted_index[j]:
                    if not used[k]:
                        total_count[k] -= 1
                        heapq.heappush(max_heap, (-total_count[k], k))

    return additional_order, intermediate_timelist


def process_subject(subject, testlist_path, coverage_path, result_path, time_record_path):
    """Process a single subject for test case prioritization."""
    logging.info(f'Processing subject: {subject}')

    testlist = read_file(testlist_path)
    coveragelist = read_file(coverage_path)

    logging.info(f'Read {len(testlist)} test cases.')
    logging.info(f'Read {len(coveragelist)} coverage lines.')

    start_time = time.time()
    used = [False] * len(coveragelist)

    sloc = 0
    forward_index = []
    for idx, line in enumerate(coveragelist):
        newline = list(map(int, line.strip().split()))
        sloc = max(sloc, max(newline, default=0))
        forward_index.append(newline)

    sloc += 1
    inverted_index = [[] for _ in range(sloc)]
    has_change = [False] * sloc

    logging.info('Building inverted index...')
    for i, line in enumerate(coveragelist):
        for item in map(int, line.strip().split()):
            inverted_index[item].append(i)
        if i % 100000 == 0:
            logging.info(f'Processed {i} lines for inverted index.')

    total_count = [len(ll) for ll in forward_index]
    logging.info('Starting greedy additional test case prioritization...')
    pre_time = time.time() - start_time
    ga_order, intermediate_timelist = greedy_additional(testlist, coveragelist, total_count, used, has_change,
                                                        forward_index, inverted_index)
    prioritize_time = time.time() - start_time - pre_time

    logging.info('Writing final sequence to file...')
    write_sequence_to_file(result_path, ga_order)

    logging.info('Writing time records to file...')
    with open(time_record_path, 'w') as f:
        f.write(f'pre,{pre_time}\n')
        for index, time_point in enumerate(intermediate_timelist):
            f.write(f'{index + 1},{time_point - start_time}\n')
        f.write(f'{len(intermediate_timelist) + 1},{prioritize_time}\n')

    logging.info(f'{subject} is completed!')


def main():
    parser = argparse.ArgumentParser(description='Greedy Additional Test Case Prioritization')
    parser.add_argument('--testlist', type=str, default='testList/testList.txt', help='Path to the test list file')
    parser.add_argument('--coverage', type=str, default='coverage', help='Path to the coverage folder')
    parser.add_argument('--priorities', type=str, default='priorities', help='Path to the priorities folder')
    parser.add_argument('--time', type=str, default='time', help='Path to the time records folder')
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    subjects = [file.split('_lines.txt')[0] for file in os.listdir(args.coverage) if file.endswith('_lines.txt')]

    for subject in subjects:
        result_path = os.path.join(args.priorities, f'{subject}_priorities.txt')
        if os.path.exists(result_path):
            logging.info(f'Skipping {subject} as it has already been processed.')
            continue

        testlist_path = args.testlist
        coverage_path = os.path.join(args.coverage, f'{subject}_lines.txt')
        time_record_path = os.path.join(args.time, f'{subject}_time.txt')

        try:
            process_subject(subject, testlist_path, coverage_path, result_path, time_record_path)
        except Exception as e:
            logging.error(f'Error processing subject {subject}: {e}')


if __name__ == '__main__':
    main()
