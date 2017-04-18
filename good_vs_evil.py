def goodVsEvil(good,evil):
    good_weight = [1,2,3,3,4,10]
    evil_weight = [1,2,2,2,3,5,10]
    total_good = sum([a * b for a, b in zip(good_weight, map(int, good.split()))])
    total_evil = sum([a * b for a, b in zip(evil_weight, map(int,evil.split()))])

    if total_evil>total_good:
        return 'Battle Result: Evil eradicates all trace of Good'
    elif total_evil< total_good:
        return 'Battle Result: Good triumphs over Evil'
    else:
        return 'Battle Result: No victor on this battle field'

print goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1')