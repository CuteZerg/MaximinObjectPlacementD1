def main():
    while True:
        try:
            k = int(input('Введите k (количество чисел r_i из условия задачи): '))
            print(f'Введите {k} чисел r_i через пробел:')
            r = list(map(float, input().split(' ')))
            if len(r) != k:
                raise Exception
            r.sort()
            g = float(input('Введите число g (левая граница отрезка допустимых значений для x): '))
            h = float(input('Введите число h (правая граница отрезка, h > g): '))
            if h <= g:
                raise Exception
            break
        except Exception:
            print('Произошла ошибка, попробуйте еще раз')
            input('Введите любую клавишу для продолжения')
    left_bound = -1
    right_bound = -1
    for i in range(len(r)):
        if r[i] >= g:
            left_bound = i
            break
    for i in range(len(r)-1, -1, -1):
        if r[i] <= h:
            right_bound = i
            break
    if left_bound == -1:
        print(f'x = {h}')
        return
    if r[-1] < h:
        r.append(h + (h - r[-1]))
    if r[1] > g:
        r.insert(0, g - (r[0] - g))
    if g <= 0.5*(r[left_bound] + r[left_bound-1]):
        left_bound -= 1
    if h < 0.5*(r[right_bound] + r[right_bound+1]):
        right_bound -= 1
    max_section = 0
    max_section_left_index = -1
    for i in range(left_bound, right_bound + 1):
        if (r[i + 1] - r[i]) > max_section:
            max_section = r[i + 1] - r[i]
            max_section_left_index = i
    print(f'x = {r[max_section_left_index] + max_section / 2.0}')


if __name__ == '__main__':
    main()
