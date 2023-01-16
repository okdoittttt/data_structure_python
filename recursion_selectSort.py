# 목록의 두 인덱스에서 값을 교환하는 유틸리티 기능
def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


# 리스트에 대한 선택 정렬을 수행하는 기능
def selection_sort(A):
    for i in range(len(A) - 1):

        minimum = i

        for j in range(i + 1, len(A)):
            # `A[j]` 요소가 더 작으면 새로운 최소값입니다.
            if A[j] < A[minimum]:
                minimum = j  # 는 최소 요소의 인덱스를 업데이트합니다.

        # 하위 목록 `A[i…n-1]`의 최소 요소를 `A[i]`로 교체
        swap(A, minimum, i)


if __name__ == '__main__':
    A = [3, 5, 8, 4, 1, 9, -2]

    selection_sort(A)
    print(A)