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
        - 比如先找到了很多DIV标签，然后遍历DIV标签，.就代表当前的的DIV标签，从DIV标签下面子标签开始选取
    - .// 从匹配当前节点的根节点开始选取，不管他们在文中的位置

- 用法实例
    bookstore	选取 bookstore 元素的所有子节点。
    /bookstore	选取根元素 bookstore。
    
    注释：假如路径起始于正斜杠( / )，则此路径始终代表到某元素的绝对路径！
    
    bookstore/book	选取属于 bookstore 的子元素的所有 book 元素。
    //book	选取所有 book 子元素，而不管它们在文档中的位置。
    bookstore//book	选择属于 bookstore 元素的后代的所有 book 元素，而不管它们位于 bookstore 之下的什么位置。
    //@lang	选取名为 lang 的所有属性

- 路径添加谓语
    / 配合元素位置使用，/逐级向下选取，如果只有一个直接逐级使用/,如果有多个就要使用位置book[1]
    // 配合元素属性使用
    /bookstore/book 选取属于 bookstore 子元素的下一级的所有book 子元素。
    /bookstore//book 选取属于 bookstore 子元素的下的所有book 子元素。
    /bookstore/book[1]	选取属于 bookstore 子元素的第一个 book 元素。
    /bookstore/book[2]	选取属于 bookstore 子元素的第二个 book 元素。
    /bookstore/book[last()]	选取属于 bookstore 子元素的最后一个 book 元素。
    /bookstore/book[last()-1]	选取属于 bookstore 子元素的倒数第二个 book 元素。
    /bookstore/book[position()<3]	选取最前面的两个属于 bookstore 元素的子元素的 book 元素。
    //title[@lang]	选取所有拥有名为 lang 的属性的 title 元素。
    //title[@lang='eng']	选取所有 title 元素，且这些元素拥有值为 eng 的 lang 属性。
    
    - 条件语句
    /bookstore/book[price>35.00]	选取 bookstore 元素的所有 book 元素，且其中的 price 元素的值(标签里面的内容)须大于 35.00。
    /bookstore/book[price>35.00]/title	选取 bookstore 元素中的 book 元素的所有 title 元素，且其中的 price 元素的值须大于 35.00
    //cell//data[text()=200 and @type="Number2"]/text()  data的内容是200和type属性是Number2的元素

- 选取未知节点
    *	匹配任何元素节点。
    @*	匹配任何属性节点。
    node()	匹配任何类型的节点。
    
    /bookstore/*	选取 bookstore 元素的所有子元素。
    //*	选取文档中的所有元素。
    //title[@*]	选取所有带有属性的 title 元素
    //title[@id='novelInfo'] 选取所有拥有id为novelInfo的属性的title元素
    
    下面实例选取的结果相同，因为id='novelInfo'属性的元素是唯一的
    *代表选取文档中的所有元素，*[@id='novelInfo']选取文档所有id属性为novelInfo的元素
    novelAllClick = response.xpath(".//*[@id='novelInfo']/table/tr[2]/td[1]/text()").extract_first()
    选取所有拥有id为novelInfo的属性的 div 元素
    novelAllClick = response.xpath(".//div[@id='novelInfo']/table/tr[2]/td[1]/text()").extract_first()
    
- 选取若干路径
    - 通过在路径表达式中使用“|”运算符，您可以选取若干个路径
    //book/title | //book/price	
    选取 book 元素的所有 title 和 price 元素。
    //title | //price	
    选取文档中的所有 title 和 price 元素。
    /bookstore/book/title | //price	
    选取属于 bookstore 元素的 book 元素的下面的title 元素，以及文档中所有的 price 元素。

   
    
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

- XPath
- 参考ch12中cnblogSpider中XPath的使用
- 参考ch17中yunqishuyuan中XPath的使用 
- 参考TZKT项目中的相关使用XPath的案例


- 难点补充1：
- / // ./ ../ .//的区别
- / 引入绝对位置路径，从文档的根开始。比如/book，只会文档中的book标签节点开始向下查找。
- // 从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置
- . 从上下文节点开始引入相对位置路径。点称为“上下文项表达式”，找的是相对路径，和python中的文件路径一样，会找父级和子级。如果在表达式的开头加上一个点，它将使其特定于上下文。换句话说，它将id="Passwd"在您调用“通过XPath查找元素”方法的节点的上下文中搜索元素。
- ./ 从选定的当前节点开始向下查找
- ../ 选取当前节点的父节点开始向下查找
- .// 从选择的当前节点处开始，向下查找，不管在文中的位置
- 补充：.主要是为了引入上下文，相对路径，如果使用了.就表示从当前节点下开始
- 参考：http://www.imooc.com/wenda/detail/579577
- 实际数据解析中，都是选选定了文档，然后从当前文档的根节点开始，比如
    - 一级文档：response，提取出二级内容：jobs，然后再每个jobs里面继续提取jobname
    - jobs = response.xpath(".//div[@id='resultList']//div[@class='el']")
    - jobName = job.xpath("./p/span/a/text()").extract_first().strip()
 
 
- 难点补充2：   
- lxml中的XPath和Scrapy中selector下的XPath提取元素语法有不同：
    - 参考002和003案例
    - 补充参考
    - 参考TZKT中的P02和P03项目
    - XPath中
    for job in jobs:
        # 匹配结果仍然是一个列表类型,列表中只有一个元素，提取元素并去掉里面的空格
        # scrapy使用的selector中的xpath不能用这种[0].strip()列表语法，使用extract()提取所有内容为一个列表,extract_first()提取第一个列表元素
        # 从当前的job下开始选取
        name = job.xpath("./p/span/a/text()")[0].strip()
    - scrapy中
     for job in jobs:
        # 匹配结果仍然是一个列表类型,列表中只有一个元素，
        # P02中已经提取过，发现里面有很多空格，提取第一个元素的值并去掉里面的空格
        # 注意P02使用的是etree.HTML解析源码，提取元素可以使用列表语法，该处selector下的xpath不可以
        jobName = job.xpath("./p/span/a/text()").extract_first().strip()
        

- 难点补充3：
描述一下XML lxml XPath之间有什么关系？
- XML是一种类似html的标记语言
- lxml是python的一个解析库，支持HTML和XML的解析
- XPath，全称XML Path Language，即XML路径语言，它是一门在XML文档中查找信息的语言，它最初是用来搜寻XML文档的，但是它同样适用于HTML文档的搜索
- 使用步骤：请求网页获取的text文本内容，使用lxml解析为XML语言，然后使用XPath查找；
- 请求网页获取到的bytes内容，可以使用BeautifulSoup4(bs4也可以传入字符串，bs4会根据传入类型自己识别解码)，解析模块可以选择lxml进行解析，然后查找.