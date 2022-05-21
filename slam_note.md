# 视觉slam笔记
##针孔相机模型
1. 世界坐标系：
	- 世界坐标：$\begin{matrix}P_w\end{matrix}$
2. 相机坐标系：O-x-y-z
	- 由于相机运动产生$\begin{matrix}R\end{matrix}$旋转矩阵和$\begin{matrix}t\end{matrix}$平移向量
	- 相机坐标：$\widetilde{P}$~c~ $\begin{bmatrix}X&Y&Z\end{bmatrix}$ ^T^
	- 公式：$\widetilde{P}$~c~ = $\begin{matrix}RP_w+t\end{matrix}$ = $\begin{matrix}TP_w\end{matrix}$
3. 成像平面：O'-x'-y'
	- 成像平面坐标：$\begin{matrix}P'\end{matrix}$ $\begin{bmatrix}X'&Y'&Z'\end{bmatrix}$^T^
	- 内参矩阵$\begin{matrix}K\end{matrix}$ = $\begin{pmatrix}f_x&0&c_x\\0&f_y&c_y\\0&0&1\end{pmatrix}$
	- 公式：
		- $\frac{Z}{f}$=$\frac{X}{X'}$=$\frac{Y}{Y'}$
		- $\begin{cases}u=\alpha X' + c_x\\v=\beta Y'+c_y\end{cases}$
		- $\begin{matrix}Z\end{matrix}$ $\begin{pmatrix}u\\v\\1\end{pmatrix}$ = $\begin{pmatrix}f_x&0&c_x\\0&f_y&c_y\\0&0&1\end{pmatrix}$ $\begin{pmatrix}X\\Y\\Z\end{pmatrix}$ = $\begin{matrix}KP\end{matrix}$ &emsp;其中 $\begin{matrix}f_x\end{matrix}$ =  $\alpha$ $\begin{matrix}f\end{matrix}$，$\begin{matrix}f_y\end{matrix}$ = $\beta$ $\begin{matrix}f\end{matrix}$

4. 归一化平面：
	-将XYZ三个方向投影到归一化平面Z=1上
	- 归一化坐标：$\begin{matrix}P_c\end{matrix}$ [$\frac{X}{Z}$ $\frac{Y}{Z}$ 1]^T^
5. 像素平面：o-u-v
	- 经过内参后得到像素坐标
	- 像素坐标：$\begin{matrix}P_{uv}\end{matrix}$ $\begin{bmatrix}u&v\end{bmatrix}$^T^
	- $\begin{matrix}P_{uv} = K P_c \end{matrix}$
##畸变模型
图像畸变的校正：
	- $\begin{cases}x_{corrected} = x(1+k_1r^2+k_2r^4+k_3r^6)+2p_1xy+p_2(r^2+2x^2)\\y_{corrected} = y(1+k_1r^2+k_2r^4+k_3r^6)+p_1(r^2+2y^2)+2p_2xy\end{cases}$
根据实际选择几项进行校正
##灰度图
一张宽度640，高度480分辨率的灰度图 `unsigned char image[480][640]`

访问位于**x,y**处的像素 `unsigned char pixel = image[y][x]`

![图像坐标示意图](https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fpic4.zhimg.com%2Fv2-183fac8fd8f40019594d5b962f2ad4cf_b.jpg&refer=http%3A%2F%2Fpic4.zhimg.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1644663441&t=1d4f49ff631811b1aa91981768148b41)


