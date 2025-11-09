import pygame
import random
import time




class Playairplane(pygame.sprite.Sprite):
    def __init__(self,screen):
        
        # 精灵类的初始化
        pygame.sprite.Sprite.__init__(self)

        # 创建飞机图片
        self.airplane = pygame.image.load("D:\\vscode\\resources\\war-of-planes-master\\feiji\\hero1.png")


        # 初始化飞机位置
        self.x = 480 / 2 - 100
        self.y = 700 
        # 获取飞机图片尺寸
        self.airplane_rect = self.airplane.get_rect()
        # 更改飞机当前的位置，底部居中
        self.airplane_rect.midbottom = (240,822)
        # 获取图片左上角位置
        self.airplane_rect.topleft = [self.x,self. y]

        # 更新窗口对象
        self.screen = screen
        
        # 设置飞机速度
        self.speed = 3

        # 创建子弹列表
        self.bulletes = pygame.sprite.Group() 


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

         # 更新子弹坐标
         self.bulletes.update()
         # 绘制所有子弹并显示屏幕
         self.bulletes.draw(self.screen)


        # 遍历所有子弹
     #     for bullet in self.bulletes[:]:
              
     #          # 发射子弹
     #          bullet.auto_move()

     #          # 显示子弹
     #          bullet.bullet_display()

     #          #判断是否超边界
     #          if bullet.is_off_screen():
     #               self.bulletes.remove(bullet)     

    # 更新显示
    def update(self):
         self.key_control()
         self.display()
         
    # 按空格只发射1颗子弹
    def shoot(self):

        bullet = Bullet(self.screen, self.airplane_rect.centerx, self.airplane_rect.top)
        self.bulletes.add(bullet)


# 敌机初始化
class Enemyairplane(pygame.sprite.Sprite):
     def __init__(self,screen):
          
          # 精灵类的初始化
          pygame.sprite.Sprite.__init__(self)

          # 创建敌机图片
          self.enemyairplane = pygame.image.load("D:\\vscode\\resources\\war-of-planes-master\\feiji\\enemy0.png")  #51*39

          # 获取敌机图片尺寸
          self.enemyairplane_rect = self.enemyairplane.get_rect()
          self.enemyairplane_rect.topleft = [0,0]

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
          self.bulletes=pygame.sprite.Group()

          # 敌机一开始的方向
          self.dict = 'right'
     
     # 敌机显示
     def display(self):
          
          # 把飞机图片拉进窗口里面
          self.screen.blit(self.enemyairplane,(self.x,self.y))
          # 更新子弹坐标
          self.bulletes.update()
          # 绘制所有子弹并显示在屏幕上
          self.bulletes.draw(self.screen)

          # 遍历所有子弹
          # for bullet in self.bulletes[:]:
               
          #      # 发射子弹
          #      bullet.auto_move()

          #      # 显示子弹
          #      bullet.bullet_display()

          #      #判断是否超边界
          #      if bullet.is_off_screen():
          #           self.bulletes.remove(bullet)    

     # 更新位置
     def update(self):
          self.auto_move()
          self.auto_shoot()
          self.display()


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
          random_num = random.randint(1,100)
          # 有频率的开火
          if random_num == 4:
               bullet = EnemyBullet(self.screen,self.x,self.y)
               self.bulletes.add(bullet)


# 子弹初始化
class Bullet(pygame.sprite.Sprite):
     
    def __init__(self,screen,x,y):
         
         # 精灵类初始化
         pygame.sprite.Sprite.__init__(self)

         # 子弹图片创建
         self.image = pygame.image.load("D:\\vscode\\resources\\war-of-planes-master\\feiji\\bullet.png")

         # 更新窗口
         self.screen = screen

         # 获取子弹图片尺寸
         self.rect = self.image.get_rect()

         # 初始化子弹位置
         self.rect.centerx = x #子弹中心对齐飞机
         self.rect.bottom = y  #子弹底部对齐y


         # self.bullet_rect.topleft = [self.bullet_rect.centerx,self.bullet_rect.bottom]

        #子弹速度
         self.speed = 2

    # 更新位置
    def update(self):
          self.rect.bottom -= self.speed
          if self.rect.bottom < 0:
               self.kill()


#     # 显示子弹
#     def bullet_display(self):
#          self.screen.blit(self.bullet,self.bullet_rect)

    


# 敌机子弹初始化
class EnemyBullet(pygame.sprite.Sprite):
     
    def __init__(self,screen,x,y):
         
         # 精灵类初始化
         pygame.sprite.Sprite.__init__(self)

         # 子弹图片创建
         self.image = pygame.image.load("D:\\vscode\\resources\\war-of-planes-master\\feiji\\bullet1.png")

         # 更新窗口
         self.screen = screen
         
         # 获取子弹图片尺寸
         self.rect = self.image.get_rect()
         
        # 初始化子弹位置
         self.rect.centerx = x + 25 #子弹中心对齐飞机
         self.rect.top = y + 39  #子弹底部对齐y

         # self.bullet_rect.topleft = [self.bullet_rect.centerx,self.bullet_rect.bottom]

        #子弹速度
         self.speed = 2

     # 更新位置
    def update(self):
          self.rect.bottom += self.speed
          if self.rect.bottom > 852:
               self.kill()

#     # 显示子弹
#     def bullet_display(self):
#          self.screen.blit(self.bullet,self.rect)



# 背景音乐初始化
class BackGroundSound(object):
     
     def __init__(self):

          # 音乐模块初始化
          pygame.mixer.init()

          # 导入音乐文件
          pygame.mixer.music.load("D:\\vscode\\resources\\war-of-planes-master\\feiji\\bg2.ogg")

          # 音量大小
          pygame.mixer.music.set_volume(1)

     def SoundPlay(self):

          # 无限循环播放
          pygame.mixer.music.play(-1)
     

def main():
    
    # 音乐播放   
    sound = BackGroundSound()
    sound.SoundPlay()
    
    # 生成窗口
    screen = pygame.display.set_mode((480,852))

    # 创建背景图片
    background  = pygame.image.load("D:\\vscode\\resources\\war-of-planes-master\\feiji\\background.png")

    # 创建飞机对象，不要忘记传窗口
    airplane = Playairplane(screen)

    enemy_airplane =Enemyairplane(screen)

    # 显示窗口，需要一直显示当前的窗口
    while True:
            # 把背景图片拉进窗口
            screen.blit(background, (0,0))

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
               
            # 飞机控制和边界管理
            airplane.key_control()

            # 飞机显示
            airplane.display()

            # 敌机显示
            enemy_airplane.display()

            # 敌机自动移动
            enemy_airplane.auto_move()

            # 敌机自动开火
            enemy_airplane.auto_shoot()


            pygame.display.update()
            time.sleep(0.01)

if __name__ == "__main__":
    main()
