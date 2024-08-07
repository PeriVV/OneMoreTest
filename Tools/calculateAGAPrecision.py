import os
import csv

# 读取文件内容
def read_file(file_path, limit=None):
    with open(file_path, 'r') as file:
        content = file.readlines()
    if limit:
        content = content[:limit]
    return [int(line.strip()) for line in content]

# 计算真阳性（tn）和假阴性（fn）
def calculate_tn_fn(priorities, labels, top_n):
    tn = sum(1 for i in range(top_n) if i < len(labels) and labels[i] == 1)
    fn = sum(1 for i in range(top_n) if i < len(labels) and labels[i] == 0)
    return tn, fn

# 获取文件列表
def get_file_list(directory, suffix):
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(suffix)]

# 处理每对文件
def process_files(label_files, priority_files):
    top_ns = [100, 10, 5, 3, 1]
    all_results = {}

    for label_file in label_files:
        base_name = os.path.basename(label_file).replace('_label.txt', '')
        priority_file = next((pf for pf in priority_files if base_name in pf), None)
        if priority_file:
            # 读取前100个优先级和标签文件
            labels = read_file(label_file, limit=100)
            priorities = read_file(priority_file, limit=100)

            # 排序优先级并获取对应的标签
            sorted_indices = sorted(range(len(priorities)), key=lambda i: priorities[i])
            sorted_labels = [labels[i] for i in sorted_indices if i < len(labels)]

            # 计算不同优先级中的tn和fn
            results = {}
            for top_n in top_ns:
                tn, fn = calculate_tn_fn(priorities, sorted_labels, top_n)
                results[f'tn{top_n}'] = tn
                results[f'fn{top_n}'] = fn

            # 保存结果
            all_results[base_name] = results

    return all_results

# 将结果写入CSV文件
def write_results_to_csv(results, output_file):
    headers = ['project_id', 'tn100', 'fn100', 'tn10', 'fn10', 'tn5', 'fn5', 'tn3', 'fn3', 'tn1', 'fn1']
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        for project_id, result in results.items():
            row = [project_id]
            for key in headers[1:]:
                row.append(result.get(key, 0))
            writer.writerow(row)

# 主函数
def main():
    label_directory = 'labels'
    priority_directory = 'priorities'
    output_file = 'results.csv'

    label_files = get_file_list(label_directory, '_label.txt')
    priority_files = get_file_list(priority_directory, '_priorities.txt')

    results = process_files(label_files, priority_files)

    write_results_to_csv(results, output_file)
    print(f'Results have been written to {output_file}')

if __name__ == '__main__':
    main()
