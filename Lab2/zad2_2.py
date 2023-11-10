import multiprocessing

"""Funtion to merge two sorted list which are sorted in the same time"""

def merge_sorted_lists(list1, list2):
    result = []
    i = j = 0

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

def parallel_sort(data, processes):
    """Function for parallel sorting two data blocks"""
 
    chunk_size = len(data) // processes #calculate chunk of data which should be sorted by this process
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)] #split data to chunks

    pool = multiprocessing.Pool(processes=processes) #stworzenie procesu
    sorted_chunks = pool.map(sorted, chunks)

    pool.close() #konczenie pracy multiProcesow
    pool.join()

    while len(sorted_chunks) > 1: #Merge sorted chunks
        merged_chunks = []
        for i in range(0, len(sorted_chunks), 2):
            if i + 1 < len(sorted_chunks):
                merged_chunk = merge_sorted_lists(sorted_chunks[i], sorted_chunks[i+1])
                merged_chunks.append(merged_chunk)
            else:
                merged_chunks.append(sorted_chunks[i])
        sorted_chunks = merged_chunks

    return sorted_chunks[0]
