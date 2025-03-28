# 等距螺旋线

等距螺旋线应为:

$$
\rho = \frac{a}{2\pi}\theta+b
$$

本题中$b=0$,因此简化为:

$$
\rho=\frac{a}{2\pi}\theta
$$

对龙头进行讨论,记$t$时刻龙头极角为$\theta_{0}(t)$,则对$dl$和$d\theta$有:
(这是参数方程求距离,在高数上有此公式)

$$
\begin{aligned}

dl&=\sqrt{\rho(\theta)^2+\rho'(\theta)^2}d\theta\\
&=\sqrt{\frac{a^2}{4\pi^2}(\theta^2+1)}d\theta\\
&=\frac{a}{2\pi}\sqrt{\theta^2+1}d\theta
\end{aligned}
$$

对于dl和dt有:

$$
dl=0-v_{0}dt
$$

整理得:

$$
\begin{aligned}
\frac{a}{2\pi}\sqrt{\theta^2+1}d\theta&=-v_{0}dt\\
\frac{a}{2\pi}\int_{\theta_{0}(0)}^{\theta_{0}(t)}\sqrt{1+\theta^2}d\theta&=-v_{0}t
\end{aligned}
$$

对于$\int\sqrt{\theta^2+1}d\theta$用一下解法:

$$
\begin{aligned}
\theta &= tant\\
d\theta &= d(tant)\\
\int\sqrt{\theta^2+1}d\theta&=\int sectd(tant)\\
&=\int sec^3tdt
\\&=sect\cdot tant-\int tan^2t\cdot sectdt \\ &=sect\cdot tant-\int sec^3t-sectdt\\&=sect\cdot tant-\int sec^3tdt+\int sectdt
\\&=sect\cdot tant-\int sec^3tdt+ln(sect+tant)\\
\int sec^3tdt &= \frac{1}{2}(sect \cdot tant +ln(set+tant)) +C
\\&=\frac{1}{2}\sqrt{1+\theta^2}+\frac{1}{2}ln(\sqrt{\theta^2+1}+\theta)+c
\end{aligned}
$$

则,有

$$
\begin{aligned}
\frac{a}{2\pi}\int_{\theta_{0}(0)}^{\theta_{0}(t)}\sqrt{1+\theta^2}d\theta&=\frac{a}{2\pi}
\frac{1}{2}\sqrt{1+\theta_{0}(t)^2}+\frac{1}{2}ln(\sqrt{\theta_{0}(t)^2+1}+\theta_{0}(t))\\
&-\frac{a}{2\pi}\frac{1}{2}\sqrt{1+\theta_{0}(0)^2}-\frac{1}{2}ln(\sqrt{\theta_{0}(0)^2+1}+\theta_{0}(0))\\&=-v_{0}t
\end{aligned}
$$

利用该公式可以求出每一个时刻$\theta_{0}$的极角.
