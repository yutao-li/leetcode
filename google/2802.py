from collections import defaultdict

SIZE = 26
BASE = ord('a')


def has_distance_exactly_one(string_list: [str]):
    prefix_postfix_pair = defaultdict(set)
    for s in string_list:
        assert s.isalpha() and s.islower()
        forward_hash = [0]
        backward_hash = [0]
        for ch in s:
            forward_hash.append(forward_hash[-1] * SIZE + ord(ch) - BASE)
        for ch in s[::-1]:
            backward_hash.append(backward_hash[-1] * SIZE + ord(ch) - BASE)
        backward_hash = backward_hash[::-1]
        for i, ch in enumerate(s):
            pair = (forward_hash[i], backward_hash[i + 1])
            if prefix_postfix_pair[pair] and ch not in prefix_postfix_pair[pair]:
                return True
            prefix_postfix_pair[pair].add(ch)
    return False


string_list = ['abcd', 'abed', 'asdf']
print(has_distance_exactly_one(string_list))
