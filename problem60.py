from lib.primes import primes_sieve

all_primes = set()
for i in primes_sieve(10000000):
    all_primes.add(i)


def check_prime(a, b):
    global all_primes
    return int(str(a) + str(b)) in all_primes and int(str(b) + str(a)) in all_primes


def primes_concat(primes_set):
    min_sum = None
    c_set = None
    for p1 in primes_set:
        s1 = {p for p in primes_set if check_prime(p, p1)}
        if len(s1) == 0 or (min_sum is not None and p1 > min_sum):
            continue

        for p2 in s1:
            s2 = {p for p in s1 if check_prime(p, p2)}
            if len(s2) == 0 or (min_sum is not None and p1 + p2 > min_sum):
                continue

            for p3 in s2:
                s3 = {p for p in s2 if check_prime(p, p3)}
                if len(s3) == 0 or (min_sum is not None and p1 + p2 + p3 > min_sum):
                    continue

                # for p4 in s3:
                #     s4 = {p for p in s3 if check_prime(p, p4)}
                #     if len(s4) == 0 or (min_sum is not None and p1 + p2 + p3 + p4 > min_sum):
                #         continue
                else:
                    temp = {p1, p2, p3, min(s3)}
                    temp_sum = sum(temp)
                    if min_sum is None or temp_sum < min_sum:
                        c_set = temp
                        min_sum = temp_sum

    return c_set, min_sum


primes = set([x for x in all_primes if x <= 20000])

print primes_concat(primes)
