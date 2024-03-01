class RapidOCR:
    def __init__(
        self,
        text_score: float = 0.5,
        print_verbose: bool = False,
        min_height: int = 30,
        width_height_ratio: float = 8,
        det_use_cuda: bool = False,
        det_model_path: Optional[str] = None,
        det_limit_side_len: float = 736,
        det_limit_type: str = "min",
        det_thresh: float = 0.3,
        det_box_thresh: float = 0.5,
        det_unclip_ratio: float = 1.6,
        det_donot_use_dilation: bool = False,
        det_score_mode: str = "fast",
        cls_use_cuda: bool = False,
        cls_model_path: Optional[str] = None,
        cls_image_shape: List[int] = [3, 48, 192],
        cls_label_list: List[str] = ["0", "180"],
        cls_batch_num: int = 6,
        cls_thresh: float = 0.9,
        rec_use_cuda: bool = False,
        rec_model_path: Optional[str] = None,
        rec_img_shape: List[int] = [3, 48, 320],
        rec_batch_num: int = 6,
    ):
        pass

engine = RapidOCR()

res, elapse = engine(img, use_det=True, use_cls=True, use_rec=True)