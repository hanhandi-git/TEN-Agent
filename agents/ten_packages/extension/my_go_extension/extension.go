package extension

import (
    "fmt"
    "ten_framework/ten"
)

const (
    textDataTextField = "text"
    textDataFinalField = "is_final"
    textDataEndOfSegmentField = "end_of_segment"
)

type myGoExtension struct {
    ten.DefaultExtension
}

func newExtension(name string) ten.Extension {
    return &myGoExtension{}
}

// OnStart 在扩展启动时调用
func (p *myGoExtension) OnStart(tenEnv ten.TenEnv) {
    tenEnv.LogInfo("MyGoExtension started")
    
    // 读取配置属性
    greeting, err := tenEnv.GetPropertyString("greeting")
    if err != nil {
        tenEnv.LogWarn(fmt.Sprintf("Failed to get greeting property: %v", err))
        greeting = "Default greeting"
    }
    
    // 发送一个示例数据
    data, _ := ten.NewData("text_data")
    data.SetPropertyString(textDataTextField, greeting)
    data.SetPropertyBool(textDataEndOfSegmentField, true)
    tenEnv.SendData(data)
    
    tenEnv.OnStartDone()
}

// OnData 处理接收到的数据
func (p *myGoExtension) OnData(tenEnv ten.TenEnv, data ten.Data) {
    text, err := data.GetPropertyString(textDataTextField)
    if err != nil {
        tenEnv.LogWarn(fmt.Sprintf("OnData GetProperty %s error: %v", textDataTextField, err))
        return
    }
    
    tenEnv.LogInfo(fmt.Sprintf("Received text: %s", text))
    
    // 处理文本并回复
    response := fmt.Sprintf("You said: %s", text)
    responseData, _ := ten.NewData("text_data")
    responseData.SetPropertyString(textDataTextField, response)
    responseData.SetPropertyBool(textDataEndOfSegmentField, true)
    tenEnv.SendData(responseData)
}

// OnCmd 处理接收到的命令
func (p *myGoExtension) OnCmd(tenEnv ten.TenEnv, cmd ten.Cmd) {
    cmdName := cmd.GetName()
    tenEnv.LogInfo(fmt.Sprintf("Received command: %s", cmdName))
    
    if cmdName == "hello" {
        cmdResult, _ := ten.NewCmdResult(ten.StatusCodeOK)
        cmdResult.SetPropertyString("message", "Hello from Go extension!")
        tenEnv.ReturnResult(cmdResult, cmd)
    } else {
        cmdResult, _ := ten.NewCmdResult(ten.StatusCodeError)
        tenEnv.ReturnResult(cmdResult, cmd)
    }
}

// OnStop 在扩展停止时调用
func (p *myGoExtension) OnStop(tenEnv ten.TenEnv) {
    tenEnv.LogInfo("MyGoExtension stopped")
    tenEnv.OnStopDone()
}

func init() {
    // 注册扩展
    ten.RegisterAddonAsExtension(
        "my_go_extension",
        ten.NewDefaultExtensionAddon(newExtension),
    )
}
