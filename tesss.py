import sys

def minh(x, B0, cA, cB):
    q0 = B0 // cB
    qx = (B0 + x) // cB
    jumps = qx - q0
    best = -x + cA * qx
    if jumps >= 1:
        rem = B0 % cB
        L0 = cB - rem if rem != 0 else cB
        b0 = L0 - 1
        val0 = -b0 + cA * q0
        if val0 < best:
            best = val0
        k = jumps - 1
        b_k = L0 + k * cB - 1
        q_k = q0 + k
        val_k = -b_k + cA * q_k
        if val_k < best:
            best = val_k
    return best

def solve(A, B, cA, cB, fA):
    lo, hi = 0, 2 * 10**18
    while lo < hi:
        mid = (lo + hi) // 2
        val = A + mid + minh(mid, B, cA, cB)
        if val >= fA:
            hi = mid
        else:
            lo = mid + 1
    return lo

def main():
    data = sys.stdin.read().split()
    idx = 0
    T = int(data[idx]); idx += 1
    out = []
    for _ in range(T):
        A = int(data[idx]); B = int(data[idx+1]); cA = int(data[idx+2])
        cB = int(data[idx+3]); fA = int(data[idx+4]); idx += 5
        out.append(str(solve(A, B, cA, cB, fA)))
    print('\n'.join(out))

main()