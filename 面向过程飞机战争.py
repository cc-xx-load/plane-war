import pygame

def main():

    # 生成窗口
    screen = pygame.display.set_mode((480,852))

    # 创建背景图片
    background  = pygame.image.load("D:\\vscode\\resources\\飞机战争\\war-of-planes-master\\feiji\\background.png")

    # 创建飞机图片
    airplane = pygame.image.load("D:\\vscode\\resources\\飞机战争\\war-of-planes-master\\feiji\\hero1.png")

    # 初始化飞机位置
    x = 480 / 2 - 100
    y = 700 

    # 获取飞机图片尺寸
    airplane_rect = airplane.get_rect()
    airplane_rect.midbottom = (240,822)
    

    # 设置飞机速度
    speed = 5

    # 显示窗口，需要一直显示当前的窗口
    while True:
            # 把背景图片拉进窗口
            screen.blit(background, (0,0))

            # 把飞机图片拉进窗口
            screen.blit(airplane,airplane_rect)

            # 处理窗口的对应事件
            for event in pygame.event.get():
                 
                # 判断是否点击退出按键
                 if event.type == pygame.QUIT:
                      pygame.quit()
                      exit()

            #监听键盘按键
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_a]:
                 airplane_rect.x -= speed
            if key_pressed[pygame.K_d]:
                 airplane_rect.x += speed
            if key_pressed[pygame.K_w]:
                 airplane_rect.y -= speed 
            if key_pressed[pygame.K_s]:
                 airplane_rect.y += speed   
            
            # 设置飞机可移动的区间
            if airplane_rect.left < 0:
                airplane_rect.left = 0
            if airplane_rect.right > 480:
                airplane_rect.right = 480
            if airplane_rect.top < 0:
                airplane_rect.top = 0
            if airplane_rect.bottom > 852:
                airplane_rect.bottom = 852
            
            pygame.display.update()


if __name__ == "__main__":
    main()
