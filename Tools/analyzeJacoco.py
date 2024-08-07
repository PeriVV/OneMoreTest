import csv
import xml.etree.ElementTree as ET
import os

def get_method_range(xml_file, class_name, method_name):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    method_start_line = None
    method_end_line = None
    found_method = False

    # 查找指定的类
    for package in root.findall('package'):
        for class_ in package.findall('class'):
            if class_.get('name') == class_name.replace('.', '/'):
                # 查找指定的方法并获取方法的起始行
                methods = class_.findall('method')
                for i, method in enumerate(methods):
                    if method.get('name') == method_name:
                        method_start_line = int(method.get('line'))
                        found_method = True
                        # 获取下一个方法的起始行作为当前方法的结束行
                        if i + 1 < len(methods):
                            method_end_line = int(methods[i + 1].get('line')) - 1
                        break
                if found_method and not method_end_line:
                    # 如果没有下一个方法，则使用类的最后一行作为结束行
                    for line in class_.findall('line'):
                        line_nr = int(line.get('nr'))
                        method_end_line = max(method_end_line or line_nr, line_nr)
                    break

    return method_start_line, method_end_line

def get_covered_lines_for_method(xml_file, sourcefile_name, method_start_line, method_end_line):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    covered_lines = []

    # 查找指定的 sourcefile
    for package in root.findall('package'):
        for sourcefile in package.findall('sourcefile'):
            if sourcefile.get('name') == sourcefile_name:
                # 查找所有覆盖的行
                for line in sourcefile.findall('line'):
                    line_nr = int(line.get('nr'))
                    if method_start_line <= line_nr <= method_end_line and int(line.get('ci')) > 0:  # 只记录覆盖的行
                        covered_lines.append(line_nr)

    return covered_lines

def write_covered_lines_to_file_one_line(covered_lines, output_file):
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w') as f:
        f.write(' '.join(map(str, covered_lines)))

# 读取 CSV 文件并处理每一行
csv_file = 'projects/MathTestMethod.csv'
xml_file = 'jacocoXml/jacoco.xml'

with open(csv_file, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        project_name, class_name, method_name = row
        sourcefile_name = class_name.split('.')[-1] + '.java'
        output_file = f'coverage/{project_name}_lines.txt'

        # 获取方法的起始和结束行号
        method_start_line, method_end_line = get_method_range(xml_file, class_name, method_name)

        if method_start_line and method_end_line:
            print(f"{method_name} 方法的起始行号: {method_start_line}")
            print(f"{method_name} 方法的结束行号: {method_end_line}")

            # 获取方法范围内的覆盖行号
            covered_lines = get_covered_lines_for_method(xml_file, sourcefile_name, method_start_line, method_end_line)
            print(f"{sourcefile_name} 文件中 {method_name} 方法的覆盖行号: {covered_lines}")

            # 将覆盖行号以空格分隔的单行格式写入文件
            write_covered_lines_to_file_one_line(covered_lines, output_file)
            print(f"覆盖行号已写入 {output_file}（单行）")
        else:
            print(f"未找到 {class_name} 类中的 {method_name} 方法")
