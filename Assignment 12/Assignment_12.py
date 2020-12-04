#P12.2
def merge(A, left, mid, right) :
    sorted = [] # 병합된 결과를 저장할 리스트
    i = left #왼쪽 블럭
    j = mid + 1 #오른쪽 블럭
    while i<=mid and j<=right : #왼쪽 블럭과 오른쪽 블럭의 데이터들을 비교하면서 병합
        if A[i] <= A[j] :
            sorted.append(A[i])
            i = i+1
        else :
            sorted.append(A[j])
            j = j+1
    while i<=mid : #왼쪽 블럭에 남은게 있다면
        sorted.append(A[i])
        i = i+1
    while j<=right : #오른쪽 블럭에 남은게 있다면
        sorted.append(A[j])
        j = j+1
    A[left:right + 1] = sorted #병합된 결과를 덮어쓰기
def merge_sort(A) :
    step = 0
    i = 1
    while i < len(A) :
        step += 1
        j = 0
        while j < len(A) :
            #왼쪽, 중간, 오른쪽을 결정
            left = j
            #mid, right는 IndexError를 발생시킬 수 있으므로 예외처리를 해주어야 한다.
            try :
                mid = j + i - 1
                A[mid] #Index를 직접 체크
            except IndexError:
                mid = len(A) - 1
            try :
                right = j + i*2 -1
                A[right] #Index를 직접 체크
            except IndexError:
                right = len(A) - 1                
            merge(A,left,mid,right)
            j = j + i * 2
        print('Step {} : {}'.format(step, A))
        i*=2

if __name__ == "__main__":
    numbers = list(map(int, input('Insert Numbers : ').split()))
    merge_sort(numbers)
    
    print("Result : {}".format(numbers))