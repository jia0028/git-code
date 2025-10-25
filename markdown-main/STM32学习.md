### 一.基础知识
- 输出0为Vss:0V,1为Vdd:3.3V.输入最高5V
- GPIOA GPIO一般有16个,命名方式PA0~PA15
- 施密特触发器,滞回比较器
- 三极管的左边是基板，带箭头的是发射极，剩下的是集电极
### 二.驱动
* USE 使用、下划线、STD 标准、PERIPH 外设、下划线、DRIVER 駆动
### 三.操作STM32GPIO步骤
1.RCC开启GPIO的时钟
2.使用GPIO_Init函数初始化GPIO
3.使用输出或输入的函数控制GPIO口
void RCC_AHBPeriphClockCmd(uint32_t RCC_AHBPeriph, FunctionalState NewState);
void RCC_APB2PeriphClockCmd(uint32_t RCC_APB2Periph, FunctionalState NewState);
void RCC_APB1PeriphClockCmd(uint32_t RCC_APB1Periph, FunctionalState NewState);


void GPIO_DeInit(GPIO_TypeDef* GPIOx);
void GPIO_AFIODeInit(void);
void GPIO_Init(GPIO_TypeDef* GPIOx, GPIO_InitTypeDef* GPIO_InitStruct);
void GPIO_StructInit(GPIO_InitTypeDef* GPIO_InitStruct);
uint8_t GPIO_ReadInputDataBit(GPIO_TypeDef* GPIOx, uint16_t GPIO_Pin);
uint16_t GPIO_ReadInputData(GPIO_TypeDef* GPIOx);
uint8_t GPIO_ReadOutputDataBit(GPIO_TypeDef* GPIOx, uint16_t GPIO_Pin);
uint16_t GPIO_ReadOutputData(GPIO_TypeDef* GPIOx);
void GPIO_SetBits(GPIO_TypeDef* GPIOx, uint16_t GPIO_Pin);
void GPIO_ResetBits(GPIO_TypeDef* GPIOx, uint16_t GPIO_Pin);
void GPIO_WriteBit(GPIO_TypeDef* GPIOx, uint16_t GPIO_Pin, BitAction BitVal);
void GPIO_Write(GPIO_TypeDef* GPIOx, uint16_t PortVal);

* AIN:模拟输入,
* IN_FLOATING:浮空输入,
* IPD:下拉输入(>In Pull Down)
* IPU:上拉输入(in pull up),
* Out_OD:开漏输出
* Out_PP:推挽输出
* AF_OD:复用开漏
* AF_PP:复用推挽
* //低电平点亮~按位取反
* PESET高电平
* SET低电平
### 四.蜂鸣器
1.低电平蜂鸣器响,高电平蜂鸣器不响.
### 最后补充
* GPIO_InitStructure.GPIO_Speed=;  这是GPIO输出速度,对输入速度没用