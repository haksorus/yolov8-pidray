# YoloV8 PIDray detection
---


## **1) About work**
 
 **Automatic security inspection** relying on computer vision technology is a challenging task in real-world scenarios due to many factors, such as: 
 * intra-class variance, 
 * class imbalance,
 * occlusion. 
 
 Most previous methods rarely touch the cases where the prohibited items are deliberately hidden in messy objects because of the scarcity of large-scale datasets, hindering their applications. 
 
 To address this issue and facilitate related research, was presented a large-scale dataset, named [**PIDray**](https://arxiv.org/pdf/2211.10763.pdf), which covers various cases in real-world scenarios for prohibited item detection.
 
 
 <p align="center">
  <img src="https://user-images.githubusercontent.com/69139386/219473437-8500eccb-b761-4e85-b538-e4ac3b8d642b.png">
</p>

This dataset has three degrees of difficulty: **easy**, **hard**, **hidden**.

Also, the authors of the article presented their approach for the detection and segmentation of these items.

You can find it in [**original repo**](https://github.com/bywang2018/security-dataset).

## **2) Original approach**

According to the article, the author proposes the selective dense attention network (**SDANet**), formed by the dense attention module and the dependency refinement module.

This method has the following **metrics**:

<p align="center">
  <img src="https://user-images.githubusercontent.com/69139386/219476130-2d2f9921-a55d-49b8-8f55-8cc3e416b6b0.png">
</p>


## **3) Yolo approach**

For these case I`ve trained two detectors from [**ultralytics**](https://ultralytics.com/): new [**YoloV8**](https://github.com/ultralytics/ultralytics) and pretty old [**YoloV5**](https://github.com/ultralytics/yolov5). 

Both of them was trained on RTX 3090 for **300 epochs** and **batch size = 32**. 

To make the inference fast, I took a **S**mall version of Yolo.

The detectors were compared after training.

 <p align="center">
  <img src="https://user-images.githubusercontent.com/69139386/219468798-46598e11-0c0a-4985-b5ae-fc65468efca2.gif">
</p>

<p align="center">
  YoloV8s inference 
</p>


### **YoloV5s training results:**
---

![results](https://user-images.githubusercontent.com/69139386/219479548-a2d5020d-663a-4e0b-9371-958e47f49f4a.png)

### **YoloV8s training results:**
---
![results](https://user-images.githubusercontent.com/69139386/219482323-fe2e5770-ee79-422d-8093-e91f444657f4.png)

### **Comparison**
---

**As we can see, YoloV8s shows the mAP result better than YoloV5s by 11%. That`s very cool.**

| Method  | Easy mAP| Hard mAP|Hidden mAP|Overall mAP| Inference / ms (RTX 3090)| 
| ------------- | :---:  |:---:  |:---:  |:---:  |:---:  | 
| YoloV5s  | 0.738  |0.715  |0.493  | 0.648  |~6 ms/image | 
| **YoloV8s**  | **0.818**  |**0.78**  |**0.589**  |**0.729**  |**~6 ms/image**  |

**Moreover, light YoloV8s better than huge SDANet more than 15% (72.9 mAP vs 61.6 mAP)...**

mAP difference between YoloV8s and YoloV5s by each class in hidden subset:

![plot](https://user-images.githubusercontent.com/69139386/219493557-5150055d-b542-4f6f-a826-c59697295304.png)

# 4) Try it yourself
---
In my repository you can find everything you need to run YoloV8 on PIDray data. 

**The only thing you need is downloaded and converted from Coco-format to Yolo-format PIDray dataset**. You can download it from [original repo](https://github.com/bywang2018/security-dataset)

Also, before start you need to install [**ultralytics**](https://github.com/ultralytics/ultralytics):
```Python
pip install ultralytics
```
Now you can use pretrained YoloV8s weights from **weights** folder to predict or validate on PIDray data.

Check **demo.ipynb** for simple inference example using high-level ultralytics lib. 

If you want more, check [ultralytics YoloV8 docs](https://docs.ultralytics.com/).
