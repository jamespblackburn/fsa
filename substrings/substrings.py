from math import factorial, log, nan
from functools import reduce
import sys
import pdb


def predict_total_substrings(word):
    word_dict = {}
    for char in word.strip():
        if char in word_dict.keys():
            word_dict[char] += 1
        else:
            word_dict[char] = 1
    sum_of_values, product, factorial_denom = 0, 1, 1
    for v in word_dict.values():
        sum_of_values += v
        product *= v
        factorial_denom *= factorial(v-1)
    return int( factorial(sum_of_values) / (product * factorial_denom) )


def count_substrings(word_string, word_list):
    total_found = 0
    for line in word_list:
        line = line.strip()
        current_str = word_string
        for char in line:
            if char in current_str:
                current_str = current_str.replace(char, '')
            else:
                break
        else:
            total_found += 1
    return total_found


def iterate_wordlist(word_list_filename, output_file):
    data = []
    with open(word_list_filename, 'r') as outer_iter:     
        for line in outer_iter:
            line = line.strip()
            with open(word_list_filename, 'r') as inner_iter:
                total_found = count_substrings(line, inner_iter)
                total_possible = predict_total_substrings(line)
                efficiency = float(total_found / total_possible)
                log_efficiency = log(efficiency)
            data.append((line, total_found, total_possible, efficiency, log_efficiency))
    sorted_data = sorted(data, key=lambda x: x[4], reverse=True)
    for item in sorted_data:
        print(item)
        output_file.write(item[0] + "\t\t\t" +\
                          str(item[1]) + "\t\t" +\
                          str(item[2]) + "\t\t" +\
                          str(item[3]) + "\t\t" +\
                          str(item[4]) + "\n")
       

output_file = open('output.txt', 'w')
iterate_wordlist('american-english', output_file)
output_file.close()


'''
word_string = sys.argv[1]
word_string = word_string.lower()
word_dict = make_word_dict(word_string)

print('total number of possible distinguishable substrings: {}'.format(total_possible))
print('total number of substrings found in word list: {}'.format(total_found))
print('efficiency: {}'.format(efficiency))
print('inverse efficiency: {}'.format(1 / efficiency))
print('log efficiency: {}'.format(log(efficiency)))


if __name__ == "__main__":
    input_string = sys.argv[1]
    count_substrings(input_string)
'''