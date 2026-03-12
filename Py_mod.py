import numpy as np
def comp(a,b,c):
    if a>10 and b>20:
        return 1
    if a<10 and c<20:
        return 2
    else:
        return 0

def intp(xarr, yarr, oarr):
    xarr = np.array(xarr, dtype=float)
    yarr = np.array(yarr, dtype=float)
    oarr = np.array(oarr, dtype=float)

    oarr_clipped = np.clip(oarr, xarr[0], xarr[-1])
    idx = np.searchsorted(xarr, oarr_clipped) - 1
    idx = np.clip(idx, 0, len(xarr) - 2)

    x0, x1 = xarr[idx], xarr[idx + 1]
    y0, y1 = yarr[idx], yarr[idx + 1]

    y_interp = y0 + (y1 - y0) * (oarr_clipped - x0) / (x1 - x0)

    return y_interp.tolist()
