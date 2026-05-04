import random

def create_maze(width, height):
    """Создаём пустой лабиринт (все клетки — стены)."""
    # width, height должны быть нечётными
    maze = [['#' for _ in range(width)] for _ in range(height)]
    return maze

def recursive_division(maze, x, y, w, h):
    """
    Рекурсивное деление области.
    (x, y) — верхний левый угол области
    w, h — ширина и высота области (в клетках)
    """
    # Проверяем, можно ли ещё делить
    if w < 3 or h < 3:
        return
    
    # Выбираем ориентацию стены
    horizontal = random.choice([True, False])
    
    if horizontal:
        # Горизонтальная стена
        wall_y = random.randint(y + 1, y + h - 2)  # не по границам
        # Где будет проход
        passage_x = random.randint(x, x + w - 1)
        
        # Рисуем стену (кроме прохода)
        for cx in range(x, x + w):
            if cx != passage_x:
                maze[wall_y][cx] = '#'
        
        # Рекурсивно обрабатываем верхнюю и нижнюю части
        recursive_division(maze, x, y, w, wall_y - y)
        recursive_division(maze, x, wall_y + 1, w, y + h - wall_y - 1)
    else:
        # Вертикальная стена
        wall_x = random.randint(x + 1, x + w - 2)
        passage_y = random.randint(y, y + h - 1)
        
        # Рисуем стену (кроме прохода)
        for cy in range(y, y + h):
            if cy != passage_y:
                maze[cy][wall_x] = '#'
        
        # Рекурсивно обрабатываем левую и правую части
        recursive_division(maze, x, y, wall_x - x, h)
        recursive_division(maze, wall_x + 1, y, x + w - wall_x - 1, h)

def generate_maze(width, height):
    """Генерируем лабиринт методом рекурсивного деления."""
    # Размеры должны быть нечётными (для корректных стен и проходов)
    if width % 2 == 0: width += 1
    if height % 2 == 0: height += 1
    
    maze = create_maze(width, height)
    
    # Начальное "прорезание" внешних стен
    for i in range(width):
        maze[0][i] = ' '
        maze[height-1][i] = ' '
    for i in range(height):
        maze[i][0] = ' '
        maze[i][width-1] = ' '
    
    # Запускаем рекурсивное деление для внутренней области
    recursive_division(maze, 1, 1, width-2, height-2)
    
    # Ставим вход и выход (по желанию)
    maze[1][0] = ' '   # вход слева
    maze[height-2][width-1] = ' '  # выход справа
    
    return maze

def print_maze(maze):
    for row in maze:
        print(''.join(row))

# Пример использования
maze = generate_maze(31, 21)
print_maze(maze)