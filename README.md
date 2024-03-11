# Pencil Sketch Module

This Python module converts an RGB image into a pencil sketch using OpenCV.

## Installation

To use this module, you need to have OpenCV installed. You can install it using pip:

```sh
pip install opencv-python
```

## Usage

```python
from pencil_sketch import pencil_sketch

# Replace "path/to/your/image.jpg" with the path to your RGB image file.
sketch = pencil_sketch("path/to/your/image.jpg")
cv2.imshow('Pencil Sketch', sketch)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
