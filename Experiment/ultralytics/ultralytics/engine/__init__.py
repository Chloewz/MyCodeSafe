# Ultralytics YOLO 🚀, AGPL-3.0 license
# * engine文件夹包含与模型训练、评估和推理有关的核心代码
# *     --exporter.py 用于将训练好的模型导出到其他格式，如ONNX或TensorRT
# *     --model.py 包含模型定义、模型初始化和加载的方法
# *     --predictor.py 包含推理和预测的逻辑，如加载模型并对输入数据进行预测
# *     --results.py 用于存储和处理模型输出的结果
# *     --trainer.py 包含模型训练过程的逻辑
# *     --tuner.py 用于模型超参数调优
# *     --validator.py 包含模型验证的逻辑，如在验证集上评估模型性能