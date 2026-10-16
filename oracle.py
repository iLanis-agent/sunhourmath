import math, json

def plural(n, one, many):
    return one if n == 1 else many

def tenths(x):
    return math.floor(x * 10 + 0.5) / 10

def fixed1(x):
    return f"{tenths(x):.1f}"

SEASONS = {"summer": 0.4, "spring": 1.0, "fall": 1.0, "winter": 2.0}

def band_truth(hours):
    if not (hours > 0):
        raise ValueError("the hours must be above zero")
    if hours >= 6:
        band = "full sun"
    elif hours >= 4:
        band = "part sun"
    elif hours >= 2:
        band = "part shade"
    else:
        band = "shade"
    return f"{hours} {plural(hours, 'hour', 'hours')} of direct sun reads {band} honestly."

def match_truth(need, offer):
    if not (need > 0):
        raise ValueError("the plant's ask must be above zero")
    if not (offer > 0):
        raise ValueError("the offered hours must be above zero")
    diff = offer - need
    if diff < 0:
        verdict = f"runs {fixed1(-diff)} hours short honestly"
    elif diff > 0:
        verdict = f"has {fixed1(diff)} hours to spare honestly"
    else:
        verdict = "meets the ask exactly honestly"
    return f"A plant asking {need} {plural(need, 'hour', 'hours')} in a spot that offers {offer} {verdict}."

def shadow_truth(height, season):
    if not (height > 0):
        raise ValueError("the height must be above zero")
    mult = SEASONS.get(season)
    if not mult:
        raise ValueError("the season must be summer, spring, fall or winter")
    label = "summer" if season == "summer" else ("winter" if season == "winter" else "spring and fall")
    return f"A {height}-foot obstacle throws a {fixed1(height * mult)}-foot shadow in {label} honestly."

def stolen_truth(distance, depth, shadow):
    if not (distance >= 0):
        raise ValueError("the distance must be zero or more")
    if not (depth > 0):
        raise ValueError("the bed depth must be above zero")
    if not (shadow > 0):
        raise ValueError("the shadow must be above zero")
    shadow_r = tenths(shadow)
    overlap = min(depth, max(0, shadow_r - distance))
    if overlap <= 0:
        return f"A bed starting {fixed1(distance)} feet from the fence and running {fixed1(depth)} feet deep sits fully clear of the {fixed1(shadow_r)}-foot shadow honestly."
    return f"A bed starting {fixed1(distance)} feet from the fence and running {fixed1(depth)} feet deep spends {fixed1(overlap)} feet inside the {fixed1(shadow_r)}-foot shadow honestly."

FNS = {"bandTruth": band_truth, "matchTruth": match_truth, "shadowTruth": shadow_truth, "stolenTruth": stolen_truth}

CASES = [
    ("bandTruth", [8]),
    ("bandTruth", [5.5]),
    ("bandTruth", [3]),
    ("bandTruth", [1]),
    ("bandTruth", [6]),
    ("bandTruth", [4]),
    ("bandTruth", [2]),
    ("bandTruth", [0]),
    ("bandTruth", [-2]),
    ("matchTruth", [8, 5.5]),
    ("matchTruth", [6, 8]),
    ("matchTruth", [6, 6]),
    ("matchTruth", [4, 3.5]),
    ("matchTruth", [1, 4]),
    ("matchTruth", [0, 5]),
    ("matchTruth", [8, 0]),
    ("shadowTruth", [6, "spring"]),
    ("shadowTruth", [6, "summer"]),
    ("shadowTruth", [6, "winter"]),
    ("shadowTruth", [10, "fall"]),
    ("shadowTruth", [4, "summer"]),
    ("shadowTruth", [1, "winter"]),
    ("shadowTruth", [0, "summer"]),
    ("shadowTruth", [6, "monsoon"]),
    ("stolenTruth", [4, 6, 12]),
    ("stolenTruth", [10, 6, 12]),
    ("stolenTruth", [14, 6, 12]),
    ("stolenTruth", [0, 6, 12]),
    ("stolenTruth", [4, 20, 12]),
    ("stolenTruth", [-1, 6, 12]),
    ("stolenTruth", [4, 0, 12]),
    ("stolenTruth", [4, 6, 0]),
]

out = []
for fn, args in CASES:
    rec = {"fn": fn, "args": args}
    try:
        rec["out"] = FNS[fn](*args)
    except ValueError as e:
        rec["err"] = str(e)
    out.append(rec)
    print(fn, args, "->", rec.get("out") or ("ERR: " + rec["err"]))

with open("expected.json", "w") as f:
    json.dump(out, f, indent=1)
    f.write("\n")
print(f"{len(out)} cases written")
