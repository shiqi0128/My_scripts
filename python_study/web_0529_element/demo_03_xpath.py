"""xpath元素定位。

相比于 6 大元素定位方式，优势在于可以组合条件， 进行精准和灵活的定位。


//*[@id="kw"] 经过优化的相对路径
/html/body/div[1]/div[1]/div[5]/div/div/form/span[1]/input  绝对路径的表示方法

在自动化测试当中，很少用绝对定位。
因为绝对定位不稳定，

什么是相对路径// ，什么是绝对路径 /。
[] 代表谓语条件
@ 代表属性

//input[@id='kw']  ==> 找标签名叫做 input, 并且 id 属性== kw


组合多种属性条件：
//input[@name='wd' and @id='kw' and @class='s_ipt']

text 文本组合
//input[text()='']
//a[text()="新闻"]


函数 contains
//a[text()="新闻" and contains(@class, 'mnav')]





"""