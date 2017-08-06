import re, random
import numpy as np
import json

poem_files = ['pg17192.txt', 'The_Hundred_Best_English_Poe.txt', 'Where the Sidewalk Ends by Shel Silverstein_djvu.txt']

poem_lines = []
firstword_count_dict = {}

for poem_file in poem_files:
    f = open(poem_file, 'r')

    for line in f:
        if len(line) > 5:
            words = re.findall('\w+',line)
            poem_lines.append(words)
    f.close()

# print poem_lines

word_nextword_counts_dict = {}

for word_list in poem_lines:
    word_list.append('\n')
    for i in range(len(word_list)-1):
        thisword = word_list[i]
        nextword = word_list[i+1]

        if thisword not in word_nextword_counts_dict:
            word_nextword_counts_dict[thisword] = {nextword: 1}
        else:
            if nextword not in word_nextword_counts_dict[thisword]:
                word_nextword_counts_dict[thisword][nextword] = 1
            else:
                word_nextword_counts_dict[thisword][nextword] += 1

word_nextword_probs_dict = {}

for word in word_nextword_counts_dict:
    nextword_dict = word_nextword_counts_dict[word]
    word_nextword_probs_dict[word] = {}
    for nextword in nextword_dict:
        word_nextword_probs_dict[word][nextword] = float(nextword_dict[nextword])/sum(word_nextword_counts_dict[word].values())

for word in word_nextword_probs_dict:
    print word, ':', word_nextword_probs_dict[word]

print len(word_nextword_probs_dict)
# words = words.replace(',', ' ').replace('.', ' ')
#
# word_states = re.findall('\w+',words)
#
# print word_states
# print len(set(word_states))
#
# counts_dictionary = {}
#
# for i in range(len(word_states)-1):
#     first_word = word_states[i]
#     next_word = word_states[i+1]
#
#     if first_word == 'a':
#         if (first_word, next_word) in counts_dictionary:
#             counts_dictionary[(first_word, next_word)] += 1
#         else:
#             counts_dictionary[(first_word, next_word)] = 1
#
# print counts_dictionary
#
# transition_probabilities = {}
#
# s = sum(counts_dictionary.values())
#
# # for i in range(10):
# #     line = ''
# #     for j in range(7):
# #         line += results[random.randint(0, len(results)-1)] + ' '
# #     print line

states = word_nextword_probs_dict.keys()

p = []
for i in range(len(states)):
    p.append(1.0/len(states))

for x in range(10):
    state = np.random.choice(states, p=p)
    poem_line_states = [state]

    for i in range(15):
        if state != '\n':
            nextword_dict = word_nextword_probs_dict[state]
            all_possible_nextwords = []
            nextword_probs = []
            for w in nextword_dict:
                all_possible_nextwords.append(w)
                nextword_probs.append(nextword_dict[w])

            state = np.random.choice(all_possible_nextwords, p=nextword_probs)
            poem_line_states.append(state)

    poem_line = ' '.join([w for w in poem_line_states if w != '\n'])
    print poem_line

output_file = open('poem_model.json', 'w')
output_file.write(json.dumps(word_nextword_probs_dict))
output_file.close()



#     if state == 'sleep':
#         state = np.random.choice(states, p=[0.7, 0.3])
#     elif state == 'eat':
#         state = np.random.choice(states, p=[0.9, 0.1])
#     rabbit_states.append(state)
#
# print rabbit_states
#
# for i in range(len(rabbit_states)-1):
#     curr_state = rabbit_states[i]
#     next_state = rabbit_states[i+1]
#
