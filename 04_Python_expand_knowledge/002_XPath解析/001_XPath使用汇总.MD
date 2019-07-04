# 1. XPath
- XPath 是一门在 XML 文档中查找信息的语言。XPath 可用来在 XML 文档中对元素和属性进行遍历。
- XPath 是 W3C XSLT 标准的主要元素，并且 XQuery 和 XPointer 都构建于 XPath 表达之上。
- 参考博客
    http://www.w3school.com.cn/xpath/index.asp
    http://www.w3school.com.cn/xpath/xpath_syntax.asp
    
- 以下内容参考books.xml查看

- XPath节点   
    - 在 XPath 中，有七种类型的节点：元素、属性、文本、命名空间、处理指令、注释以及文档（根）节点。
    - XML 文档是被作为节点树来对待的。树的根被称为文档节点或者根节点。    
        <bookstore> （文档节点）
        <author>J K. Rowling</author> （元素节点）
        lang="en" （属性节点）
    - 元素就相当于HTML中的标签
        
- 基本值（或称原子值，Atomic value）
    J K. Rowling
    "en"


- 语法
    - nodename	选取此节点的所有子节点。
    - /	从根节点选取，/符号连续使用就是逐级向下选择（最大的根标签html标签）
    - //	从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。
    - .	选取当前节点。
    - ..	选取当前节点的父节点。
    - @	选取属性。
    - ./ 从当前节点的根节点开始选取，
        - 比如先找到了很多DIV标签，然后遍历DIV标签，从DIV标签下面子标签

- 用法实例
    bookstore	选取 bookstore 元素的所有子节点。
    /bookstore	选取根元素 bookstore。
    
    注释：假如路径起始于正斜杠( / )，则此路径始终代表到某元素的绝对路径！
    
    bookstore/book	选取属于 bookstore 的子元素的所有 book 元素。
    //book	选取所有 book 子元素，而不管它们在文档中的位置。
    bookstore//book	选择属于 bookstore 元素的后代的所有 book 元素，而不管它们位于 bookstore 之下的什么位置。
    //@lang	选取名为 lang 的所有属性

- 路径添加谓语
    / 配合元素位置使用
    // 配合元素属性使用
    /bookstore/book[1]	选取属于 bookstore 子元素的第一个 book 元素。
    /bookstore/book[last()]	选取属于 bookstore 子元素的最后一个 book 元素。
    /bookstore/book[last()-1]	选取属于 bookstore 子元素的倒数第二个 book 元素。
    /bookstore/book[position()<3]	选取最前面的两个属于 bookstore 元素的子元素的 book 元素。
    //title[@lang]	选取所有拥有名为 lang 的属性的 title 元素。
    //title[@lang='eng']	选取所有 title 元素，且这些元素拥有值为 eng 的 lang 属性。
    /bookstore/book[price>35.00]	选取 bookstore 元素的所有 book 元素，且其中的 price 元素的值须大于 35.00。
    /bookstore/book[price>35.00]/title	选取 bookstore 元素中的 book 元素的所有 title 元素，且其中的 price 元素的值须大于 35.00

- 选取未知节点
    *	匹配任何元素节点。
    @*	匹配任何属性节点。
    node()	匹配任何类型的节点。
    
    /bookstore/*	选取 bookstore 元素的所有子元素。
    //*	选取文档中的所有元素。
    //title[@*]	选取所有带有属性的 title 元素
    
    下面实例选取的结果相同，因为id='novelInfo'属性的元素是唯一的
    *代表选取文档中的所有元素，*[@id='novelInfo']选取文档所有id属性为novelInfo的元素
    novelAllClick = response.xpath(".//*[@id='novelInfo']/table/tr[2]/td[1]/text()").extract_first()
    选取所有拥有id为novelInfo的属性的 div 元素
    novelAllClick = response.xpath(".//div[@id='novelInfo']/table/tr[2]/td[1]/text()").extract_first()
    
- 选取若干路径
    - 通过在路径表达式中使用“|”运算符，您可以选取若干个路径
    //book/title | //book/price	选取 book 元素的所有 title 和 price 元素。
    //title | //price	选取文档中的所有 title 和 price 元素。
    /bookstore/book/title | //price	选取属于 bookstore 元素的 book 元素的
    所有 title 元素，以及文档中所有的 price 元素。

- 参考ch12中cnblogSpider中XPath的使用
- 参考ch17中yunqishuyuan中XPath的使用     
    
- XPath开发工具
    - 开源的XPath表达式工具：XMLQire
    - chrome插件：XPath Helper
    - Firefox插件：XPath Checker（新版已经没有了该插件）
    
- Firefox使用XPath:
- 方法1：
    - xPath Finder
    - 附加组件中安装该插件，然后点击插件，鼠标放到要寻找的元素上面点击一下，
    - 左下角就会显示XPath的路径
    - 参考图片xPath Finder.png图片
- 方法2：
    - 以百度首页上方的新闻为例，先右键打开查看元素，
    - 然后右键新闻，查看元素，此时查看器中已经定位到新闻这个元素的位置
    - 然后查看器中，右键，复制，XPath即可复制出来路径
    - 可以对比两种方法结果一样
- 只需要路径，直接使用方法1，向具体查看源代码，使用方法2
- 方法2还可以复制CSS路径
- 百度首页新闻
    - XPath路径：/html/body/div[1]/div[1]/div/div[3]/a[1]
    - CSS路径：html body div#wrapper div#head div.head_wrapper div#u1 a.mnav
    - XPath更加简洁明了

- Firefox中有一个Try Path插件，用来验证XPath路径是否正确
    - 比如查找一个页面所有的文章
    - 以七夜博客第一页：https://www.cnblogs.com/qiyeboy/default.html?page=1
    - 作为例子，先看ch12中七夜博文规律分析的图片
    - 第一步输入表达式，就可以匹配到所有符合规律的元素（标签），蓝色虚线显示
    - 第二步，向下滚动，可以选择查看每一个元素

- 也可以使用bs4，参考ch12中sht中bs4的使用