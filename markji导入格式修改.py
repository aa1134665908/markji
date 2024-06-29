import re

with open('E:\desk\啊.txt', 'w') as fs :
    fs.write('')
    # 单选题
# with open('E:\desk\墨墨.txt', 'r') as f :
#     for line in f :
#         url = line.replace('\n', '')
#         r = re.match('.*(。)', url)
#         a = re.match('.*(A\\))', url)
#         b = re.match('.*(B\\))', url)
#         c = re.match('.*(C\\))', url)
#         d = re.match('.*(D\\))', url)
#         f = url.endswith('分  ')
#         with open('E:\desk\啊.txt', 'a') as fq :
#             if a is not None :
#                 fq.writelines('[Choice##' + '\n')
#                 fq.write('- ')
#
#             if b is not None :
#                 fq.write('- ')
#             if c is not None :
#                 fq.write('- ')
#             if d is not None :
#                 fq.write('- ')
#             fq.writelines(url + '\n')
#             if f :
#                 fq.writelines(']' + '\n' + '\n')
#
# with open('E:\desk\啊.txt', 'r') as f :
#     lines = f.readlines()
#     for idx, line in enumerate(lines) :
#         if '正确答案为' in line :
#             ans = line[7]
#             for i in range(idx - 1, 0, -1) :
#                 if ans in lines[i] :
#                     lines[i] = lines[i].replace('-', '*', 1)
#                     break
#         if '正确答案为' in line :
#             del lines[idx]
#             del lines[idx]
#     for linew in lines :
#         url = linew.replace('\n', '')
#         r = re.match('- ([A-D])\\)', url)
#         q = re.match('\\* ([A-D]\\))', url)
#         if r is not None :
#             print('- ' + url.replace(r.group(), ''))
#         elif q is not None :
#             print('* ' + url.replace(q.group(), ''))
#         else :
#             print(url)
    # 多选题
with open('E:\desk\墨墨.txt', 'r') as f :
    for line in f :
        url = line.replace('\n', '')
        r = re.match('.*(。)', url)
        a = re.match('.*(A\\))', url)
        b = re.match('.*(B\\))', url)
        c = re.match('.*(C\\))', url)
        d = re.match('.*(D\\))', url)
        fs = url.find('本小题得分')
        with open('E:\desk\啊.txt', 'a') as fq :
            if a is not None :
                fq.writelines('[Choice#multi#' + '\n')
                fq.write('- ')

            if b is not None :
                fq.write('- ')
            if c is not None :
                fq.write('- ')
            if d is not None :
                fq.write('- ')
            fq.writelines(url + '\n')
            if fs !=-1:
                fq.writelines(']' + '\n' + '\n')

with open('E:\desk\啊.txt', 'r') as f :
    lines = f.readlines()
    for idx, line in enumerate(lines) :
        if '正确答案为' in line :
            ans = line[7:line.find('你')].strip().split(' ')
            for i in range(idx - 1, 0, -1) :
                if '[Choice#multi#' in lines[i]:
                    break
                for p in ans:
                    if p in lines[i]:
                        lines[i] = lines[i].replace('-', '*', 1)

        if '正确答案为' in line :
            del lines[idx]
            del lines[idx]
    for linew in lines :
        url = linew.replace('\n', '')
        r = re.match('- ([A-D])\\)', url)
        q = re.match('\\* ([A-D]\\))', url)
        if r is not None :
            print('- ' + url.replace(r.group(), ''))
        elif q is not None :
            print('* ' + url.replace(q.group(), ''))
        else :
            print(url)

# str='正确答案为： A B C   你错选为 B C'
#
# a=str[7:str.find('你')].strip().split(' ')
#
# print(a)