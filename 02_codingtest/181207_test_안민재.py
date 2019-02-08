import operator

def solution(N, stages):
    total_number_of_people = len(stages)
    failure = [0 for _ in range(N)]
    number_of_people_in_stage = [ 0 for _ in range(N + 1)]

    #현재 각 stage 에 몇명 있는지 확인
    for stage in stages:
        print(stage)
        number_of_people_in_stage[stage - 1] += 1

    #failure 계산
    sum = 0
    for index, number in enumerate(number_of_people_in_stage):
        try:
            failure[index] = number / (total_number_of_people - sum)
            sum += number
        except:
            failure[index] = 0

    #각 stage 당 failure
    stage_failure = dict()
    for index, fail in enumerate(failure):
        stage_failure[index] = fail

    sorted_stage_failure = sorted(stage_failure.items(), key=operator.itemgetter(1), reverse=True)

    return_value = list()
    for item in sorted_stage_failure:
        return_value.append(item[0])

    return return_value
