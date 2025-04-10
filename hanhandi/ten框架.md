TEN 框架其实有三部分组成，底层叫 TEN Framework，由 C、Rust 和 Go 写成，我看了一下源代码，但还没有学会怎么编译。如果你不开发底层，好像也不需要编译。

大部分人其实不需要改 TEN Framework，我这些天主要折腾的也都是 TEN Agent，这也是第二部分，大家可以在这里面写插件。TEN 的神奇之处是你可以使用 Python、Go、C++ 等语言写插件，并通过 Graph Designer（或 JSON）把这些插件串联起来，组成一个图（Graph），然后不同语言写得插件甚至可以在同一个进程中运行！

第三部分就是上面说的 Graph Designer。日后，更多的开发者其实只需要会 Graph Designer 就好了，然后就可以组合出不同的对话流程。如果 Graph Designer 成熟了，TEN Agent 里面的插件丰富了，也许就不需要我们这些开发者了。