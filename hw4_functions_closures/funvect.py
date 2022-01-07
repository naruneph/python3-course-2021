def superposition(funmod, funseq):
    def helper(f1, f2):
        return lambda x: f1(f2(x))
    return [helper(funmod, f) for f in funseq]
