from ten import Extension, TenEnv, Data, Cmd, CmdResult, StatusCode

class MyPythonExtension(Extension):
    def __init__(self, name: str):
        super().__init__(name)
        
    def on_init(self, ten: TenEnv) -> None:
        ten.log_info("MyPythonExtension initialized")
        ten.on_init_done()
        
    def on_start(self, ten: TenEnv) -> None:
        ten.log_info("MyPythonExtension started")
        
        # 读取配置属性示例
        greeting = ten.get_property_string("greeting")
        ten.log_info(f"Greeting property: {greeting}")
        
        # 发送一个示例数据
        output_data = Data.create("text_data")
        output_data.set_property_string("text", greeting)
        output_data.set_property_bool("end_of_segment", True)
        ten.send_data(output_data)
        
        ten.on_start_done()
        
    def on_data(self, ten: TenEnv, data: Data) -> None:
        # 处理接收到的数据
        if data.get_name() == "text_data":
            text = data.get_property_string("text")
            ten.log_info(f"Received text: {text}")
            
            # 处理文本并回复
            response = f"You said: {text}"
            output_data = Data.create("text_data")
            output_data.set_property_string("text", response)
            output_data.set_property_bool("end_of_segment", True)
            ten.send_data(output_data)
    
    def on_cmd(self, ten: TenEnv, cmd: Cmd) -> None:
        cmd_name = cmd.get_name()
        ten.log_info(f"Received command: {cmd_name}")
        
        # 处理命令
        if cmd_name == "hello":
            cmd_result = CmdResult.create(StatusCode.OK)
            cmd_result.set_property_string("message", "Hello from Python extension!")
            ten.return_result(cmd_result, cmd)
        else:
            cmd_result = CmdResult.create(StatusCode.ERROR)
            ten.return_result(cmd_result, cmd)
    
    def on_stop(self, ten: TenEnv) -> None:
        ten.log_info("MyPythonExtension stopped")
        ten.on_stop_done()
        
    def on_deinit(self, ten: TenEnv) -> None:
        ten.log_info("MyPythonExtension deinitialized")
        ten.on_deinit_done()

# 注册扩展
def register_extension(name: str) -> Extension:
    return MyPythonExtension(name)
