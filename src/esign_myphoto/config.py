from tomlkit.items import Table


class SigConfig:
    def __init__(self, toml_table: Table):
        self.license = None
        self.reason = None
        self.image_width = 1200
        self.image_height = 400
        self.mime_type = "image/jpeg"
        self.ink_width = 0.8
        self.ink_color = 0x000000  # Black
        self.background_color = 0xFFFFFF  # White
        self.padding_x = 0.0
        self.padding_y = 0.0
        self.flags = 0x002000 | 0x080000  # RenderOutputBase64 | RenderColor32BPP

        if "license" in toml_table:
            self.license = str(toml_table["license"])

        if "reason" in toml_table:
            self.reason = str(toml_table["reason"])

        if "image_width" in toml_table:
            loaded_image_width = toml_table["image_width"]
            if isinstance(loaded_image_width, int) and loaded_image_width <= 2000:
                self.image_width = loaded_image_width

        if "image_height" in toml_table:
            loaded_image_height = toml_table["image_height"]
            if isinstance(loaded_image_height, int) and loaded_image_height <= 2000:
                self.image_height = loaded_image_height
