
### QRCODE(Version:2 ErrorCorrectionLevel:Q)
#### by teeSngRovn
------
* `__QRPaint__.py`用于最后整合其它文件并绘图
* `AlphaCode_generator.py`是用于生成伽罗瓦域中$\alpha^x$及其对应值
* `FormatCode_Generator`是用于计算格式编码的小模块，不被其他文件调用
* `CorrectionCode.py`是用于计算纠错码生成多项式的模块
* `Encode.py`用于数据码与纠错码的计算及整合，并确定`QRversion`和`ErrorCorrection Level`
#### 注：
* 在绘图时调用了`opencv-python`的`cv2`
* 在生成像素矩阵时调用了`numpy`来预处理像素矩阵

-----
* 独立运行绘图:
``` shell
 python __QRPaint__.py

 >>>Enter(LETTERS IN UPPERCASE):
    123ABD
```

* 作为模块导入时:
``` python
import __QRPaint__

# __QRPaint__.paint(string A)
__QRPaint__.paint('123')

```
---
# 总结反思
1. 你觉得解决这个任务的过程有意思吗？
> 感觉还行挺有意思，特别是图形出来的时候有点爽，就是通宵肝有点难受
2. 你在网上找到了哪些资料供你学习？
> 见最后参考文档
3. 你觉得去哪里/用什么方式搜索可以比较有效的获得自己想要的资料？
> baidu,上简书和一些CSDN博客
4. 在过程中，你遇到最大的困难是什么？你是怎么解决的？
> 纠错码的生成，平常不写算法，多项式展开只会暴力计算，后来真的暴算出来了
5. 完成任务之后，再回去阅读你写下的代码和文档，有没有看不懂的地方？如果再过一年，你觉得那时你还可以看懂你的代码吗？
> 现在能看懂，一年后不一定，因为现在写的和屎山一样，命名不够清晰。以后写的话可以对一些模块进行修改(比如加点对象)，这样互相调用时命名可以更加清楚。同样可以多写点注释让人更好理解
6. 在完成任务之后，如果要求你在已写好的代码基础上再加入生成 version 3~40 的二维码的功能，你是否会选择重新规划代码结构并重写大部分代码？
> 我的数据编码部分可以不用更改，但是绘图部分会有大问题。我的绘图框架是手动生成的，没有自动化。要改成多version的话要对预生成填充矩阵和格式信息位置的部分进行更改
7. 其他想说的想法或者建议。
> 这个纠错码生成部分感觉应该在前面的QRCODE标准的表格中把纠错等级对应的纠错码数目给写出来，网上找了好久才找到
----
# 参考文档
* [二维码的实现原理和实现过程](https://blog.csdn.net/bosaidongmomo/article/details/103232449)
* [纠错码生成细节和原理](https://www.cnblogs.com/txqdm/p/8629661.html)
* [QR TUTORIAL](https://www.thonky.com/qr-code-tutorial/)
* [二维码生成原理](https://blog.csdn.net/ajianyingxiaoqinghan/article/details/78837864)
