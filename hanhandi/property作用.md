



# TEN 框架中 property.json 文件的作用

在 TEN 框架中，`property.json` 文件扮演着非常重要的角色，它有以下几个主要作用：

## 1. 扩展配置

对于扩展目录中的 `property.json`（如您的 `agents/ten_packages/extension/my_python_extension/property.json`）：

- 定义扩展的默认配置参数
- 这些参数可以在扩展的 `on_start` 或其他生命周期方法中通过 `ten.get_property_xxx()` 方法读取
- 例如，您的扩展中定义的 `"greeting": "Hello from my Python extension!"` 可以通过 `ten.get_property_string("greeting")` 读取

## 2. 运行时配置覆盖

当扩展被集成到代理中时：

- 代理的 `property.json` 中可以覆盖扩展的默认配置
- 例如，在代理的 `property.json` 中可以为您的扩展指定不同的 greeting 值
- 这使得同一个扩展可以在不同的代理中有不同的行为

## 3. 图形定义（代理级别）

在代理级别的 `property.json` 中：

- 定义了扩展节点之间的连接关系，形成一个处理图（Graph）
- 指定了每个扩展节点的配置参数
- 控制了数据和命令的流动路径

## 4. 示例：代理级别的 property.json

代理级别的 `property.json` 通常包含一个 `_ten` 字段，定义了处理图：

```json
{
  "_ten": {
    "predefined_graphs": [
      {
        "name": "my_custom_graph",
        "auto_start": true,
        "nodes": [
          {
            "type": "extension",
            "name": "my_extension",
            "addon": "my_python_extension",
            "extension_group": "default",
            "property": {
              "greeting": "Hello from my custom agent!" // 覆盖扩展默认值
            }
          }
        ]
      }
    ]
  }
}
```

## 5. 动态配置

`property.json` 还支持动态配置：

- 可以在运行时通过 API 或 Graph Designer 界面修改
- 修改后的配置会影响扩展的行为，无需重启
- 这使得系统具有高度的灵活性和可配置性

## 6. 与 manifest.json 的关系

`property.json` 与 `manifest.json` 密切相关：

- `manifest.json` 定义了扩展支持哪些属性（property）及其类型
- `property.json` 则提供了这些属性的具体值
- 系统会根据 `manifest.json` 中的定义验证 `property.json` 中的值

## 总结

`property.json` 文件是 TEN 框架中的核心配置文件，它：

1. 为扩展提供默认配置参数
2. 允许代理覆盖扩展的默认配置
3. 定义扩展节点之间的连接关系
4. 支持动态配置，提高系统灵活性
5. 与 `manifest.json` 配合，形成完整的扩展定义和配置机制

通过这种设计，TEN 框架实现了高度模块化和可配置的架构，使得不同语言编写的扩展可以在同一个处理图中协同工作。
