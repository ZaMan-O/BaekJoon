import sys
I = sys.stdin.readline

dosun_position = list(map(int, I().split()))
command = I().strip()
robot_position = [0,0]
robot_rotation = 0
position_info = []
commands = [i for i in command if not i.isdigit()]
nums = []
distance_info = []
get_dosun = False

tmp = command.split("S")
for i in tmp:
    nums += i.split("T")
nums = [int(i) for i in nums if i]

for i in range(len(command)):
    if command[i] == 'T' or command[i] == 'S':
        now_command = command[i]

for i in range(len(commands)):
    if commands[i] == 'T':
        robot_rotation = (robot_rotation + nums[i]) % 4
    else:
        temp = robot_position[::]
        if robot_rotation == 0:
            robot_position[0] += nums[i]
        elif robot_rotation == 1:
            robot_position[1] += nums[i]
        elif robot_rotation == 2:
            robot_position[0] -= nums[i]
        elif robot_rotation == 3:
            robot_position[1] -= nums[i]
        position_info.append([temp[0], temp[1], robot_position[0], robot_position[1], robot_rotation])
    if i == len(commands) - 1:
        for ii in range(len(position_info)):
            position = position_info[ii]
            rotation = position[4]
            if rotation == 0 or rotation == 2:
                if max(position[0], position[2]) >= dosun_position[0] >= min(position[0], position[2]) and dosun_position[1] == position[1]:
                    print(-1)
                    get_dosun = True
                    break
                if max(position[0],position[2]) >= dosun_position[0] >= min(position[0], position[2]):
                    distance_info.append([dosun_position[0],position[1]])
                elif dosun_position[0] >= max(position[0], position[2]):
                    distance_info.append([max(position[0], position[2]), position[1]])
                else:
                    distance_info.append([min(position[0], position[2]), position[1]])
            else:
                if max(position[1], position[3]) >= dosun_position[1] >= min(position[1], position[3]) and dosun_position[0] == position[0]:
                    print(-1)
                    get_dosun = True
                    break
                if max(position[1],position[3]) >= dosun_position[1] >= min(position[1], position[3]):
                    distance_info.append([position[0],dosun_position[1]])
                elif dosun_position[1] >= max(position[1], position[3]):
                    distance_info.append([position[0], max(position[1], position[3])])
                else:
                    distance_info.append([position[0], min(position[1], position[3])])

if get_dosun == False and len(distance_info) >= 1:
    min_index = 0
    min_distance = 0
    for i in range(len(distance_info)):
        distance = pow(dosun_position[0] - distance_info[i][0], 2) + pow(dosun_position[1] - distance_info[i][1], 2)
        if i == 0:
            min_distance = distance
        else:
            if distance < min_distance:
                min_distance = distance
                min_index = i
    print(distance_info[min_index][0], distance_info[min_index][1])
elif get_dosun == False and robot_position == dosun_position:
    print(-1)
elif get_dosun == False:
    print(0, 0)