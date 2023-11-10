import multiprocessing

def merge_sorted_lists(list1, list2):
    result = []
    i = j = 0

    list1 = try_list(list1)
    list2 = try_list(list2)

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    while i < len(list1):
        result.append(list1[i])
        i += 1

    while j < len(list2):
        result.append(list2[j])
        j += 1

    return result


def try_list(list1):
    try:
        len(list1)
    except TypeError:
        list1 = [list1]
    return list1


def check_sort(data):
    try:
        return sorted(data)
    except TypeError:
        if isinstance(data, int):
            return data
        else:
            raise

def parallel_sort(data, processes):

    with multiprocessing.Pool(processes=processes) as pool:
        sorted_chunks = pool.map(check_sort, data)

    while len(sorted_chunks) > 1:
        merged_chunks = []
        for i in range(0, len(sorted_chunks), 2):
            if i + 1 < len(sorted_chunks):
                merged_chunk = merge_sorted_lists(sorted_chunks[i], sorted_chunks[i+1])
                merged_chunks.append(merged_chunk)
            else:
                merged_chunks.append(sorted_chunks[i])
        sorted_chunks = merged_chunks

    return sorted_chunks[0]
