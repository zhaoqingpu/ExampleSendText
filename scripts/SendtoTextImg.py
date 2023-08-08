import contextlib

import gradio as gr
from modules import scripts

def send_text_to_prompt(new_text, old_text):
    if old_text == "":
        return new_text
    return old_text + ", " + new_text  # 如果不为空就拼接到末尾

class ExampleScript(scripts.Script):
    def __init__(self) -> None:
        super().__init__()


    #组件的title
    def title(self):
        return "测试插件"


    #组件默认显示状态
    def show(self, is_img2img):
        return scripts.AlwaysVisible


    #组件初始化UI
    def ui(self, is_img2img):
        with gr.Group():
            with gr.Accordion("测试插件", open=False):
                send_text_button = gr.Button(value='发送文本', variant='primary')
                text_to_be_sent = gr.Textbox(label="文本内容")

        with contextlib.suppress(AttributeError):
            if is_img2img:
                # 根据当前的Tab来设置点击后数据输出的组件
                send_text_button.click(fn=send_text_to_prompt, inputs=[text_to_be_sent, self.boxxIMG], outputs=[self.boxxIMG])
            else:
                # 根据当前的Tab来设置点击后数据输出的组件
                send_text_button.click(fn=send_text_to_prompt, inputs=[text_to_be_sent, self.boxx], outputs=[self.boxx])

        return [text_to_be_sent, send_text_button]

    #组件调用后，判断组件是否是txt2img_prompt或者img2img_prompt，prompt赋值到组件显示。
    def after_component(self, component, **kwargs):
        if kwargs.get("elem_id") == "txt2img_prompt":
            self.boxx = component
        if kwargs.get("elem_id") == "img2img_prompt":
            self.boxxIMG = component








