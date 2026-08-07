"""
    Project: Virtual Try-On

    Stage: 6
    Substage: 6.1 - Create Accessory Renderer

    Description:
    Accessory rendering module.
"""

# ===
# Stage 6.1
# Import libraries
# ===

import logging
import math
import os

import cv2

logger = logging.getLogger(__name__)

# ===
# Stage 6.3
# Face Mesh landmark indices
# ===

# Glasses

LEFT_EYE = 33
RIGHT_EYE = 263

# Hat

FOREHEAD = 10

TOP_LEFT_FOREHEAD = 67
TOP_RIGHT_FOREHEAD = 297

LEFT_HAIRLINE = 109
RIGHT_HAIRLINE = 338

# Mask

NOSE = 1
CHIN = 152

# Earrings

LEFT_EAR = 234
RIGHT_EAR = 454

GLASSES = "glasses"
HAT = "hats"
MASK = "masks"


# ===
# Stage 6.1
# Accessory Renderer
# ===

class AccessoryRenderer:
    """
    Accessory rendering module.
    """

    def __init__(self):
        """
        Initialize renderer.
        """

        self.scaled_cache = {}
        self.rotated_cache = {}
        self.cache = {}
        self.profile_enabled = True
        self.profile_counter = 0

    def get_cached_accessory(self, accessory_path):
        """
        Load accessory only once.
        """

        if accessory_path is None:
            return None

        if accessory_path not in self.cache:

            image = cv2.imread(
                accessory_path,
                cv2.IMREAD_UNCHANGED
            )

            image = self.trim_transparent(image)

            if image is None:
                logger.error(
                    "Cannot load accessory: %s",
                    accessory_path
                )

                return None

            if image.shape[2] != 4:
                logger.warning(
                    "Accessory has no alpha channel."
                )

                return None

            self.cache[accessory_path] = image

        return self.cache[accessory_path]

    # ===
    # Stage 6.1
    # Render accessory
    # ===

    def render(
            self,
            frame,
            accessory,
            landmarks,
            accessory_path
    ):
        """
        Render accessory on frame.

        Args:
            frame: OpenCV frame.
            accessory: PNG image.
            landmarks: Face landmarks.
            accessory_path: Path to accessory PNG file.

        Returns:
            OpenCV frame.
        """

        try:

            if (
                    frame is None
                    or accessory is None
                    or not landmarks
            ):
                return frame

            anchors = self.get_anchor_points(landmarks)

            if anchors is None:
                return frame

            if (
                    anchors["left_eye"] is None or
                    anchors["right_eye"] is None
            ):
                return frame

            face_width = abs(
                anchors["right_eye"][0] -
                anchors["left_eye"][0]
            )

            angle = self.calculate_angle(
                anchors["left_eye"],
                anchors["right_eye"]
            )

            eye_center = (
                (anchors["left_eye"][0] + anchors["right_eye"][0]) // 2,
                (anchors["left_eye"][1] + anchors["right_eye"][1]) // 2
            )

            # Face width

            accessory_type = self.get_accessory_type(accessory_path)

            accessory = self.get_cached_accessory(
                accessory_path
            )

            if accessory_type is None:
                return frame

            if accessory_type == GLASSES:
                return self.render_glasses(
                    frame,
                    accessory,
                    accessory_path,
                    face_width,
                    angle,
                    eye_center
                )

            elif accessory_type == HAT:
                return self.render_hat(
                    frame,
                    accessory,
                    anchors,
                    accessory_path,
                    face_width,
                    angle
                )

            elif accessory_type == MASK:
                return self.render_mask(
                    frame,
                    accessory,
                    accessory_path,
                    face_width,
                    angle,
                    eye_center
                )

            return frame

        except Exception as error:

            logger.error(
                "Accessory rendering failed: %s",
                error
            )
            return frame

    # ===
    # Stage 6.3
    # Get anchor points
    # ===

    def get_anchor_points(self, landmarks):
        """
        Get anchor landmarks for accessories.

        Args:
            landmarks: List of pixel landmarks.

        Returns:
            Dictionary with anchor points.
        """

        required = [
            LEFT_EYE,
            RIGHT_EYE,
            FOREHEAD,
            NOSE,
            CHIN,
            LEFT_EAR,
            RIGHT_EAR
        ]

        if len(landmarks) <= max(required):
            return None

        return {

            "left_eye": landmarks[LEFT_EYE],

            "right_eye": landmarks[RIGHT_EYE],

            "forehead": landmarks[FOREHEAD],

            "top_left": landmarks[TOP_LEFT_FOREHEAD],

            "top_right": landmarks[TOP_RIGHT_FOREHEAD],

            "hair_left": landmarks[LEFT_HAIRLINE],

            "hair_right": landmarks[RIGHT_HAIRLINE],

            "nose": landmarks[NOSE],

            "chin": landmarks[CHIN],

            "left_ear": landmarks[LEFT_EAR],

            "right_ear": landmarks[RIGHT_EAR]
        }

    # ===
    # Stage 6.4
    # Scale accessory
    # ===

    def scale_accessory(self, accessory, face_geometry, scale=1.0):
        """
        Scale accessory according to face size.

        Args:
            accessory: PNG image with alpha channel.
            face_geometry: Face geometry dictionary.
            scale: Additional scale factor.

        Returns:
            Resized accessory image.
        """

        if accessory is None:
            logger.error("Accessory image not loaded.")
            return accessory

        if face_geometry is None:
            return accessory

        face_width = face_geometry["width"]

        if face_width <= 0:
            return accessory

        target_width = max(
            1,
            int(face_width * scale)
        )

        height, width = accessory.shape[:2]

        aspect_ratio = height / width

        target_height = int(
            target_width * aspect_ratio
        )

        interpolation = (
            cv2.INTER_LINEAR
            if target_width > width
            else cv2.INTER_AREA
        )

        resized = cv2.resize(
            accessory,
            (target_width, target_height),
            interpolation=interpolation
        )

        return resized

    # ===
    # Stage 6.5
    # Calculate accessory position
    # ===

    def calculate_position(
            self,
            accessory,
            anchor_point,
            offset_x=0,
            offset_y=0,
            align="center"
    ):
        """
        Calculate top-left position for accessory.

        Args:
            accessory: Accessory image.
            anchor_point: (x, y) anchor point.
            offset_x: Horizontal offset.
            offset_y: Vertical offset.
            align: Alignment mode ("center", "top", or "bottom").

        Returns:
            (x, y) position.
        """

        if accessory is None:
            logger.error("Error: Accessory image not loaded.")
            return None

        if anchor_point is None:
            return None

        height, width = accessory.shape[:2]

        if align == "center":

            x = anchor_point[0] - width // 2 + offset_x
            y = anchor_point[1] - height // 2 + offset_y

        elif align == "top":

            x = anchor_point[0] - width // 2 + offset_x
            y = anchor_point[1] + offset_y

        elif align == "bottom":

            x = anchor_point[0] - width // 2 + offset_x
            y = anchor_point[1] - height + offset_y

        else:
            raise ValueError(f"Unknown alignment: {align}")

        return x, y

    # ===
    # Stage 6.6
    # Calculate rotation angle
    # ===

    def calculate_angle(
            self,
            left_eye,
            right_eye
    ):
        """
        Calculate head rotation angle.

        Args:
            left_eye: (x, y)
            right_eye: (x, y)

        Returns:
            Rotation angle in degrees.
        """

        if left_eye is None or right_eye is None:
            return 0.0

        dx = right_eye[0] - left_eye[0]
        dy = right_eye[1] - left_eye[1]

        angle = math.degrees(
            math.atan2(dy, dx)
        )

        return angle

    # ===
    # Stage 6.6
    # Rotate accessory
    # ===

    def rotate_accessory(
            self,
            accessory,
            angle
    ):
        """
        Rotate accessory image.

        Args:
            accessory: PNG image.
            angle: Rotation angle.

        Returns:
            Rotated image.
        """

        if accessory is None:
            logger.error("Error: Accessory image not loaded.")
            return None

        height, width = accessory.shape[:2]

        center = (
            width // 2,
            height // 2
        )

        matrix = cv2.getRotationMatrix2D(
            center,
            angle,
            1.0
        )

        rotated = cv2.warpAffine(
            accessory,
            matrix,
            (width, height),
            flags=cv2.INTER_LINEAR,
            borderMode=cv2.BORDER_CONSTANT,
            borderValue=(0, 0, 0, 0)
        )

        return rotated

    def get_transformed_accessory(
            self,
            accessory,
            accessory_path,
            width,
            angle
    ):
        """
        Return cached scaled and rotated accessory.
        """

        width = round(width / 32) * 32
        angle = round(angle / 20) * 20

        scale_key = (
            accessory_path,
            width
        )

        if scale_key in self.scaled_cache:
            scaled = self.scaled_cache[scale_key]
        else:
            scaled = self.scale_accessory(
                accessory,
                {"width": width}
            )
            self.scaled_cache[scale_key] = scaled

        rotate_key = (
            accessory_path,
            width,
            angle
        )

        if rotate_key in self.rotated_cache:
            return self.rotated_cache[rotate_key]

        rotated = self.rotate_accessory(
            scaled,
            angle
        )

        self.rotated_cache[rotate_key] = rotated

        return rotated

    # ===
    # Stage 6.7
    # Alpha blending
    # ===

    def alpha_blend(
            self,
            frame,
            accessory,
            position
    ):
        """
        Blend RGBA accessory with BGR frame.

        Args:
            frame: OpenCV frame.
            accessory: RGBA PNG image.
            position: (x, y) top-left position.

        Returns:
            Frame with accessory.
        """

        if (
                frame is None
                or accessory is None
                or position is None
        ):
            return frame

        x, y = position

        acc_h, acc_w = accessory.shape[:2]
        frame_h, frame_w = frame.shape[:2]

        # Completely outside the frame

        if (
                x >= frame_w
                or y >= frame_h
                or x + acc_w <= 0
                or y + acc_h <= 0
        ):
            return frame

        # Clip accessory area

        x1 = max(0, x)
        y1 = max(0, y)

        x2 = min(frame_w, x + acc_w)
        y2 = min(frame_h, y + acc_h)

        acc_x1 = x1 - x
        acc_y1 = y1 - y

        acc_x2 = acc_x1 + (x2 - x1)
        acc_y2 = acc_y1 + (y2 - y1)

        accessory_crop = accessory[
                         acc_y1:acc_y2,
                         acc_x1:acc_x2
                         ]

        alpha = accessory_crop[:, :, 3:4].astype("float32") / 255.0

        frame_crop = frame[
                     y1:y2,
                     x1:x2
                     ]

        frame[y1:y2, x1:x2] = (
                alpha * accessory_crop[:, :, :3]
                +
                (1.0 - alpha) * frame_crop
        ).astype("uint8")

        return frame

    def render_hat(
            self,
            frame,
            accessory,
            anchors,
            accessory_path,
            face_width,
            angle
    ):

        width = int(face_width * 3.4)

        accessory = self.get_transformed_accessory(
            accessory,
            accessory_path,
            width,
            angle
        )

        center_x = anchors["forehead"][0]

        top_y = min(
            anchors["forehead"][1],
            anchors["top_left"][1],
            anchors["top_right"][1],
            anchors["hair_left"][1],
            anchors["hair_right"][1]
        )

        anchor = (
            center_x,
            top_y
        )

        position = self.calculate_position(
            accessory,
            anchor,
            offset_y=10,
            align="bottom"
        )

        return self.alpha_blend(
            frame,
            accessory,
            position
        )

    def render_mask(
            self,
            frame,
            accessory,
            accessory_path,
            face_width,
            angle,
            eye_center
    ):

        width = int(face_width * 2.2)

        accessory = self.get_transformed_accessory(
            accessory,
            accessory_path,
            width,
            angle
        )

        position = self.calculate_position(
            accessory,
            eye_center,
            offset_y=10
        )

        return self.alpha_blend(
            frame,
            accessory,
            position
        )

    def render_glasses(
            self,
            frame,
            accessory,
            accessory_path,
            face_width,
            angle,
            eye_center
    ):

        width = int(face_width * 2.2)

        accessory = self.get_transformed_accessory(
            accessory,
            accessory_path,
            width,
            angle
        )

        position = self.calculate_position(
            accessory,
            eye_center,
            offset_y=-accessory.shape[0] // 10
        )

        return self.alpha_blend(
            frame,
            accessory,
            position
        )

    def trim_transparent(self, accessory):
        """
        Remove transparent borders from RGBA image.

        Args:
            accessory: RGBA image.

        Returns:
            Cropped RGBA image.
        """

        if accessory is None:
            logger.error("Error: Accessory image not loaded.")
            return None

        if len(accessory.shape) != 3 or accessory.shape[2] != 4:
            logger.error("Error: Accessory must be RGBA.")
            return None

        alpha = accessory[:, :, 3]

        points = cv2.findNonZero(alpha)

        if points is None:
            return accessory

        x, y, w, h = cv2.boundingRect(points)

        return accessory[y:y + h, x:x + w]

    #
    # Stage 6.9
    # Determine accessory type
    # ===

    def get_accessory_type(self, path):
        """
        Determine accessory type from file path.
        """

        if path is None:
            return None

        folder = os.path.basename(
            os.path.dirname(path)
        )

        return folder.lower()

    def get_earring_anchors(self, anchors):
        """
        Calculate anchor points for earrings.

        Args:
            anchors: Face anchor dictionary.

        Returns:
            Tuple of (left_anchor, right_anchor).
        """

        left_anchor = (
            anchors["left_ear"][0] - 10,
            anchors["left_ear"][1] + 35
        )

        right_anchor = (
            anchors["right_ear"][0] + 10,
            anchors["right_ear"][1] + 35
        )

        return left_anchor, right_anchor

    def clear_cache(self):
        """
        Clear renderer cache.
        """

        self.scaled_cache.clear()
        self.rotated_cache.clear()
        self.cache.clear()

    def close(self):
        """
        Release renderer resources.
        """

        self.clear_cache()
