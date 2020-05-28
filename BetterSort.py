import csv
import time
import random

def Total__Sort(data, SortName:'All'or'Bub'or'Sel'or'Ins'or'Qui'or'Mer'or'Hea'or'She'= 'All', Key:str or int = ..., increase:bool=True, Recommend:bool=False, StepPrint:bool=False, Wating_sec:float=60 ):
    
    # 정렬 이름 : 정렬 정의                                             : 공간복잡도 : 시간복잡도

    # 버블 정렬 : 인접한 두 값을 비교해 자리를 바꿔준다                 : N          : N^2
    if   SortName == 'Bub'or'All':
        start = time.time()
        result = data

        for i in enumerate(result):
            if time.time()-start > Wating_sec:  # 시간이 초과하면 리턴
                print('버블 정렬 실패. 시간초과')
                return result

            if i[0] == len(result)-1 :           # Wave는 마지막 원소에 도달하면 탈출
                break
            if StepPrint == True: print()
            for j in enumerate(result):
                if j[0] == len(result)-i[0]-1:      # Round는 매 Wave의 미정렬 원소 끝에 도달하면 탈출 == 총 길이 - 정렬길이
                    break
                
                if result[j[0]] > result[j[0]+1] and increase==True:    # 비교 후 이후 값이 더 작다면 치환(오름차순 옵션)
                    result[j[0]], result[j[0]+1] = result[j[0]+1], result[j[0]]

                if result[j[0]] < result[j[0]+1] and increase==False:   # 비교 후 이후 값이 더 크다면 치환(오름차순 옵션)
                    result[j[0]], result[j[0]+1] = result[j[0]+1], result[j[0]]

                if StepPrint == True: print('Bubble     : Wave %3d  Round %3d    time : %3.8f    %s'%(i[0]+1,j[0]+1, time.time()-start, result))
        
        print('버블 정렬 성공. 소요 시간 : %3.8f'%(time.time()-start))
        if SortName != 'All':
            return result
    # 선택 정렬 : 끝 값을 검색해 저장, 남은 부분 반복                   : N          : N^2
    elif SortName == 'Sel'or'All':
        start = time.time()
        result = data

        tmp = result[0]

        for i in enumerate(result):
            if time.time()-start > Wating_sec:  # 시간이 초과하면 리턴
                print('선택 정렬 실패. 시간초과')
                return result

            if i[0] == len(result)-1 :           # Wave는 마지막 원소에 도달하면 탈출
                break
            if StepPrint == True: print()
            for j in enumerate(result):
                if j[0] == len(result)-i[0]-1:      # Round는 매 Wave의 미정렬 원소 끝에 도달하면 탈출 == 총 길이 - 정렬길이
                    break
                
                if result[j[0]] > tmp and increase==True:    # 비교 후 이후 값이 더 작다면 저장(오름차순 옵션)
                    tmp = result[j[0]]

                if result[j[0]] < tmp and increase==False:   # 비교 후 이후 값이 더 크다면 저장(내림차순 옵션)
                    tmp = result[j[0]]

                if StepPrint == True: print('Selection  : Wave %3d  Round %3d    time : %3.8f    %s'%(i[0]+1,j[0]+1, time.time()-start, result))
        
        print('선택 정렬 성공. 소요 시간 : %3.8f'%(time.time()-start))
        if SortName != 'All':
            return result
    # 삽입 정렬 : 선택 위치에서 정렬된 배열 내 적합한 위치를 찾아 삽입  : N          : N^2  + 거의 정렬된 상태에서 고효율
    elif SortName == 'Ins'or'All':
        start = time.time()
        result = data


        if SortName != 'All':
            return result
    # 퀵 정렬   : 첫 위치를 pivot으로 삼고 탐색, 첫 타겟과 치환         : N^2  + 대부분의 상황에서 고효율
    elif SortName == 'Qui'or'All':
        start = time.time()
        result = data


        if SortName != 'All':
            return result
    # 병합 정렬 : 한 자료로 분할, 두 값 정렬 후 합치기 반복             : Nlog2N
    elif SortName == 'Mer'or'All':
        start = time.time()
        result = data


        if SortName != 'All':
            return result
    # 힙 정렬   :       : Nlog2N
    elif SortName == 'Hea'or'All':
        start = time.time()
        result = data


        if SortName != 'All':
            return result
    # 셸 정렬   :       : N^2
    elif SortName == 'She'or'All':
        start = time.time()
        result = data


        return result
    else:
        print('SortName을 확인해주세요')


def main():
    
    #Test = [10, 5, 2, 9, 3, 6, 7, 1, 8, 4]
    #Test = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    #Test = ['f', 'g', 'a', 'r', 'h', 'x']
    #Test = ['ㅎ', 'ㅁ', 'ㄷ', 'ㄴ', 'ㄱ']
    #Test = ['해', '하', '황', '곤', '공']
    #Test = ['하늘', '하지', '가람', '미숫가루', '가리비']
    Test = []
    for i in range(1000):
        Test.append(random.randint(1,100))

    #print(Test)
    Result = Total__Sort(Test, 'Sel', StepPrint=False, Wating_sec=.8)
    #print("\n\n%s"%(Result))

    '''
    # 글 번호(업소 아이디) 순 정렬
    f = open('서울시 가격안정 모범업소 상품목록 현황.csv', 'r')     # 업소id / 업소명 / 분류코드 / 분류명 / 주소 / 전화번호 / 추천수 / 상품명 / 가격 
    DATASET = []
    F = csv.reader(f)

    for i in F:
        if len(DATASET) == 0:
            for j in range(len(i)):
                DATASET.append(i[0])


    # 0. 데이터 셋, [기준 컬럼1, 기준컬럼2, ...]  1. 특정 정렬 / 모든 정렬  (++소요시간표시)  2. 오름차순 설정 
    # 3. 모든 정렬 시 추천 표시 여부  4. 정렬 과정 출력 여부  5. 정렬 최대 몇 초까지 기다려볼건지(기본 60초)
    #Total__Sort(DATASET, ['업소명', '상품명'], 'All') 
    #sorted()


    f.close()
    '''

if __name__ == "__main__":
    main()
