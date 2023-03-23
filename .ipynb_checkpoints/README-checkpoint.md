# Python OpenCV for Calibrate HLS mask
### Detect logo by color space selection
- used HLS color space and threshold the HLS image to get only blue, red, and green colors
![mask_result](assets/result/mask_result.png)
- preprocess color space mask by dilation, erosion
![lego_result_color_space](assets/result/lego_result_color_space.png)

### Detect logo by edge(opencv canny)
- used canny to create edge
- preprocess edge mask by dilation, erosion
![lego_result_canny](assets/result/lego_result_canny.png)

### code on workspace
- Calibrate color Mask with adjustbar
- Apply to tracking object.