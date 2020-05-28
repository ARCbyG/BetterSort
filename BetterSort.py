import csv
import time
import random

def M__Loc(Matrix, loc:tuple):
    return Matrix[loc[0]][loc[1]]
def M_Row(Matrix, row:int):
    return Matrix[row]
def M_Col(Matrix, col:int):
    ret = []
    for i in Matrix:
        ret.append(i[col])
    return ret

# Key값은 [ 첫번째 키, 두번째 키, ...] 이런 식으로 입력해주세요
def Total__Sort(data, SortName:'All'or'Bub'or'Sel'or'Ins'or'Qui'or'Mer'or'Hea'or'She'= 'All', Key:int=0, increase:bool=True, Recommend:bool=False, StepPrint:'no'or'time'or'all'='no', Wating_sec:float=60 ):
    if StepPrint != 'no' and StepPrint != 'time' and StepPrint != 'all':
        print('StepPrint를 확인해주세요')
        return data
    ##### 정렬 이름 : 정렬 정의                                             : 공간복잡도 : 시간복잡도

    ##### 버블 정렬 : 인접한 두 값을 비교해 자리를 바꿔준다                 : N          : N^2
    if   SortName == 'Bub'or SortName == 'All':
        start = time.time()
        result = data

        for BubI in enumerate(result):
            if time.time()-start > Wating_sec:  # 시간이 초과하면 리턴
                print('버블 정렬 실패. 시간초과')
                return result

            if BubI[0] == len(result)-1 :           # Wave는 마지막 원소에 도달하면 탈출
                break
            if StepPrint != 'no': print()
            for BubJ in enumerate(result):
                if BubJ[0] == len(result)-BubI[0]-1:      # Round는 매 Wave의 미정렬 원소 끝에 도달하면 탈출 == 총 길이 - 정렬길이
                    break
                
                if result[BubJ[0]][Key[0]] > result[BubJ[0]+1][Key[0]] and increase==True:    # 비교 후 이후 값이 더 작다면 치환(오름차순 옵션)
                    result[BubJ[0]], result[BubJ[0]+1] = result[BubJ[0]+1], result[BubJ[0]]

                if result[BubJ[0]][Key[0]] < result[BubJ[0]+1][Key[0]] and increase==False:   # 비교 후 이후 값이 더 크다면 치환(내림차순 옵션)
                    result[BubJ[0]], result[BubJ[0]+1] = result[BubJ[0]+1], result[BubJ[0]]

                if StepPrint != 'no': print('Bubble     : Wave %3d  Round %3d    time : %3.8f    '%(BubI[0]+1,BubJ[0]+1, time.time()-start), end='')
                if StepPrint == 'time': print()
                if StepPrint == 'all': print(result)
        
        print('버블 정렬 성공. 소요 시간 : %3.8f'%(time.time()-start))
        if SortName != 'All':
            return result
    ##### 선택 정렬 : 끝 값을 검색해 저장, 남은 부분 반복                   : N          : N^2
    elif SortName == 'Sel'or SortName == 'All':
        start = time.time()
        result = data

        for SelI in enumerate(result):
            if time.time()-start > Wating_sec:  # 시간이 초과하면 리턴
                print('선택 정렬 실패. 시간초과')
                return result

            if SelI[0] == len(result)-1 :           # Wave는 마지막 원소에 도달하면 탈출
                break
            if StepPrint != 'no': print()
            Tmp = [SelI[0], result[SelI[0]][Key[0]]]
            for SelJ in enumerate(result):
                if SelJ[0] == len(result)-SelI[0]-1:      # Round는 매 Wave의 미정렬 원소 끝에 도달하면 탈출 == 총 길이 - 정렬길이
                    break
                
                if result[Tmp[0]][Key[0]] > result[-(SelJ[0]+1)][Key[0]] and increase==True:    # 비교 후 이후 값이 더 작다면 result[index]에 저장(오름차순 옵션)
                    Tmp = [-(SelJ[0]+1), result[-(SelJ[0]+1)][Key[0]]]                             # SelJ Round는 뒤쪽에서 돌도록

                if result[Tmp[0]][Key[0]] < result[-(SelJ[0]+1)][Key[0]] and increase==False:   # 비교 후 이후 값이 더 크다면 result[index]에 저장(내림차순 옵션)
                    Tmp = [-(SelJ[0]+1), result[-(SelJ[0]+1)][Key[0]]]                             # SelJ Round는 뒤쪽에서 돌도록

                if StepPrint != 'no': print('Selection  : Wave %3d  Round %3d   time : %3.8f    '%(SelI[0]+1, SelJ[0]+1, time.time()-start), end='')
                if StepPrint == 'time': print()
                if StepPrint == 'all': print('Tmp : %s    %s'%(Tmp, result))
            if result[SelI[0]][Key[0]] != result[Tmp[0]][Key[0]] :         # Tmp에 저장된 위치가 현재 i와 다르다면 swap
                result[Tmp[0]][Key[0]], result[SelI[0]][Key[0]] = result[SelI[0]][Key[0]], result[Tmp[0]][Key[0]]
                if StepPrint == 'all': print('정렬 후 : %s'%result)
            
        print('선택 정렬 성공. 소요 시간 : %3.8f'%(time.time()-start))
        if SortName != 'All':
            return result
    # 삽입 정렬 : 다른 값들을 옆으로 밀어 적절한 자리를 만들고 삽입         : N          : N^2  + 거의 정렬된 상태에서 고효율
    elif SortName == 'Ins'or SortName == 'All':
        start = time.time()
        result = data
        
        for InsI in range(1, len(result)):             # 첫 칸은 무조건 그대로 있으니 0은 패스.
            if time.time()-start > Wating_sec:  # 시간이 초과하면 리턴
                print('삽입 정렬 실패. 시간초과')
                return result

            Tmp = result[InsI]                          # 새로 정렬할 값은 항상 기정렬 배열의 마지막
            InsX = InsI                                    # 기정렬 배열의 크기(마지막위치) 저장                
            while InsX>0 and result[InsX-1][Key[0]] > Tmp[Key[0]] and increase==True: # 배열 범위 안에서 자신보다 큰 값이 나오면 밀기   (오름차순)
                result[InsX] = result[InsX-1]
                InsX -= 1
            while InsX>0 and result[InsX-1][Key[0]] > Tmp[Key[0]] and increase==False: # 배열 범위 안에서 자신보다 작은 값이 나오면 밀기 (내림차순)
                result[InsX] = result[InsX-1]
                InsX -= 1            
            result[InsX] = Tmp                      # 빈 자리에 삽입            

            if StepPrint != 'no': print('\nInsertion  : Wave %3d  time : %3.8f    '%(InsI+1, time.time()-start), end='')
            if StepPrint == 'time': print()
            if StepPrint == 'all': print('Tmp : %s    %s'%(Tmp, result))
            

        print('삽입 정렬 성공. 소요 시간 : %3.8f'%(time.time()-start))
        if SortName != 'All':
            return result
    # 퀵 정렬   : 첫 위치를 pivot으로 삼고 탐색, 첫 타겟과 치환         : N^2  + 대부분의 상황에서 고효율
    elif SortName == 'Qui'or SortName == 'All':
        start = time.time()
        result = data


        if SortName != 'All':
            return result
    # 병합 정렬 : 한 자료로 분할, 두 값 정렬 후 합치기 반복             : Nlog2N
    elif SortName == 'Mer'or SortName == 'All':
        start = time.time()
        result = data


        if SortName != 'All':
            return result
    else:
        print('SortName을 확인해주세요')
        return data


def main():
    
    #Test = [[5, '하늘'], [3, '하지'], [2, '가람'], [4, '미숫'], [1, '가리비']]
    '''
    roop = 1000
    Test = []
    for i in range(roop):
        Test.append([])
        Test[i] = [random.randint(1,100)]
    '''
    Test = [[4, 'ㄹ'], [3, 'ㄷ'], [1, 'ㄱ'], [2, 'ㄴ'], [5, 'ㅁ']]
    
    Total__Sort(Test, 'Ins', Key=[0], StepPrint='time', Wating_sec=10)
    #print("\n\n%s"%(Result))

    # 글 번호(업소 아이디) 순 정렬
    f = open('서울시 가격안정 모범업소 상품목록 현황.csv', 'r')     # 업소id / 업소명 / 분류코드 / 분류명 / 주소 / 전화번호 / 추천수 / 상품명 / 가격 
    w = open('정렬 결과.csv', 'w', encoding='EUC-KR')
    DATASET = []
    F = csv.reader(f)
    Col = []

    for i in F:                         # csv를 2차원 배열로 입력
        if len(Col) == 0:
            Col.append(i)
            continue
        DATASET.append(i)
    
    #print(DATASET)

    
    i, j = 0, 0
    for i in range(len(DATASET)):       # 2차원 배열을 csv로 출력
        for j in range(len(DATASET[0])):
            w.write(DATASET[i][j])
            w.write(', ')
        w.write('\n')

    #sorted()

    w.close()
    f.close()


if __name__ == "__main__":
    main()
