import math


def getRate(U, Phi):
    """
    利用Rothermel 算法计算蔓延速度
    :param U: 风速 m/min
    :param Phi: 𝝓 坡度角度
    :return: 火焰蔓延速度, 考虑风速和坡度下的蔓延速度
    """
    W0 = 0.6
    h = 8372
    Pp = 545
    sigma = 8800
    delta = 0.15
    Mf = 0.3
    St = 0.007
    Se = 0.005
    Mx = 0.34

    # 8
    A = 8.9033 * (sigma ** -0.7913)
    # 4
    Gamma_max = (0.0591 + 2.926 * (sigma ** -1.5)) ** -1
    # 6
    Pb = W0 / delta
    # 5
    beta = Pb / Pp
    # 7
    BetaOp = 0.20395 * (sigma ** -0.8189)
    # 3
    Gamma = Gamma_max * ((beta / BetaOp) ** A) * math.exp(A * (1 - beta / BetaOp))

    # 9
    Wn = W0 * (1 - St)
    # 10
    EtaM = 1 - 2.59 * Mf / Mx + 5.11 * ((Mf / Mx) ** 2) - 3.52 * (Mf / Mx) ** 3
    # 11
    EtaS = 0.174 * (Se ** -0.19)
    # 12
    Zeta = ((192 + 7.9095 * sigma) ** -1) * math.exp((0.972+3.7597*(sigma**0.4)*(beta+0.1)))
    # 14
    Epsilon = math.exp(-4.528 / sigma)
    # 15
    Qig = 581 + 2594 * Mf

    # 2
    Ir = Gamma * Wn * h * EtaM * EtaS
    # 1
    R0 = Ir * Zeta / (Pb * Epsilon * Qig)

    # 17
    PhiS = 5.275 * (beta ** -0.3) * (math.tan(Phi) ** 2)

    # 20
    C = 7.47 * math.exp(-0.8711 * (sigma ** 0.55))
    # 21
    B = 0.15988 * (sigma ** 0.54)
    # 22
    E = 0.715 * math.exp(-0.01094 * sigma)
    # 19
    PhiW = C * ((3.281 * U) ** B) * ((beta / BetaOp) ** -E)
    # 18
    R = R0 * (1 + PhiS + PhiW)
    return R0, R
