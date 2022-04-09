import itertools
import random



def _flatten_user(user):
    return  [elem["name"] for elem in user ]


def _findsubsets(S,m):
    return set(itertools.combinations(S, m))


def _sort_sublist(list):
    return [sorted(elem, key=str.lower)for elem in list]


def _compare_with_doubles(selection, doubles):
    return [elem for elem in selection if elem not in doubles]


def select_random_Ns(user, room_user):
    usser_flatten = _flatten_user(user)
    user_set = set(usser_flatten)
    result = []
    for val in _findsubsets(user_set, 2):
        result.append(list(val))
    without_doubles = _compare_with_doubles(_sort_sublist(result), _sort_sublist(room_user))
    best_solution = []
    best_solution_count = 0 
    for _ in range(10):
        result = []
        user_assigned = []
        random.shuffle(without_doubles)
        for elem in without_doubles:
            if elem[0] not in user_assigned and elem[1] not in user_assigned:
                result.append(elem)
                user_assigned.extend(elem)
        if len(result)>best_solution_count:
            best_solution = list(result)
            best_solution_count = len(result)
    return best_solution