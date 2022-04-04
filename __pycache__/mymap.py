def mymap1(func, *seqs):
	res = []
	for args in zip(*seqs):
		res.append(func(*args))
	return res
def mymap2(func, *seqs):
        return [func(*args) for args in zip(*seqs)]

def myzip(*seqs):
        minlen = min(len(S) for S in seqs)
        return [tuple(S[i] for S in seqs) for i in range(minlen)]

def mymapPad(*seqs, pad=None):
        maxlen = max(len(S) for S in seqs)
        index = range(maxlen)
        return [tuple((S[i] if len(S) > i else pad) for S in seqs) for i in index]


def myzip2(*args):
        iters = map(iter, args)
        while iters:
                res = [next(i) for i in iters]
                yield tuple(res)
