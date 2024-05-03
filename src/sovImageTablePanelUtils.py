import numpy as np
from PySide6.QtGui import QImage, QPixmap


def get_qthumbnail_from_array(thumb_array):
    auto_range = np.quantile(thumb_array, [0.1, 0.9])
    thumb_array = np.clip(thumb_array, auto_range[0], auto_range[1])
    thumb_array = (
        (thumb_array - auto_range[0]) / (auto_range[1] - auto_range[0]) * 255
    ).astype(np.uint8)
    thumb_image = QImage(
        thumb_array.data,
        thumb_array.shape[1],
        thumb_array.shape[0],
        thumb_array.strides[0],
        QImage.Format_Grayscale8,
    )
    thumb_pixmap = QPixmap.fromImage(thumb_image).scaled(100, 100)
    return thumb_pixmap
