import pygame
import random

class Playairplane(object):

    # 飞机的初始化
    def __init__(self,screen):
         
        # 创建飞机图片
        self.airplane = pygame.image.load("D:\\vscode\\resources\\飞机战争\\war-of-planes-master\\feiji\\hero1.png")

        # 初始化飞机位置
        self.x = 480 / 2 - 100
        self.y = 700 

        # 获取飞机图片尺寸
        self.airplane_rect = self.airplane.get_rect()
        # 更改飞机当前的位置，底部居中
        self.airplane_rect.midbottom = (240,822)

        # 更新窗口对象
        self.screen = screen
        
        # 设置飞机速度
        self.speed = 1

        # 创建子弹列表
        self.bulletes = []


    # 飞机控制的初始化
    def key_control(self):
            
            #监听键盘按键
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_a]:
                 self.airplane_rect.x -= self.speed
            if key_pressed[pygame.K_d]:
                 self.airplane_rect.x += self.speed
            if key_pressed[pygame.K_w]:
                 self.airplane_rect.y -= self.speed 
            if key_pressed[pygame.K_s]:
                 self.airplane_rect.y += self.speed   
            # if key_pressed[pygame.K_SPACE]:
            #     #  空格键发射子弹
            #      self.bullet = Bullet(self.screen,self.airplane_rect.centerx,self.airplane_rect.top)
            #     # 子弹放列表里面
            #      self.s.append(self.bullet)
            #      self.bulletes.append(self.bullet)

            
            # 设置飞机可移动的区间
            if self.airplane_rect.left < 0:
                self.airplane_rect.left = 0
            if self.airplane_rect.right > 480:
                self.airplane_rect.right = 480
            if self.airplane_rect.top < 0:
                self.airplane_rect.top = 0
            if self.airplane_rect.bottom > 852:
                self.airplane_rect.bottom = 852
    
    # 飞机显示
    def display(self):
         
         # 把飞机图片拉进窗口里面
         self.screen.blit(self.airplane,self.airplane_rect)

        # 遍历所有子弹
         for bullet in self.bulletes[:]:
              
              # 发射子弹
              bullet.auto_move()

              # 显示子弹
              bullet.bullet_display()

              #判断是否超边界
              if bullet.is_off_screen():
                   self.bulletes.remove(bullet)     


    # 按空格只发射1颗子弹
    def shoot(self):

        bullet = Bullet(self.screen, self.airplane_rect.centerx, self.airplane_rect.top)
        self.bulletes.append(bullet)


# 敌机初始化
class Enemyairplane(object):
     pygame.init()

     def __init__(self,screen):
          
          # 创建敌机图片
          self.enemyairplane = pygame.image.load("D:\\vscode\\resources\\飞机战争\\war-of-planes-master\\feiji\\enemy0.png")  #51*39

          # 获取敌机图片尺寸
          self.enemyairplane_rect = self.enemyairplane.get_rect()

          # 更新窗口
          self.screen = screen

          # 初始化敌机位置
          side = random.choice(['left','right'])
          if side == 'left':
               self.x = random.randint(0,240)
          elif side == 'right':
               self.x = random.randint(300,400)

          self.y = random.randint(-40,-10)

          # 敌机速度
          self.speed = 0.5

          # 创建子弹列表
          self.bulletes=[]

          # 敌机一开始的方向
          self.dict = 'right'
     
     # 敌机显示
     def display(self):
          
          # 把飞机图片拉进窗口里面
          self.screen.blit(self.enemyairplane,(self.x,self.y))

          # 遍历所有子弹
          for bullet in self.bulletes[:]:
               
               # 发射子弹
               bullet.auto_move()

               # 显示子弹
               bullet.bullet_display()

               #判断是否超边界
               if bullet.is_off_screen():
                    self.bulletes.remove(bullet)    

     # 敌机自动移动
     def auto_move(self):
          self.y += self.speed
          # if self.dict == 'right':
          #      self.x+=self.speed
          # elif self.dict == 'left':
          #      self.x-=self.speed

          # if self.x > 480 - 51:
          #      self.dict = 'left'
          # elif self.x <= 0:
          #      self.dict = 'right'
     
     def auto_shoot(self):
          random_num = random.randint(1,40)
          # 有频率的开火
          if random_num == 4:
               bullet = EnemyBullet(self.screen,self.x,self.y)
               self.bulletes.append(bullet)


# 子弹初始化
class Bullet(object):
     
    def __init__(self,screen,x,y):

         # 子弹图片创建
         self.bullet = pygame.image.load("D:\\vscode\\resources\\飞机战争\\war-of-planes-master\\feiji\\bullet.png")

        #  获取子弹图片尺寸
         self.bullet_rect = self.bullet.get_rect()

         # 更新窗口
         self.screen = screen
        
        # 初始化子弹位置
         self.bullet_rect.centerx = x #子弹中心对齐飞机
         self.bullet_rect.bottom = y  #子弹底部对齐y

        #子弹速度
         self.speed = 1


    # 显示子弹
    def bullet_display(self):
         self.screen.blit(self.bullet,self.bullet_rect)

    #子弹移动
    def auto_move(self):
         self.bullet_rect.bottom -= self.speed

    #判断子弹是否超过屏幕
    def is_off_screen(self):
         return self.bullet_rect.bottom < 0
    


# 敌机子弹初始化
class EnemyBullet(object):
     
    def __init__(self,screen,x,y):
         

         # 子弹图片创建
         self.bullet = pygame.image.load("D:\\vscode\\resources\\飞机战争\\war-of-planes-master\\feiji\\bullet1.png")

        #  获取子弹图片尺寸
         self.bullet_rect = self.bullet.get_rect()

         # 更新窗口
         self.screen = screen
        
        # 初始化子弹位置
         self.bullet_rect.centerx = x + 25 #子弹中心对齐飞机
         self.bullet_rect.bottom = y + 39  #子弹底部对齐y

        #子弹速度
         self.speed = 2

    # 显示子弹
    def bullet_display(self):
         self.screen.blit(self.bullet,self.bullet_rect)

    #子弹移动
    def auto_move(self):
         self.bullet_rect.bottom += self.speed

    #判断子弹是否超过屏幕
    def is_off_screen(self):
         return self.bullet_rect.bottom > 852

              
     

def main():
    
    # 生成窗口
    screen = pygame.display.set_mode((480,852))

    # 创建背景图片
    background  = pygame.image.load("D:\\vscode\\resources\\飞机战争\\war-of-planes-master\\feiji\\background.png")

    # 创建飞机对象，不要忘记传窗口
    airplane = Playairplane(screen)

    enemy_airplane =Enemyairplane(screen)

    # 显示窗口，需要一直显示当前的窗口
    while True:
            # 把背景图片拉进窗口
            screen.blit(background, (0,0))

            # 把飞机图片拉进窗口
            airplane.display()


            # 处理窗口的对应事件
            for event in pygame.event.get():
                 
                # 判断是否点击退出按键
                 if event.type == pygame.QUIT:
                      pygame.quit()
                      exit()


                # 判断是否按下空格键,每按一次发射1颗子弹，不支持连续按住发射
                 if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        airplane.shoot()



            # 把背景图片拉进窗口
            screen.blit(background, (0,0))

            # 把飞机图片拉进窗口
            airplane.display()

            # 把敌机图片拉进窗口
            enemy_airplane.display()

            # 敌机自动移动
            enemy_airplane.auto_move()

            # 敌机自动开火
            enemy_airplane.auto_shoot()

            #飞机控制和边界管理
            airplane.key_control()

            pygame.display.update()

if __name__ == "__main__":
    main()
