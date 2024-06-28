import re

def convert_text_group(question, choices, correct_answers):
    formatted_text = f"{question}\n[Choice#multi#\n"

    for choice in choices:
        if choice[0] in correct_answers:
            formatted_text += f"* {choice[3:]}\n"
        else:
            formatted_text += f"- {choice[3:]}\n"

    formatted_text += "]"

    return formatted_text


def convert_text(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    groups = []
    current_group = {}

    for line in lines:
        line = line.strip()

        if line.startswith('正确答案为：'):
            correct_answers = re.findall(r'[A-D]', line)
            current_group['correct_answers'] = correct_answers
        elif line.startswith('本小题得分：'):
            groups.append(current_group)
            current_group = {}
        elif re.match(r'\d+\.', line):
            current_group['question'] = line
        elif line.startswith(('A)', 'B)', 'C)', 'D)')):
            current_group.setdefault('choices', []).append(line)

    formatted_texts = []

    for group in groups:
        formatted_text = convert_text_group(group['question'], group['choices'], group['correct_answers'])
        formatted_texts.append(formatted_text)

    with open(output_file, 'w', encoding='utf-8') as file:
        for formatted_text in formatted_texts:
            file.write(formatted_text + '\n\n')


# 调用示例
input_file = 'C:\\Users\\Administrator\\Desktop\\input.txt'
output_file = 'C:\\Users\\Administrator\\Desktop\\近代史.txt'
convert_text(input_file, output_file)