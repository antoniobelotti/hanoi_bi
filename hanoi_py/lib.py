def hanoi(n, source, dest, tmp):
    if n == 1:
        return ["{} -> {}".format(source, dest)]

    return  hanoi(n-1, source, tmp, dest) + \
            hanoi(1, source, dest, tmp) + \
            hanoi(n-1, tmp, dest, source)
    

def merge(n, source, dest, tmp):
    if n == 1:
        return ["{} -> {}".format(source, dest)]

    return  merge(n-1, dest, source, tmp) + \
            hanoi(n+(n-1), source, dest, tmp)


def hanoi_bicolor_with_merged_tower(n, source, dest, tmp):
    if n == 1:
        return ["{} -> {}".format(source, dest)]

    return  hanoi(n, source, dest, tmp) + \
            hanoi_bicolor_with_merged_tower(n-1, dest, source, tmp)


def hanoi_bicolor_version(n, source1, source2, tmp):
    return  merge(n, source2, source1, tmp) + \
            hanoi_bicolor_with_merged_tower(n*2, source1, source2, tmp)


def optimize(moves):
    i = 0
    while i <= len(moves):
        try:
            if moves[i][-1] == moves[i+1][0]:  # ex: a -> b , b -> c becomes a -> c
                moves[i] = moves[i].replace(moves[i][-1], moves[i+1][-1])
                del moves[i+1]

                if(moves[i][0] == moves[i][-1]):    # c -> c
                    del moves[i]

                if i > 0:   # may have deleted 2 moves: current move and next move. so get back to the previous move
                    i -= 1
            else:
                # continue the loop
                i += 1

        except IndexError:
            return
