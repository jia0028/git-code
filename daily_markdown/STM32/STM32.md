#### 

运算放大器   51 AD/DA
![alt text](image.png)

uint8_t = unsigned char    uint16_t = unsigned short

####  宏定义  typedef   结构体  枚举

![alt text](image-1.png)
typedef:
![alt text](image-2.png)
结构体:
![alt text](image-3.png)

![alt text](image-4.png)
typedef和结构体的结合
![alt text](image-5.png)

枚举
![alt text](image-6.png)

#### GPIO输入
Ctrl+Alt+空格  代码提示
<!-- GPIO不管是输入还是输出都是对于单片机而言 ,操作流程是:开启时钟,定义结构体 (输入输出模式,引脚,输出速度)GPIO_Init将指定的GPIO外设初始化好
重要的是模块的封装,每个模块硬件可以使用一个单独的.h.c文件封装,这个可以分配给任何人完成团队的合作-->