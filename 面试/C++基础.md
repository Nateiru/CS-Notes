#### C++中指针和引用的区别

1. 指针有自己的一块空间，而引用只是一个别名；
2. 使用 sizeof 看一个指针的大小为4字节（32位，如果要是64位的话指针为8字节），而引用则是被引用对象的大小；
3. 指针可以被初始化为 NULL，而引用必须被初始化且必须是一个已有对象的引用；
4. 作为参数传递时，指针需要被解引用才可以对对象进行操作，而直接对引用的修改都会改变引用所指向的对象；
5. 指针在使用中可以指向其他对象，但是引用只能是一个对象的引用，不能被改变；
6. 指针可以是多级，而引用没有分级；
7. 如果返回动态分配内存的对象或者内存，必须使用指针，引用可能引起内存泄漏。

**引用占用内存空间吗？** 对引用取地址，其实是取的引用所对应的内存空间的地址。这个现象让人觉得引用好像并非一个实体。但是引用是占用内存空间的，而且其占用的内存和指针一样，因为引用的内部实现就是通过指针来完成的。

#### 四种类型转换

- `static_cast`：用于良性转换，一般不会导致意外发生，风险很低。常用于基本类型转换到 void，转换父类指针到子类不安全；

- `const_cast`：一般用于去掉const属性以及volatile，但是如果原来他就是**常量去掉之后千万不要修改**；比如你手里有一个常量指针引用，但是函数接口是非常量指针，可能需要转换一下；成员函数声明为const，你想用this去执行一个函数，也需要用 `const_cast`；

- `dynamic_cast`：用于在类的继承层次之间进行类型转换，它既允许向上转型（Upcasting），也允许向下转型（Downcasting）。向上转型是无条件的，不会进行任何检测，所以都能成功；向下转型的前提必须是安全的，要借助 RTTI 进行检测，所有只有一部分能成功；

- `reinterpret_cast`：重新解释转换是将一个指针或引用转换为另一个类型的指针或引用，通常用于底层编程，如将指针转换为整数。重新解释转换是最不安全的转换方式，可能会引发未定义行为，用于序列化网络包数据等。

#### C++中的容器了解多少

一个容器是特定类型对象的集合，在C++标准库中包含了大部分常见的容器。STL 是“Standard Template Library”的缩写，中文译为“标准模板库”。STL 是 C++ 标准库的一部分，不用单独安装。TSL核心包括3个组件。容器(containers)，算法(algorithms)，迭代器(iterators)。除此外还有仿函数，内存配置器和配接器。

- 序列式容器（Sequence containers）：此为可序群集，其中每个元素均有固定位置—取决于插入时机和地点，和元素值无关。如果你以追加方式对一个群集插入六个元素，它们的排列次序将和插入次序一致。STL提供了三个序列式容器：向量（vector）、双端队列（deque）、列表（list），此外你也可以把 string 和 array 当做一种序列式容器。
- 关联式容器（Associative containers）：此为已序群集，元素位置取决于特定的排序准则以及元素值，和插入次序无关。如果你将六个元素置入这样的群集中，它们的位置取决于元素值，和插入次序无关。STL提供了四个关联式容器：集合（set）、多重集合（multiset）、映射（map）和多重映射（multimap）。

对于容器，主要的操作有：容器的建立、插入元素、删除元素、查询、遍历、计算元素个数、检查元素是否为空、输出容器包含的内容。

#### C++17的新特性

1. **结构化绑定（Structured bindings）**：允许从元组、数组、结构体等类型的数据中提取数据成员，并将其绑定到变量上。

```cpp
struct Point {
    int x;
    int y;
};
Point p{1, 2};
auto [x, y] = p;
std::cout << "x = " << x << ", y = " << y << std::endl;
```

2. **条件表达式/选择中支持初始化语句**

```cpp
// c++17
map<int, string> c = {{1,"a"}};
// 条件表达式支持初始化语句 if (init; condition)
if(auto res = c.insert(make_pair(2, "b")); !res.second ) {
    cout << "key 1 exist" << endl;
} else {
    cout << "insert success, value:" << res.first->second << endl;
}
// 同时支持选择 switch (init; condition)
```

3. **折叠表达式**：简化一些复杂的表达式，可以将一系列的表达式进行“折叠”成一个结果

折叠表达式的基本形式为：

```R
(expression op ...)
(... op expression)
```

其中，`expression`是一个可变参数包，`op`是一个二元操作符。

折叠表达式有两种形式：左折叠和右折叠。左折叠是指先对前两个表达式进行操作，然后将结果与下一个表达式继续操作，一直到最后一个表达式为止。右折叠则是从最后一个表达式开始，依次与前面的表达式进行操作，直到第一个表达式为止。

以求和操作为例，假设我们有一个可变参数包`args`，我们可以使用左折叠表达式来计算它们的和：

```cpp
// 将参数包args中的所有参数依次相加
template<typename... Args>
auto sum(Args... args) {
    return (args + ...); // 左折叠求和
}
```

4. **constexpr lambda表达式**：C++17前lambda表达式只能在运行时使用，C++17引入了constexpr lambda表达式，可以用于在编译期进行计算。

```cpp
int main() { // c++17可编译
    constexpr auto lamb = [] (int n) { return n * n; };
    static_assert(lamb(3) == 9, "a");
}
```

5. **lambda表达式用*this捕获对象副本**

正常情况下，lambda表达式中访问类的对象成员变量需要捕获this，但是这里捕获的是this指针，指向的是对象的引用，正常情况下可能没问题，但是如果多线程情况下，函数的作用域超过了对象的作用域，对象已经被析构了，还访问了成员变量，就会有问题。

```cpp
#include <iostream>
#include <thread>
#include <vector>

class Foo {
public:
    Foo(int val): m_val(val) {}

    void doSomething() {
        std::thread t([this] {
            std::cout << "Thread ID: " << std::this_thread::get_id() << ", m_val = " << m_val << std::endl;
        });
        t.detach();
    }

private:
    int m_val;
};

int main() {
    std::vector<Foo> foos;
    foos.emplace_back(1);
    foos.emplace_back(2);
    foos.emplace_back(3);

    for (auto& foo : foos) {
        foo.doSomething();
    }

    // Wait for all threads to complete
    std::this_thread::sleep_for(std::chrono::seconds(1));

    return 0;
}

```

在上面的例子中，我们定义了一个`Foo`类，其中包含一个`int`类型的成员变量`m_val`，和一个成员函数`doSomething()`。在`doSomething()`函数中，我们创建了一个新线程，其中我们使用了Lambda表达式来打印当前线程的ID和`m_val`的值，Lambda表达式中捕获了`this`指针。

在`main()`函数中，我们创建了一个`std::vector<Foo>`，并向其中添加了三个`Foo`对象，分别使用`1`，`2`和`3`来初始化它们的成员变量`m_val`。接下来，我们使用`for`循环遍历这些对象，并分别调用它们的`doSomething()`函数来启动一个新线程。

但是，由于在创建新线程后，我们立即将其分离，所以这些线程可能在`main()`函数完成之前就完成了。如果这样，`Foo`对象的生命周期将结束，`this`指针将成为悬空指针，而当新线程访问`m_val`成员变量时，就会发生未定义行为。

因此，在使用Lambda表达式访问类的成员变量时，必须确保类对象的生命周期长于Lambda表达式。

所以C++17增加了新特性，捕获*this，不持有this指针，而是持有对象的拷贝，这样生命周期就与对象的生命周期不相关了。

```cpp
struct A {
    int a;
    void func() {
        auto f = [*this] { // 这里
            cout << a << endl;
        };
        f();
    }  
};
int main() {
    A a;
    a.func();
    return 0;
}
```

####  如何实现编译期间算n的阶乘？

#### 如何实现无锁队列

#### 如何实现一个string类