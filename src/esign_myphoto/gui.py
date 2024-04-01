import tkinter as tk
from pathlib import Path

from esign_myphoto import io as app_io, i18n, sig
from esign_myphoto.config import SigConfig


class App(tk.Tk):
    def __init__(
        self,
        init_err: str | None,
        root_path: Path,
        sig_config: SigConfig,
    ):
        tk.Tk.__init__(self)
        screen_x = int((self.winfo_screenwidth() / 2) - (400 / 2))
        screen_y = int((self.winfo_screenheight() / 2) - (200 / 2))
        self._root_path = root_path
        self._sig_config = sig_config
        self._frame: tk.Frame | None = None
        self.title("AMY e-sign myPhoto")
        self.geometry(f"400x200+{screen_x}+{screen_y}")

        if init_err:
            self.switch_frame(InitFrame(self, init_err))
        elif self._sig_config is not None:
            self.switch_frame(InputFrame(self))

    def switch_frame(self, new_frame: tk.Frame) -> None:
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(expand=True, padx=20, pady=20)
        self.update()
        self.update_idletasks()

    def on_capture_signature(self, last_name: str, first_name: str) -> None:
        if not app_io.are_input_names_valid(last_name, first_name):
            return

        self.switch_frame(CaptureFrame(self))

        capture_result = sig.capture_signature(self._sig_config, last_name, first_name)
        top_msg = i18n.tr.MSG_CAPTURE_FAILED
        bottom_msg = capture_result.msg

        if capture_result.data:
            save_result = app_io.save_signature(
                capture_result.data, last_name, first_name, self._root_path
            )

            if save_result.success:
                top_msg = i18n.tr.MSG_CAPTURE_SUCCESSFUL
            bottom_msg = save_result.msg

        self.switch_frame(ResultFrame(self, top_msg, bottom_msg))


class InitFrame(tk.Frame):
    def __init__(self, parent: App, msg: str):
        tk.Frame.__init__(self, parent)
        self.columnconfigure(0, weight=1)

        top_label = tk.Label(self, text=i18n.tr.ERR_INITIALIZATION)
        top_label.grid(column=0, row=0, pady=10)

        bottom_label = tk.Label(self, text=msg)
        bottom_label.grid(column=0, row=1, pady=10)


class InputFrame(tk.Frame):
    def __init__(self, parent: App):
        tk.Frame.__init__(self, parent)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        last_name_label = tk.Label(
            self, text=i18n.tr.LABEL_LAST_NAME, width=10, anchor="w"
        )
        last_name_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=10)

        last_name_entry = tk.Entry(self, width=30)
        last_name_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=10)

        first_name_label = tk.Label(
            self, text=i18n.tr.LABEL_FIRST_NAME, width=10, anchor="w"
        )
        first_name_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=10)

        first_name_entry = tk.Entry(self, width=30)
        first_name_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=10)

        capture_button = tk.Button(
            self,
            text=i18n.tr.BUTTON_CAPTURE_SIGNATURE,
            width=20,
            command=lambda: parent.on_capture_signature(
                last_name_entry.get().strip(), first_name_entry.get().strip()
            ),
        )
        capture_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=10)


class CaptureFrame(tk.Frame):
    def __init__(self, parent: App):
        tk.Frame.__init__(self, parent)
        tk.Label(self, text=i18n.tr.MSG_CAPTURING_SIGNATURE).pack(
            side="top", fill="x", pady=10
        )


class ResultFrame(tk.Frame):
    def __init__(self, parent: App, top_msg: str, bottom_msg: str):
        tk.Frame.__init__(self, parent)
        self.columnconfigure(0, weight=1)

        top_label = tk.Label(self, text=top_msg)
        top_label.grid(column=0, row=0, pady=10)

        bottom_label = tk.Label(self, text=bottom_msg)
        bottom_label.grid(column=0, row=1, pady=10)

        home_button = tk.Button(
            self,
            text=i18n.tr.BUTTON_HOME,
            width=20,
            command=lambda: parent.switch_frame(InputFrame(parent)),
        )
        home_button.grid(column=0, row=2, padx=5, pady=10)
