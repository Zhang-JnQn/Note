<!-- @format -->

# How to make rt file

- ## 在本机 deep_learning/export_weight/darknet 文件夹下

  - ### mkdir layers debug
  - ### zsh export_layers_debug.sh（注意修改里面的 cfg、weight 路径）

&nbsp;

- ## 在车上 tkDNN/build 文件夹下

  - ### 将 layers debug 拷贝到 yoloTiny 文件夹下

&nbsp;

- ## 在车上 tkDNN/tests/darknet 文件夹下

  - ### 修改 yolo4Tiny.cpp（注意可能要替换 cfg 文件夹下的 yolo-obj-tiny.cfg 和 names 文件夹下的 obj.names）

&nbsp;

- ## 在车上 tkDNN/build 文件夹下

  - ### make
  - ### ./test\_<rt 文件名字> （./test_yolo4Tiny）
    - ### 回生成 rt 文件在 build 文件夹下

&nbsp;

- ## 在车上 tkdnn_ros 文件夹下
  - ### 查看 cfg 文件夹中的 ros_17.yaml 和 yolo4Tiny_17.yaml 是否需要修改
  - ### 将 tkDNN/build/yoloTiny 文件夹下的 layers、debug 文件夹以及 build 文件夹下的 rt 文件拷贝到 yolo_network_config 文件夹下
