from rothermel import getRate
import math


# d = 0.001
# end_time = 10 * 60
# time_spice = 1
# now_time = 0

position_liveNum = dict()
position_K = dict()
position_cacl = dict()


def clear_map():
    position_liveNum.clear()
    position_K.clear()
    position_cacl.clear()


def cacl_map(U, Phi, position: tuple, d, time_spice, end_time, now_time=0, Ir0=None, Ir=None):
    """
    推演火势
    :param U: 风速 m/min
    :param Phi: 𝝓 坡度角度
    :param position: 起火点位置 （x, y）
    :param now_time: 起火时间，默认0
    :param end_time: 推演结束时间
    :param d: 网格间隔距离
    :param time_spice: 时间片大小，s
    :return:
    """
    if Ir0 is None:
        Ir0, Ir = getRate(U, Phi)
    sub_rates = [0] * 8

    sub_rates[0] = sub_rates[4] = Ir
    sub_rates[2] = sub_rates[6] = Ir0
    sub_rates[1] = sub_rates[3] = sub_rates[5] \
        = sub_rates[7] = (sub_rates[0]**2 + sub_rates[2]**2)**0.5

    x = position[0]
    y = position[1]
    position_cacl[(x, y)] = 1
    sub_positions = [0] * 8
    sub_positions[0] = (x, y+d)
    sub_positions[1] = (x+d, y+d)
    sub_positions[2] = (x+d, y)
    sub_positions[3] = (x+d, y-d)
    sub_positions[4] = (x, y-d)
    sub_positions[5] = (x-d, y-d)
    sub_positions[6] = (x-d, y)
    sub_positions[7] = (x-d, y+d)

    liveNum = get_liveNum(x, y)
    for i in range(0, 8):
        if sub_positions[i] not in position_cacl:
            position_K[sub_positions[i]] = get_ki(sub_rates[i], liveNum, i, time_spice, d)
            # position_cacl[sub_positions[i]] = 1
    position_liveNum[(x, y)] = liveNum + 1
    now_time += time_spice

    if now_time < end_time:
        for i in range(0, 7):
            if sub_positions[i] in position_K and position_K[sub_positions[i]] == 1:
                cacl_map(U, Phi, sub_positions[i], d, time_spice, end_time, now_time, Ir0, Ir)

    return position_K


def get_ki(ri, life_num, i, time_spice, d):
    i += 1
    a = 4 / math.pi * math.atan(2*ri*life_num*time_spice/((2**0.5+1 + (-1)**i*(2**0.5-1)) * d))
    if a > 1.9996:
        a = 1
    else:
        a = 0
    return math.floor(a)


def get_liveNum(x, y):
    if (x, y) not in position_liveNum:
        position_liveNum[(x, y)] = 1
    return position_liveNum[(x, y)]


if __name__ == '__main__':
    import time
    print(time.localtime(time.time()))
    cacl_map(2, 15, (5, 6), 1, 1, 10, 0)
    print(position_K)
    print(time.localtime(time.time()))