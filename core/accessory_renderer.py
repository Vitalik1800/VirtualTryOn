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

import math
import cv2
import os

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
EARRINGS = "earrings"
NECKLACE = "necklaces"
WATCH = "watches"

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

        Returns:
            OpenCV frame.
        """
        try:

            scale = 2.2
            offset_x = 0
            offset_y = 0

            if (
                frame is None
                or accessory is None
                or not landmarks
            ):
                return frame

            anchors = self.get_anchor_points(
                landmarks
            )

            if (
                anchors["left_eye"] is None
                or anchors["right_eye"] is None
            ):
                return frame

            # Face width
            
            accessory_type = self.get_accessory_type(accessory_path)

            if accessory_type is None:
                return frame

            if accessory_type == GLASSES:
                return self.render_glasses(
                    frame,
                    accessory,
                    anchors
                )

            elif accessory_type == HAT:
                return self.render_hat(
                    frame,
                    accessory,
                    anchors
                )
            
            elif accessory_type == MASK:
                return self.render_mask(
                    frame,
                    accessory,
                    anchors
                )

            elif accessory_type == EARRINGS:
                return self.render_earrings(
                    frame,
                    accessory,
                    anchors
                )

            elif accessory_type == NECKLACE:
                return self.render_necklace(
                    frame,
                    accessory,
                    anchors
                )

            elif accessory_type == WATCH:
                return self.render_watch(
                    frame,
                    accessory,
                    anchors
                )

            return frame

            geometry = {
                "width": int(face_width * 2.2)
            }

            key = (
                accessory_path,
                geometry["width"]
            )

            if key in self.scaled_cache:
                accessory = self.scaled_cache[key]
            else:
                accessory = self.scale_accessory(
                    accessory,
                    geometry
                )
                self.scaled_cache[key] = accessory

            if accessory.size == 0:
                return frame

            angle = round(
                self.calculate_angle(
                    anchors["left_eye"],
                    anchors["right_eye"]
                )
            )

            key = (
                accessory_path,
                geometry["width"],
                angle
            )

            if key in self.rotated_cache:
                accessory = self.rotated_cache[key]
            else:
                accessory = self.rotate_accessory(
                    accessory,
                    angle
                )
                self.rotated_cache[key] = accessory

            position = self.calculate_position(
                accessory,
                anchor,
                offset_y=-accessory.shape[0] // 6
            )

            return self.alpha_blend(
                frame,
                accessory,
                position
            )

        except Exception as error:

            print(f"[AccessoryRenderer] {error}")
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
            print("Error: Accessory image not loaded.")
            return frame

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

        resized = cv2.resize(
            accessory,
            (target_width, target_height),
            interpolation=cv2.INTER_AREA
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

        Returns:
            (x, y) position.
        """

        if accessory is None:
            print("Error: Accessory image not loaded.")
            return frame

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

        return (x, y)

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
            print("Error: Accessory image not loaded.")
            return frame

        height, width = accessory.shape[:2]

        center = (
            width //2,
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

        alpha = accessory_crop[:, :, 3] / 255.0
        alpha = alpha[:, :, None]

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

    def render_hat(self, frame, accessory, anchors):

        accessory = self.trim_transparent(accessory)

        face_width = abs(
            anchors["right_eye"][0] -
            anchors["left_eye"][0]
        )

        accessory = self.scale_accessory(
            accessory,
            {
                "width": int(face_width * 3.4)
            }
        )

        angle = self.calculate_angle(
            anchors["left_eye"],
            anchors["right_eye"]
        )

        accessory = self.rotate_accessory(
            accessory,
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

    def render_mask(self, frame, accessory, anchors):

        face_width = abs(
            anchors["right_eye"][0] -
            anchors["left_eye"][0]
        )

        geometry = {
            "width": int(face_width * 2.6)
        }

        accessory = self.scale_accessory(
            accessory,
            geometry
        )

        angle = self.calculate_angle(
            anchors["left_eye"],
            anchors["right_eye"]
        )

        accessory = self.rotate_accessory(
            accessory,
            angle
        )

        position = self.calculate_position(
            accessory,
            anchors["nose"],
            offset_y=10
        )

        return self.alpha_blend(
            frame,
            accessory,
            position
        )

    def render_earrings(self, frame, accessory, anchors):

        accessory = self.trim_transparent(accessory)

        geometry = {
            "width": 70
        }

        accessory = self.scale_accessory(
            accessory,
            geometry
        )

        left_anchor, right_anchor = self.get_earring_anchors(
            anchors
        )

        left_position = self.calculate_position(
            accessory,
            left_anchor
        )

        right_position = self.calculate_position(
            accessory,
            right_anchor
        )

        frame = self.alpha_blend(
            frame,
            accessory,
            left_position
        )

        frame = self.alpha_blend(
            frame,
            accessory,
            right_position
        )

        return frame

    def render_watch(self, frame, accessory, anchors):
        """
        Watches require hand tracking.
        """

        return frame

    def render_necklace(self, frame, accessory, anchors):

        geometry = {
            "width": 260
        }

        accessory = self.scale_accessory(
            accessory,
            geometry
        )

        position = self.calculate_position(
            accessory,
            anchors["chin"],
            offset_y=15,
            align="top"
        )

        return self.alpha_blend(
            frame,
            accessory,
            position
        )

    def render_glasses(self, frame, accessory, anchors):

        accessory = self.trim_transparent(accessory)

        face_width = abs(
            anchors["right_eye"][0] -
            anchors["left_eye"][0]
        )

        geometry = {
            "width": int(face_width * 2.2)
        }

        accessory = self.scale_accessory(
            accessory,
            geometry
        )

        angle = self.calculate_angle(
            anchors["left_eye"],
            anchors["right_eye"]
        )

        accessory = self.rotate_accessory(
            accessory,
            angle
        )

        center = (
            (anchors["left_eye"][0] + anchors["right_eye"][0]) // 2,
            (anchors["left_eye"][1] + anchors["right_eye"][1]) // 2
        )

        position = self.calculate_position(
            accessory,
            center,
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
            print("Error: Accessory image not loaded.")
            return frame

        if len(accessory.shape) != 3 or accessory.shape[2] != 4:
            print("Error: Accessory must be RGBA.")
            return frame

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

    def close(self):
        """
        Release renderer resources.
        """

        self.clear_cache()
