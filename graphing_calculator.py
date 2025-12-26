import pygame, random, json, math
from Typing import Typing
import SomeFunctions as sf
pygame.init()

#date started: 08/09/2024, Sunday @ 6:30pm -> 10:00pm
#continued: 09/09/2024, Monday @ 9:00am -> 10:00am, 4:20pm -> 5:40pm
#continued: 10/09/2024, Tuesday @ 9:30am -> 10:00am
#continued: 11/09/2024, Wednesday @ 9:00am -> 10:30am, 8:00pm -> 10:15pm
#continued: 12/09/2024, Thursday @ 5:30pm -> 9:15pm
#continued: 13/09/2024, Friday @ 10:10am -> 10:45am
#continued: 16/09/2024, Monday @ 4:10pm -> 4:30pm
#date finished: dd/mm/yyyy

infoObject = pygame.display.Info() #OR WIDTH, HEIGHT = X, Y
WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h

screen = pygame.display.set_mode((0, 0))
pygame.display.set_caption('Graphing Calculator')
clock = pygame.time.Clock()
pygame.display.toggle_fullscreen()

BLACK = (0, 0, 0)
WHITE = (227, 221, 215)
GRAY = (150, 150, 150)
LBLUE = (240, 240, 255)
DGRAY = (50, 50, 50)
LYELLOW = (220, 220, 150)
DYELLOW = (200, 200, 100)
LRED = (230, 170, 170)
DRED = (200, 140, 140)

pulling_window = False
left_dummy = False
specific_value_typing = False
specific_value = ""
new_function_typing = False
new_function = ""
key_list = []
dummy = []
function_names_offset = 0
specific_value_ans = ""
specific_number = ""
specific_func_name = ""
displaying_answer = False
click_dummy = 0
scale = 50 # scale is the number of pixels 1 unit represents (1 unit = 50 pixels)

TEXT_FONT = pygame.font.SysFont('falling sky', 55)
y_axis_arrow = TEXT_FONT.render('^', True, BLACK)
x_axis_arrow = TEXT_FONT.render('>', True, BLACK)

NUMBERS_FONT = pygame.font.SysFont('falling sky', 40)
zero_text = NUMBERS_FONT.render('0', True, BLACK)

PullingPanel = pygame.Rect(300, 0, 4, HEIGHT) #x, y, width, height
DrawingWindow = pygame.Rect(PullingPanel.x, 0, WIDTH - PullingPanel.x, HEIGHT)
SpecificFunctionValueRect = pygame.Rect(0.25 * PullingPanel.x, 30, PullingPanel.x / 2, 100)
NewFunctionRect = pygame.Rect(0.25 * PullingPanel.x, 160, PullingPanel.x / 2, 100)

x_offset = PullingPanel.x + DrawingWindow.width / 2
y_offset = HEIGHT/2

radius_of_dots = 2

try:
    f = open("All_Functions_Saved.json", 'r')
except:
    f = open("All_Functions_Saved.json", 'w')
    f.write("[]")
    f.close()

f = open("All_Functions_Saved.json", 'r')
All_Functions_Saved = json.load(f)    
f.close()

class Function:
    new_adding_dummy = 0
    All_Functions = []

    def __init__(self, name, equation, start, end, number_of_iterations, color):
        self.name = name
        self.equation = equation
        self.start = start
        self.end = end
        self.number_of_iterations = number_of_iterations
        self.color = color

        self.step = (float(self.end) - float(self.start)) / float(self.number_of_iterations)
        self.function_text = TEXT_FONT.render(f"{self.name}: {self.equation}", True, self.color)
        self.points = []
        self.x = self.start

        self.vertical_line = False
        if "x=" in self.equation:
            self.vertical_line = True
            self.start = self.end = self.equation.split("x=")[-1]

        self.font_size = 1

        while ((PullingPanel.x - pygame.font.SysFont('falling sky', int(PullingPanel.x / self.font_size)).size(f'{str(self.name)}: {self.equation} [{str(int(self.start))}; {str(int(self.end))}]')[0]) / 2) <= PullingPanel.x and self.font_size != 0.01 and PullingPanel.x - pygame.font.SysFont('falling sky', int(PullingPanel.x / self.font_size)).size(f'{str(self.name)}: {self.equation} [{str(int(self.start))}; {str(int(self.end))}]')[0] <= 10:
            self.font_size += 0.01
        else:
            self.font_size -= 0.01

        for item in All_Functions_Saved:
            if item[0] == self.name:
                Function.new_adding_dummy += 1
        if Function.new_adding_dummy == 0:
            All_Functions_Saved.append([self.name, self.equation, self.start, self.end, self.number_of_iterations, self.color])
        Function.new_adding_dummy = 0

        with open("All_Functions_Saved.json", 'w') as f:
            json.dump(All_Functions_Saved, f)

        Function.All_Functions.append(self)

        self.delete_rect = pygame.Rect(5, 300 + Function.All_Functions.index(self) * 50 + function_names_offset - 2, PullingPanel.x - 10, 45)


for func in All_Functions_Saved:
    Function(func[0], func[1], func[2], func[3], func[4], func[5])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEWHEEL:
            if mouse_rect.x >= PullingPanel.x + 10:
                scale += event.y * 5
            else:
                function_names_offset += event.y * 10

        if event.type == pygame.KEYDOWN:
            key_list.append(1)
            if specific_value_typing:
                specific_value = Typing(specific_value, dummy)
            if new_function_typing:
                new_function = Typing(new_function, dummy)

        if event.type == pygame.KEYUP:
            key_list.remove(1)

    if len(key_list) == 0:
        dummy.clear()

    left, middle, right = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()
    mouse_rect = pygame.Rect(mouse[0], mouse[1], 1, 1)
    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_ESCAPE]:
        with open("All_Functions_Saved.json", 'w') as f:
            json.dump(All_Functions_Saved, f)
        pygame.quit()
        exit()

    if keys_pressed[pygame.K_TAB]:
        x_offset = (WIDTH - PullingPanel.x) / 2 + PullingPanel.x
        y_offset = HEIGHT / 2
        scale = 50

    if keys_pressed[pygame.K_UP]:
        y_offset += 1 * 5
    if keys_pressed[pygame.K_DOWN]:
        y_offset -= 1 * 5
    if keys_pressed[pygame.K_LEFT]:
        x_offset += 1 * 5
    if keys_pressed[pygame.K_RIGHT]:
        x_offset -= 1 * 5

    if scale < 1:
        scale = 1
    
    screen.fill(WHITE)

    DrawingWindow.x, DrawingWindow.width = PullingPanel.x, WIDTH - PullingPanel.x
    SpecificFunctionValueRect.x =  0.25 * PullingPanel.x
    SpecificFunctionValueRect.width = PullingPanel.x / 2
    NewFunctionRect.x = 0.25 * PullingPanel.x
    NewFunctionRect.width = PullingPanel.x / 2

    pygame.draw.rect(screen, LBLUE, DrawingWindow)
    pygame.draw.line(screen, BLACK, (0, 290), (PullingPanel.x, 290), width = 3)


    if mouse_rect.colliderect(SpecificFunctionValueRect):
        pygame.draw.rect(screen, DYELLOW, SpecificFunctionValueRect, border_radius = 5)
        if left and not new_function_typing:
            specific_value_typing = True
            specific_value = ''
    else:
        pygame.draw.rect(screen, LYELLOW, SpecificFunctionValueRect, border_radius = 5)
    pygame.draw.rect(screen, BLACK, SpecificFunctionValueRect, border_radius = 5, width = 3)


    if mouse_rect.colliderect(NewFunctionRect):
        pygame.draw.rect(screen, DRED, NewFunctionRect, border_radius = 5)
        if left and not specific_value_typing:
            new_function_typing = True
            new_function = ''
    else:
        pygame.draw.rect(screen, LRED, NewFunctionRect, border_radius = 5)
    pygame.draw.rect(screen, BLACK, NewFunctionRect, border_radius = 5, width = 3)



    panel_font_size = int(PullingPanel.x / 5 - 3)
    PANEL_FONT = pygame.font.SysFont('falling sky', panel_font_size)

    specific_value_text = PANEL_FONT.render('f(a) = b', True, BLACK)
    screen.blit(specific_value_text, ((SpecificFunctionValueRect.width - PANEL_FONT.size('f(a) = b')[0]) / 2 + SpecificFunctionValueRect.x, (SpecificFunctionValueRect.height - PANEL_FONT.size('f(a) = b')[1]) / 2 + SpecificFunctionValueRect.y))

    new_function_text = pygame.font.SysFont('falling sky', int(PullingPanel.x / 8 - 6)).render('New Function', True, BLACK)

    screen.blit(new_function_text, ((NewFunctionRect.width - pygame.font.SysFont('falling sky', int(PullingPanel.x / 8 - 6)).size('New Function')[0]) / 2 + NewFunctionRect.x, (NewFunctionRect.height - pygame.font.SysFont('falling sky', int(PullingPanel.x / 8 - 3)).size('Function')[1]) / 2 + NewFunctionRect.y))


    if left and not left_dummy:
        x_temp, y_temp = mouse_rect[0], mouse_rect[1]
        x_offset_temp, y_offset_temp = x_offset, y_offset
        left_dummy = True

    if left and left_dummy:
        if mouse_rect.colliderect(PullingPanel) or mouse_rect.x <= PullingPanel.x + 15:
            pass
        else:
            x_offset = mouse_rect[0] + x_offset_temp - x_temp
            y_offset = mouse_rect[1] + y_offset_temp - y_temp

    if left and click_dummy == 0:
        click_dummy += 1

    if not left:
        pulling_window = False
        x_temp = y_temp = 0
        left_dummy = False

    if mouse_rect.colliderect(PullingPanel) or pulling_window:
        pygame.draw.rect(screen, GRAY, PullingPanel)
        if left:
            pulling_window = True
    else:
        pygame.draw.rect(screen, BLACK, PullingPanel)

    if pulling_window and 0 <= mouse_rect.x <= 450:
        PullingPanel.x = mouse_rect.x

    pygame.draw.line(screen, DGRAY, (PullingPanel.x + 4, y_offset), (WIDTH, y_offset), width = 2) #x-axis

    if x_offset - PullingPanel.x >= 0:
        pygame.draw.line(screen, DGRAY, (x_offset, 0), (x_offset, HEIGHT), width = 2) #y-axis
    
    screen.blit(x_axis_arrow, (WIDTH - 20, y_offset - 20))

    if x_offset >= PullingPanel.x:
        screen.blit(y_axis_arrow, (x_offset - 10, -5))
        screen.blit(zero_text, (x_offset + 5, y_offset + 5))


    for i in range(int(y_offset/scale) + 1): # y-axis +
        if x_offset >= PullingPanel.x:
            pygame.draw.circle(screen, BLACK, (x_offset + 1, y_offset - scale * i + 1), radius_of_dots)

    for i in range(int(-(HEIGHT - y_offset/scale) + 1), 0): # y-axis -
        if x_offset >= PullingPanel.x:
            pygame.draw.circle(screen, BLACK, (x_offset + 1, y_offset - scale * i + 1), radius_of_dots)

    for i in range(int(-(x_offset - PullingPanel.x) / scale), 0): # x-axis -
        if scale * i + x_offset >= PullingPanel.x:
            pygame.draw.circle(screen, BLACK, (scale * i + x_offset, y_offset + 1), radius_of_dots)

    for i in range(1, int((WIDTH - x_offset) / scale) + 1): # x-axis +
        if x_offset + scale * i >= PullingPanel.x:
            pygame.draw.circle(screen, BLACK, (x_offset + scale * i, y_offset + 1), radius_of_dots)

    if displaying_answer:
        try:
            screen.blit(TEXT_FONT.render(f'{specific_func_name}({str(specific_number)}) = {specific_value_ans}', True, BLACK), (WIDTH - pygame.font.SysFont('falling sky', 40).size(f'{specific_func_name}({str(specific_number)}) = {specific_value_ans}')[0] - 75, HEIGHT - 45))

            if float(specific_number) * scale + x_offset >= PullingPanel.x:
                pygame.draw.circle(screen, BLACK, (float(specific_number) * scale + x_offset + 1, - float(specific_value_ans) * scale + y_offset + 1), 5)
        except:
            displaying_answer = False

    for func in Function.All_Functions:
        if not func.vertical_line:
            if len(func.points) < func.number_of_iterations:
                for i in range(0, int(func.number_of_iterations + 1)):
                    try:
                        func.points.append([func.x, eval(func.equation.replace('x', str(func.x)))])
                        func.x += func.step
                    except:
                        Function.All_Functions.remove(func)
                        print('removed from original')
                        for saved_func in All_Functions_Saved:
                            if saved_func[0] == func.name:
                                All_Functions_Saved.remove(saved_func)
                                print('removed from save')


            for point in func.points:
                if point[0] * scale + x_offset >= PullingPanel.x: # draws the points on the graph
                    pygame.draw.circle(screen, func.color, (point[0] * scale + x_offset + 1, - point[1] * scale + y_offset + 1), 1)

                    if func.points.index(point) != len(func.points) - 1: # connects the dots
                        pygame.draw.line(screen, func.color, (point[0] * scale + x_offset, - point[1] * scale + y_offset), (func.points[func.points.index(point) + 1][0] * scale + x_offset, - func.points[func.points.index(point)+1][1] * scale + y_offset), width = 2)

        else:
            if float(func.start) * scale + x_offset >= PullingPanel.x + 5:
                pygame.draw.line(screen, func.color, (float(func.start) * scale + x_offset, 0), (float(func.start) * scale + x_offset, HEIGHT), width = 2)

        if 300 + Function.All_Functions.index(func) * 50 + function_names_offset >= 300: # displays name of functions on screen
            screen.blit(pygame.font.SysFont('falling sky', int(PullingPanel.x / func.font_size)).render(f'{str(func.name)}: {func.equation} [{str(int(func.start))}; {str(int(func.end))}]', True, func.color), (((PullingPanel.x - pygame.font.SysFont('falling sky', int(PullingPanel.x / func.font_size)).size(f'{str(func.name)}: {func.equation} [{str(int(func.start))}; {str(int(func.end))}]')[0]) / 2), 300 + Function.All_Functions.index(func) * 50 + function_names_offset))

        func.delete_rect.width = PullingPanel.x - 10
        func.delete_rect.y = 300 + Function.All_Functions.index(func) * 50 + function_names_offset

        if mouse_rect.colliderect(func.delete_rect) and not left and click_dummy == 1: # removes the functions you click on
            if func.delete_rect.y >= 300:
                Function.All_Functions.remove(func)
                for saved_func in All_Functions_Saved:
                    if saved_func[0] == func.name:
                        All_Functions_Saved.remove(saved_func)
            click_dummy = 0

    if new_function_typing:
        screen.blit(TEXT_FONT.render(new_function, True, BLACK), (PullingPanel.x + 20, HEIGHT - 50))
        LRED = DRED
        if keys_pressed[pygame.K_RETURN]:
            try:
                try:
                    color = (int(new_function.split()[5]), int(new_function.split()[6]), int(new_function.split()[7])) 
                except:
                    color = (random.randint(10, 245), random.randint(10, 245), random.randint(10, 245))
                Function(new_function.split()[0], new_function.split()[1], float(new_function.split()[2]), float(new_function.split()[3]), float(new_function.split()[4]), color)
            except:
                new_function = ''
            new_function_typing = False
    else:
        LRED = (230, 170, 170)

    if specific_value_typing:
        screen.blit(TEXT_FONT.render(specific_value, True, BLACK), (PullingPanel.x + 20, HEIGHT - 50))
        LYELLOW = DYELLOW
        if keys_pressed[pygame.K_RETURN]:
            try:
                specific_value = specific_value.split('(')
                if specific_value[-1][-1] == ')':
                    specific_value[-1] = specific_value[-1][:-1]
                specific_number = specific_value[-1]
                for func in Function.All_Functions:
                    if not func.vertical_line:
                        if func.name == specific_value[0]:
                            try:
                                specific_value_ans = eval(func.equation.replace('x', str(specific_number)))
                                specific_func_name = specific_value[0]
                                displaying_answer = True
                                break
                            except:
                                specific_value = ''
                                specific_value_ans = ''
                                specific_func_name = ''
                    else:
                        if func.name == specific_value[0]:
                            if specific_number == func.start:
                                specific_number = func.start
                                specific_value_ans = 0
                                specific_func_name = specific_value[0]
                                displaying_answer = True
                                break
                        else:
                            specific_value = ''
                            specific_value_ans = ''
                            specific_func_name = ''
            except:
                specific_value = ''
                specific_value_ans = ''
                specific_func_name = ''

            specific_value_typing = False
            specific_value = ''
    else:
        LYELLOW = (220, 220, 150)

    if not left:
        click_dummy = 0

    pygame.display.update()
    clock.tick(60)
